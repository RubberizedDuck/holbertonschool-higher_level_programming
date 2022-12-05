#!/usr/bin/node

const fiveSquare = require('./5-square');

class Square extends fiveSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    super.print(c);
  }
}
module.exports = Square;
