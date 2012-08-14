RPi-nikon-remote
===============

A program to emulate the ML-L3 remote by nikon for their DSLR cameras that uses the GPIO of the Raspberry Pi

Todo checklist:
* Design a circuit that send IR signals from a GPIO pin on the Raspberry Pi
* Figure out best way to send v. short pulses - python's `time.sleep()` probably isn't accurate/granular enough...
* Add the ability to do timelapses etc.
* Eventually extend to a general ir remote emulator...

[This](http://www.bigmike.it/ircontrol/index.html) site has useful info on pulse lengths etc.

Prerequisites
------------

Need to have the `RPi.GPIO` library installed from [here](http://pypi.python.org/pypi/RPi.GPIO). You can find installation instructions [here](http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/).