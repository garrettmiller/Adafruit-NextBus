Adafruit-NextBus-Pittsburgh
================

Python front-end for the NextBus schedule service, for Raspberry Pi, etc, adapted for Pittsburgh from Adafruit-NextBus.


Installation:       
----------------

sudo pip install ElementTree requests pgh-bustime


Files:   
----------------

apitest.py: Used to test/play around with the API.  Requires your own Port Authority API key.

nextbus.py: Scrolling marquee using 64x32 RGB LED matrix. Requires rpi-rgb-led-matrix library: https://github.com/adafruit/rpi-rgb-led-matrix

pghpredict.py: class that handles periodic queries to the Pittsburgh Port Authority API. Imported by other scripts; doesn't do anything on its own.

Dependencies:  sudo pip install ElementTree requests xmltodict pytz pgh-bustime


Acknowledgements:   
----------------

Adafruit Raspberry Pi RGB LED Matrix:
https://github.com/adafruit/rpi-rgb-led-matrix

Adafruit and PaintYourDragon's NextBus:
https://github.com/adafruit/Adafruit-NextBus

nhfruchter's pgh-bustime:
https://github.com/nhfruchter/pgh-bustime

Adapted from PaintYourDragon's Adafruit-NextBus, by Garrett Miller, 2015.
