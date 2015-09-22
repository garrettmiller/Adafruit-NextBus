#!/usr/bin/python
####################################################################
#apitest.py                                                        #
#API test for Pittsburgh Bus API                                   #
#Garrett Miller, 2015 - garrettmiller@gmail.com                    #
#Other code/APIs borrowed are property of their respective authors.#
####################################################################

#Set up to run
from pghbustime import *
mykey = "API-KEY-GOES-HERE"
api = BustimeAPI(mykey, _format="xml")

#Pull predictions from the API for a given stop (nice that it does this for us)
print api.predictions(stpid=3144)
