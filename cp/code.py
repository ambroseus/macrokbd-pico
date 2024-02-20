import asyncio, json
import time
from Colors import Colors
from BoardLed import BoardLed, BlinkLed

color = Colors.Blue

try:
    with open("/colors.json", "w") as fp:
        fp.write(json.dumps(Colors.__dict__))
        fp.flush()
    color = Colors.Green
except OSError as e:
    print("ERROR: ", e)
    color = Colors.Orange
    

async def blink(color):
    blinking = BlinkLed(BoardLed(color))
    while True:
        await blinking.update()

########################################################################
async def main():
    blink_task = asyncio.create_task(blink(color))
    await asyncio.gather(blink_task)

# asyncio.run(main())

led = BoardLed(color)
led.set_brightness(0.1)

while True:
    led.show()
    time.sleep(1)
