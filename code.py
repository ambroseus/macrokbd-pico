import asyncio, json
from Colors import Colors
from BoardLed import BoardLed, BlinkLed

color = Colors.Orange

try:
    with open("/colors.txt", "w") as fp:
        fp.write(json.dumps(Colors.__dict__))
        fp.flush()
    color = Colors.Green
except OSError as e:
    print("ERROR: ", e)
    color = Colors.Red

async def blink(color):
    blinking = BlinkLed(BoardLed(color))
    while True:
        await blinking.update()

########################################################################
async def main():
    blink_task = asyncio.create_task(blink(color))
    await asyncio.gather(blink_task)

asyncio.run(main())
