import board
from digitalio import DigitalInOut, Direction, Pull

class BoardBtn:
    def __init__(self):
        self.btn = DigitalInOut(board.GP24)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.UP
        
    def is_pressed(self):
        return not self.btn.value
