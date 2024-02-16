import board
from time import sleep
from neopixel import NeoPixel
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP24)
btn.direction = Direction.INPUT
btn.pull = Pull.UP


OFF = (0, 0, 0)
Red = (100, 0, 0)
Green = (0, 100, 0)
Blue = (0, 0, 100)
Yellow = (100, 100, 0)
Magenta = (100, 0, 100)
Cyan = (0, 100, 100)
Orange = (120, 40, 0)
White = (150, 150, 150)

colors = (Red, Green, Blue, Yellow, Magenta, Cyan, Orange, White, OFF)
colors_len = len(colors)
cur_color = 0

led = NeoPixel(board.GP23, 1)
led.brightness = 0.05
led[0] = OFF

def next_color():
    global cur_color, colors_len
    cur_color += 1
    if cur_color == colors_len:
        cur_color = 0

def set_led(color):
    global led
    led[0] = color

def set_led_cur_color():
    global colors, cur_color
    set_led(colors[cur_color])

prev_state = btn.value

########################################################################
while True:
    cur_state = btn.value
    
    if cur_state != prev_state:
        if cur_state:
            # release button
            set_led_cur_color()
            next_color()
    
    prev_state = cur_state
