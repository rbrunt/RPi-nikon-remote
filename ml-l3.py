import RPi.GPIO as GPIO
# Time is required for the blinking:
import time

# Choose which pin the LED is controlled from:
LED_Pin = 11

# Setup output pin:
GPIO.setup(11, GPIO.OUT)

# Infinite Loop - for now we'll just blink the LED to make sure it's all working...
while True
	GPIO.output(LED_Pin, True)
	time.sleep(1)
	GPIO.output(LED_Pin, False)
	time.sleep(1)

# Pulses:
# ON	2000 us
# OFF	27830 us
# ON	400 us
# OFF	1580 us
# ON	400 us
# OFF	3580 us
# ON	400 us
# Repeats again after 63.2 ms
