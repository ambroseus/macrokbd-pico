import asyncio
import board
import time
from neopixel import NeoPixel

class BoardLed:
    def __init__(self, color):
        self.brightness = 0
        self.color = color
        self.__led = NeoPixel(board.GP23, 1, brightness=self.brightness, auto_write=False)
        self.__led[0] = color

    def set_brightness(self, value):
        self.brightness = value
        if value < 0:
            self.brightness = 0
        elif value > 1:
            self.brightness = 1
        
    def show(self):
        self.__led.brightness = self.brightness
        self.__led[0] = self.color
        self.__led.show()

    def __del__(self):
        self.__led.deinit()

class BlinkLed:
    _max_brightness = 0.2
    _pause_on = 0.1
    _pause_off = 0.5
    _step = 0.03
    _delay = 0.001
    
    
    def __init__(self, led: BoardLed):
        self.led = led
        self.current_ts = time.monotonic()
        self.inc = 1
        self.led = led
        
    async def update(self):
        if time.monotonic() - self.current_ts > self._delay:
            self.current_ts = time.monotonic()
            self.led.set_brightness(self.led.brightness + self.inc * self._step)

            if self.led.brightness >= self._max_brightness:
                self.led.set_brightness(self._max_brightness)
                self.inc = -1
            elif self.led.brightness <= 0:
                self.led.set_brightness(0)
                self.inc = 1

            self.led.show()
            
            if self.led.brightness == self._max_brightness:
                await asyncio.sleep(self._pause_on)
            elif self.led.brightness == 0:
                await asyncio.sleep(self._pause_off)

        await asyncio.sleep(0)

