import storage, usb_cdc, time, board
from neopixel import NeoPixel
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP24)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

led = NeoPixel(board.GP23, 1, brightness=0.2)
led[0] = (0, 0, 0)

if btn.value:
    usb_cdc.enable(console=False, data=True)
    storage.disable_usb_drive()
else:
    usb_cdc.enable(console=True, data=True)
    led[0] = (100, 100, 100)
    time.sleep(1)
    led[0] = (0, 0, 0)
