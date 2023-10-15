from gpiozero import LED
from time import sleep



led = LED(17)

def lights_on():
    led.on()




def lights_off():
    led.off()