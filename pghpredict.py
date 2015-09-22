#!/usr/bin/python
####################################################################
#pghpredict.py                                                     #
#Adapted from Adafruit-Nextbus using pghbustime for Pittsburgh.	   #
#Adapted by Garrett Miller, garrettmiller@gmail.com, 2015		   #
#Other code/APIs borrowed are property of their respective authors.#
####################################################################

from pghbustime import *
import threading
import time
import datetime
import xml.etree.ElementTree as ET

##############Set up the API##############
mykey = "API-KEY-GOES-HERE"
api = BustimeAPI(mykey, _format="xml")
##########################################

class predict:
	interval  = 120 # Default polling interval = 2 minutes
	initSleep = 0   # Stagger polling threads to avoid load spikes

	# predict object initializer.  1 parameter, a 3-element tuple:
	# First is line tag (e.g. '71D')
	# Second is stop tag (e.g. '3144')
	# Third is a prettyname -- not a tag, this element is human-readable
	
	# Each predict object spawns its own thread and will perform
	# periodic server queries in the background, which can then be
	# read via the predictions[] list (est. arrivals, in seconds).
	def __init__(self, data):
		self.data          = data
		self.predictions   = []
		self.lastQueryTime = time.time()
		t                  = threading.Thread(target=self.thread)
		t.daemon           = True
		t.start()

	# Periodically get predictions from server ---------------------------
	def thread(self): 
		initSleep          = predict.initSleep
		predict.initSleep += 5   # Thread staggering may
		time.sleep(initSleep)    # drift over time, no problem
		while True:
			route = self.data[0]    # Route
			stop = self.data[1]    # Stop 
			result = predict.req(route, stop)
			if result is None: return     # Connection error, handle empty results
			parsed = ET.fromstring(result)
		
			self.lastQueryTime = time.time()
			newList     = []
			for child in parsed.findall('prd'):      # Build new prediction list
				#This converts the string object returned from API into epoch time. 
				predictedTime = time.mktime(datetime.datetime.strptime(child.find('prdtm').text, "%Y%m%d %H:%M:%S").timetuple())
				#Then do the math, correcting for our timezone from epoch
				secondsUntilNext = predictedTime - (int(time.time()) - 14400) 
				newList.append(int(secondsUntilNext)) #Append it to the list
			self.predictions = newList # Replace current list
			time.sleep(predict.interval)

	# Open URL, send request, read & parse XML response ------------------
	@staticmethod
	def req(route, stop):
		xml = None
		try:
			#Pull predictions from the API
			xml = api.predictions(stpid=stop, rt=route)
		finally:
			return xml

	# Set polling interval (seconds) -------------------------------------
	@staticmethod
	def setInterval(i):
		interval = i
