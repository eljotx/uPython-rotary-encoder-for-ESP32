import machine,time
from machine import Pin
from time import sleep

switch = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
enc_plus = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)
enc_minu = Pin(19, mode=Pin.IN, pull=Pin.PULL_UP)


def switch_ch(pin): #routine for encoder switch
    global push
    sleep(0.03)
    if switch.value() == 0:
        #switch.irq(handler=None)
        push = push + 1
        print ("Pushed ", push, "times")
    
def encoder_pl(pin): #routine for encoder
    global counter
    if enc_plus.value() == 0:
        if enc_minu.value() == 1:
            counter = counter + direction
            print("counter =", counter)
            #switch.irq(handler=switch_ch)   
                         
def encoder_mi(pin):
    global counter
    if enc_minu.value() == 0:
        if enc_plus.value() == 1:
            counter = counter - direction
            print("counter =", counter)
            #switch.irq(handler=switch_ch)   

switch.irq(trigger=Pin.IRQ_FALLING,handler=switch_ch)
enc_plus.irq(trigger=Pin.IRQ_FALLING,handler=encoder_pl)
enc_minu.irq(trigger=Pin.IRQ_FALLING,handler=encoder_mi)

direction = 1
counter = 0
push = 0
while True:
    continue