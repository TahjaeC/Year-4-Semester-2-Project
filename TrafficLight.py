import RPi.GPIO as GPIO
import time
import signal
import sys
from pynput import keyboard


class TrafficLightLEDs:
    RED = 18
    AMBER = 12
    GREEN = 16
    WALK = 21


#class TrafficLightStates:
 #   RED = 2
  #  REDAMBER = 3
  #  GREEN = 4
  #  AMBER = 5

# All Lights OFF


def allLightsOff(signal, frame):
    GPIO.output(TrafficLightLEDs.RED, False)
    GPIO.output(TrafficLightLEDs.AMBER, False)
    GPIO.output(TrafficLightLEDs.GREEN, False)
    GPIO.output(TrafficLightLEDs.WALK, False)
    GPIO.cleanup()
    sys.exit(0)


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        button_read()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


w_is_pressed = False


def button_read():
   # print('Hello')
    global w_is_pressed
    w_is_pressed = True


listener = keyboard.Listener(
    on_press=on_press,
    on_release=None)
listener.start()
signal.signal(signal.SIGINT, allLightsOff)

while True:
    # Setup Hardware
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TrafficLightLEDs.RED, GPIO.OUT)
    GPIO.setup(TrafficLightLEDs.AMBER, GPIO.OUT)
    GPIO.setup(TrafficLightLEDs.GREEN, GPIO.OUT)
    GPIO.setup(TrafficLightLEDs.WALK, GPIO.OUT)

    #currentState = TrafficLightStates.RED

    # RED and Walk ON
    GPIO.output(TrafficLightLEDs.RED, True)
    GPIO.output(TrafficLightLEDs.AMBER, False)
    GPIO.output(TrafficLightLEDs.GREEN, False)
    GPIO.output(TrafficLightLEDs.WALK, True)
    print('Red')
    print('Walk')
    time.sleep(12)
    GPIO.output(TrafficLightLEDs.WALK, False)
    time.sleep(0.5)
    GPIO.output(TrafficLightLEDs.WALK, True)
    time.sleep(0.5)
    GPIO.output(TrafficLightLEDs.WALK, False)
    time.sleep(0.5)
    GPIO.output(TrafficLightLEDs.WALK, True)
    time.sleep(0.5)
    GPIO.output(TrafficLightLEDs.WALK, False)
    time.sleep(0.5)
    GPIO.output(TrafficLightLEDs.WALK, True)
    time.sleep(0.5)

    #currentState = TrafficLightStates.GREEN

    # GREEN ON
    GPIO.output(TrafficLightLEDs.RED, False)
    GPIO.output(TrafficLightLEDs.AMBER, False)
    GPIO.output(TrafficLightLEDs.GREEN, True)
    GPIO.output(TrafficLightLEDs.WALK, False)
    print('Green')
    print('Dont Walk')
    w_is_pressed = False
    start_time = time.time()
    elapsed_time = 0

    print("Press w to cross")
    while elapsed_time < 20:
        elapsed_time = time.time() - start_time
        if(w_is_pressed):
            elapsed_time = time.time() - start_time
            if(elapsed_time < 18):
                print('w pressed! please wait for signal to cross')
                time.sleep(1)
            break
        #time.sleep(20)
        #print(elapsed_time)
        #print(w_is_pressed)
    print("Stop Listening for w press")
    #print(elapsed_time)

    #currentState = TrafficLightStates.AMBER

    # AMBER ON
    GPIO.output(TrafficLightLEDs.RED, False)
    GPIO.output(TrafficLightLEDs.AMBER, True)
    GPIO.output(TrafficLightLEDs.GREEN, False)
    GPIO.output(TrafficLightLEDs.WALK, False)
    print('Amber')
    time.sleep(3)

    #currentState = TrafficLightStates.RED

