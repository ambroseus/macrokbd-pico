const { NeoPixel } = require('neopixel')
const BOARD_NEOPIXEL_PIN = 23
// pinMode(BOARD_NEOPIXEL_PIN, OUTPUT)

const np = new NeoPixel(BOARD_NEOPIXEL_PIN, 1)
let on = false

const toggle = () => {
  const color = on ? np.color(20, 40, 0) : np.color(0, 0, 0)
  np.setPixel(0, color)

  np.show()
  on = !on
}

setInterval(toggle, 1000)
