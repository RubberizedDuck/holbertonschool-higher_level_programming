#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (c = 'X') {
    let value = '';
    for (let i = 0; i < this.width; i++) {
      value += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(value);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}
module.exports = Rectangle;
