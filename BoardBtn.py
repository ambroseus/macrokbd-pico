import board
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP24)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
