const { NeoPixel } = require('neopixel')
const BOARD_NEOPIXEL_PIN = 23
const np = new NeoPixel(BOARD_NEOPIXEL_PIN, 1)
const Off = np.color(0, 0, 0)
const Green = np.color(20, 40, 0)

let on = false

const toggle = () => {
  np.setPixel(0, on ? Green : Off)
  np.show()
  on = !on
}

setInterval(toggle, 1000)
