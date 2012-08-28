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

Pinout Diagram:
---------------
```
	3.3V			( ) | ( )	5V
	GPIO0 (SDA)		( ) | (X) 	--
	GPIO1 (SCL)		( ) | ( ) 	GND
	GPIO4 (GPCLK0)	( ) | ( ) 	GPIO14 (TXD)
	-- 				(X) | ( ) 	GPIO15 (RXD)
	GPIO17			( ) | ( ) 	GPIO18 (PCM_CLK)
	GPIO21(PCM_DOUT)( ) | (X) 	--
	GPIO22			( ) | ( ) 	GPIO23
	-- 				(X) | ( )	GPIO24 
	GPIO10 (MOSI)	( ) | (X) 	--
	GPIO9 (MISO)	( ) | ( )	GPIO25 
	GPIO11 (SCKL)	( ) | ( ) 	GPIO18 (CE0)
	-- 				(X) | ( ) 	GPIO17 (CE1)
```