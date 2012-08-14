nikon-remote-pi
===============

A program to emulate the ML-L3 remote by nikon for their DSLR cameras that uses the GPIO of the Raspberry Pi

Todo checklist:
* Design a circuit that send IR signals from a GPIO pin on the Raspberry Pi
* Figure out best way to send v. short pulses - python's `time.sleep()` probably isn't accurate/granular enough...
* Eventually extend to a general ir remote emulator...

[This](http://www.bigmike.it/ircontrol/index.html) site has useful info on pulse lengths etc.