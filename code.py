import asyncio
import Colors
from BoardLed import BoardLed, BlinkLed

async def blink(color):
    blinking = BlinkLed(BoardLed(color))
    while True:
        await blinking.update()

########################################################################
async def main():
    blink_task = asyncio.create_task(blink(Colors.Orange))
    await asyncio.gather(blink_task)

asyncio.run(main())
