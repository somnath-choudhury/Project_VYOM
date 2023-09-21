import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 16
GPIO_ECHO = 26

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

out1 = 17
out2 = 18
out3 = 27
out4 = 22

step_sleep = 0.02

step_count = 60

GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)

GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(out3, GPIO.LOW)
GPIO.output(out4, GPIO.LOW)


def cleanup():
    GPIO.output(out1, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)
    GPIO.cleanup()


def trigger_stepper():
    try:
        i = 0
        for i in range(step_count):
            if i % 4 == 0:
                GPIO.output(out4, GPIO.HIGH)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out1, GPIO.LOW)
            elif i % 4 == 1:
                GPIO.output(out4, GPIO.LOW)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out2, GPIO.HIGH)
                GPIO.output(out1, GPIO.LOW)
            elif i % 4 == 2:
                GPIO.output(out4, GPIO.LOW)
                GPIO.output(out3, GPIO.HIGH)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out1, GPIO.LOW)
            elif i % 4 == 3:
                GPIO.output(out4, GPIO.LOW)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out1, GPIO.HIGH)

            time.sleep(step_sleep)
        #cleanup()

    except KeyboardInterrupt:
        cleanup()
        exit(1)


def measure_distance():
    GPIO.output(GPIO_TRIG, GPIO.LOW)
    time.sleep(0.1)

    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, GPIO.LOW)

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        bounce_back_time = time.time()

    pulse_duration = bounce_back_time - start_time
    distance = round(pulse_duration * 17150, 2)

    print(f"Distance: {distance} cm")

    if distance < 26:
        trigger_stepper()
        time.sleep(2)


try:
    while True:
        user_input = input("Press enter to measure distance (or 'q' to quit): ")
        if user_input == "":
            measure_distance()
        elif user_input == "q":
            break
        else:
            print("Invalid input. Please try again.")

finally:
    GPIO.cleanup()
