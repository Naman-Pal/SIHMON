import RPi.GPIO as GPIO 
import time 
import board 
import busio 
import threading 

# Set the GPIO mode 
GPIO.setmode(GPIO.BCM) 
# Set the GPIO pin numbers 
sound_pin = 13 
led_pin = 21 
# Setup the GPIO pins 
GPIO.setup(13, GPIO.IN) 
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Changed initial value to LOW 
def blink_led(): 
while True: 
GPIO.output(led_pin, GPIO.HIGH) 
print("LED ON") 
time.sleep(0.5) 
GPIO.output(led_pin, GPIO.LOW) 
print("LED OFF") 
time.sleep(0.5) 
def sound_sense(): 
while True: 
# Read the sound sensor value 
sound_value = GPIO.input(13)
# Control the LED based on the sound sensor value 
if sound_value == GPIO.HIGH: 
# Turn on the LED 
print("Sound Detected") 
else: 
# Turn off the LED 
print("No Sound") 
# Wait for a short delay 
time.sleep(0.5) 
try: 
led_thread = threading.Thread(target=blink_led) 
led_thread.start() 
# Create and start the accelerometer thread 
sound_thread = threading.Thread(target=sound_sense) 
sound_thread.start() 
# Wait for both threads to finish (which will not happen in this case) 
led_thread.join() 
sound_thread.join() 
except KeyboardInterrupt: 
GPIO.output(21, GPIO.LOW) 
# Clean up the GPIO pins 
GPIO.cleanup()
