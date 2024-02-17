import board, usb_cdc, supervisor, storage, time
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel

btn = DigitalInOut(board.GP24)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
time.sleep(0.1)
print("btn is pressed: ", not btn.value)

if btn.value:
    print("work mode")
    usb_cdc.enable(console=False, data=True)
    supervisor.runtime.autoreload = False
    storage.disable_usb_drive()
    storage.remount("/", readonly=False)
else:
    print("dev mode")
    usb_cdc.enable(console=True, data=True)
    with NeoPixel(board.GP23, 1, brightness=0.2) as led:
        led[0] = (100, 100, 100)
        time.sleep(0.5)
        led[0] = (0, 0, 0)
