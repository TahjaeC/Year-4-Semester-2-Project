# Write your code here :-)
from gpiozero import LED
from time import sleep
import keyboard
import time

red = LED(18)
amber = LED(16)
green = LED(8)
walk = LED(21)

while True:
    red.on()
    #walk.blink()
    sleep(15)

   if red.on():
    print("blaaah")

    else:
      #walk.off
        print('boomblass')
      sleep(3)
  
    red.off()
    #green.on()
    #sleep(20)

    if keyboard.is_pressed('w')#and green.time >=8 and <=15:
    wait (3)
    #green.off()

    amber.on()
    sleep(4)
    amber.off()

    if keyboard.is_pressed and green.off: