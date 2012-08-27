import RPi.GPIO as GPIO
import time

# Set to board pin numbering scheme:
GPIO.setmode(GPIO.BOARD)

# Choose which pin the LED is controlled from:
GREEN_1 = 7
GREEN_2 = 11
YELLOW_1 = 12
YELLOW_2 = 13
RED_1 = 15
RED_2 = 16

# Define array of pins:
PIN_LIST = [GREEN_1, GREEN_2, YELLOW_1, YELLOW_2, RED_1, RED_2]


# Setup output pins from list:
def setupoutputs(OUT_LIST) :
	print "Setting up Output pins:"
	i = 0
	while i < len(OUT_LIST) :
		GPIO.setup(OUT_LIST[i], GPIO.OUT)
		print "setting up pin number " + str(OUT_LIST[i]) + " as an output"
		i += 1
	print "setup complete!"


# Light up to a certain number of LEDs  (by cycling through the list)
# Pass a number between 1 and 6:
def displayprogress(num) :
	if num < 7 :
		# Turn off any LEDs currently lit:
		print "turning off LEDs:"
		i = 0
		while i < len(PIN_LIST) :
			GPIO.output(PIN_LIST[i], False)
			i += 1
		# Now we turn on the LEDs that we want:
		i = 0
		while i < (num - 1) :
			GPIO.output(PIN_LIST[i], True)
			i += 1


	else
		print "You need to pass a number between 1 and 6!"

setupoutputs(PIN_LIST)
print ""
print "turn on 1 LED"
displayprogress(1)
time.sleep(1)
print "turn on 2 LEDs"
displayprogress(2)
time.sleep(1)
print "turn on 3 LEDs"
displayprogress(3)
time.sleep(1)
print "turn on 4 LEDs"
displayprogress(4)
time.sleep(1)
print "turn on 5 LEDs"
displayprogress(5)
time.sleep(1)
print "turn on 6 LEDs"
displayprogress(6)
time.sleep(1)

while True :
	number = int(input("Please enter the number of LED's to light:"))
	if number < 7 :
		print "Lighting " + str(number) + " LED's..."
		displayprogress(number)
		print ""
	else :
		print "you need to enter a number between 1 and 6!"
		print ""


# Infinite Loop - for now we'll just blink the LED to make sure it's all working...
while True :
	print "Turning on"
	GPIO.output(LED_Pin, True)
	time.sleep(1)
	print "Turning off"
	GPIO.output(LED_Pin, False)
	time.sleep(1)
