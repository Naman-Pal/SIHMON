import time
import board
import busio
import adafruit_adxl34x
import adafruit_tmp006
import RPi.GPIO as GPIO
import threading
from heartrate_monitor import HeartRateMonitor
import argparse

# Setup ADXL I2C functions
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c, address=0x53)

# Create library objects using Bus I2C ports
i2c_tmp006 = busio.I2C(board.SCL, board.SDA)
tmp006_sensor = adafruit_tmp006.TMP006(i2c_tmp006, address=0x40)

# Set up the LED and GPIO pins
sound_pin = 13  # Sound sensor GPIO pin
led_pin = 21  # GPIO pin number used for the LED circuit

# Setup GPIO pin mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO pin mode
GPIO.setup(sound_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

# Create locks: synchronize all print statements
print_lock = threading.Lock()

def adxl_senses():
    while True:
        x, y, z = accelerometer.acceleration
        if abs(x) > 15 or abs(y) > 20 or abs(z) > 25:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        with print_lock:
            print("%f %f %f" % (x, y, z))
        time.sleep(1.0)

# def blink_led():
#     while True:
#         with print_lock:
#             GPIO.output(led_pin, GPIO.HIGH)
#             print("LED ON")
#         time.sleep(1.0)
#         with print_lock:
#             GPIO.output(led_pin, GPIO.LOW)
#             print("LED OFF")
#         time.sleep(1.0)
 
def sound_sense():
    while True:
        # Read the sound sensor value
        sound_value = GPIO.input(sound_pin)
        # Control the LED based on the sound sensor value
        with print_lock:
            if sound_value == GPIO.HIGH:
                print("Sound Detected")
                #GPIO.output(led_pin, GPIO.HIGH)
            else:
                print("No Sound")
                GPIO.output(led_pin, GPIO.LOW)
        # Wait for a short delay
        time.sleep(1.0)

def temperature_sense():
    while True:
        obj_temp_celsius = tmp006_sensor.temperature
        obj_temp_fahrenheit = (obj_temp_celsius * 9/5) + 32
        with print_lock:
            print("Object temperature: %.2f °C | %.2f °F\n" % (obj_temp_celsius, obj_temp_fahrenheit))
        
        if abs(obj_temp_celsius) > 20:
            led_state = GPIO.HIGH
        else:
            led_state = GPIO.LOW
        with print_lock:
            GPIO.output(led_pin, led_state)
        time.sleep(1)

def heart_rate_monitor():
    parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
    parser.add_argument("-r", "--raw", action="store_true",
                        help="print raw data instead of calculation result")
    parser.add_argument("-t", "--time", type=int, default=30,
                        help="duration in seconds to read from sensor, default 30")
    args = parser.parse_args()

    print('Sensor starting...')
    hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
    hrm.start_sensor()

    led_state = GPIO.LOW  # Initialize LED state

    try:
        for _ in range(args.time):
            bpm = hrm.bpm  # Access the current BPM value from the HeartRateMonitor
            spo2 = hrm.spo2  # Access the current SpO2 value from the HeartRateMonitor
            with print_lock:
                print("BPM: {}, SpO2: {}".format(bpm, spo2))

            if bpm > 170 or spo2 < 95:
                led_state = GPIO.HIGH  # Turn on the LED
            else:
                led_state = GPIO.LOW  # Turn off the LED

            GPIO.output(led_pin, led_state)  # Set the LED state

            # Wait for a short delay
            time.sleep(1)

    except KeyboardInterrupt:
        print('Keyboard interrupt detected, exiting...')

    hrm.stop_sensor()
    print('Sensor stopped!')


try:
    # Create and start the heart rate monitor thread
    hrm_thread = threading.Thread(target=heart_rate_monitor)
    hrm_thread.start()

#     # Create and start the LED blinking thread
#     led_thread = threading.Thread(target=blink_led)
#     led_thread.start()

    # Create and start the accelerometer thread
    adxl_thread = threading.Thread(target=adxl_senses)
    adxl_thread.start()

    # Create and start the sound sensor thread
    sound_thread = threading.Thread(target=sound_sense)
    sound_thread.start()

    # Create and start the temperature sensing thread
    temperature_thread = threading.Thread(target=temperature_sense)
    temperature_thread.start()

    # Wait for all threads to finish (which will not happen in this case)
#    led_thread.join()
    adxl_thread.join()
    sound_thread.join()
    temperature_thread.join()
    hrm_thread.join()

except KeyboardInterrupt:
    with print_lock:
        GPIO.output(led_pin, GPIO.LOW)

        # Clean up GPIO on keyboard interrupt
        GPIO.cleanup()