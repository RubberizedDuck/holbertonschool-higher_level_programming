#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let value = '';
      for (let j = 0; j < this.width; j++) {
        value += 'X';
      }
      console.log(value);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }
}
module.exports = Rectangle;
