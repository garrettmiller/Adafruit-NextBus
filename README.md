Adafruit-NextBus-Pittsburgh
================

Python front-end for the NextBus schedule service, for Raspberry Pi, etc, adapted for Pittsburgh from Adafruit-NextBus.

apitest.py: Used to test/play around with the API.  Requires your own Port Authority API key.

pghpredict.py: class that handles periodic queries to the Pittsburgh Port Authority API. Imported by other scripts; doesn't do anything on its own.

nextbus.py: Scrolling marquee using 64x32 RGB LED matrix. Requires rpi-rgb-led-matrix library: https://github.com/adafruit/rpi-rgb-led-matrix

Adapted from Adafruit-NextBus, https://github.com/adafruit/Adafruit-NextBus, by Garrett Miller, 2015.