/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ([
/* 0 */,
/* 1 */
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

const { PIO, ASM, StateMachine } = __webpack_require__(2);

class NeoPixel {
  constructor(pin, len, options = {}) {
    this.pin = pin;
    this.length = len;
    this.smId = options.sm ?? StateMachine.getAvailableId();
    this.hz = options.hz || 800000;
    this.buf = new Uint32Array(this.length);
    this.buf.fill(0);

    const asm = new ASM({ sideset: 1 });
    asm
      .label("bitloop")
      .out("x", 1)
      .side(0)
      .delay(2)
      .jmp("!x", "do_zero")
      .side(1)
      .delay(1)
      .label("do_one")
      .jmp("bitloop")
      .side(1)
      .delay(4)
      .label("do_zero")
      .nop()
      .side(0)
      .delay(4);

    this.sm = new StateMachine(this.smId, asm, {
      freq: this.hz * 10,
      autopull: true,
      pullThreshold: 24,
      fifoJoin: PIO.FIFO_JOIN_TX,
      sidesetBase: this.pin,
      outShiftDir: PIO.SHIFT_LEFT,
    });
    this.sm.active(true);
  }

  color(r, g, b) {
    return (g << 24) | (r << 16) | (b << 8);
  }

  setPixel(index, color) {
    this.buf[index] = color;
  }

  getPixel(index) {
    return this.buf[index];
  }

  clear() {
    this.buf.fill(0);
  }

  show() {
    this.sm.put(this.buf);
  }
}

exports.NeoPixel = NeoPixel;


/***/ }),
/* 2 */
/***/ ((module) => {

"use strict";
module.exports = require("rp2");

/***/ })
/******/ 	]);
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
const { NeoPixel } = __webpack_require__(1)
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

})();

/******/ })()
;