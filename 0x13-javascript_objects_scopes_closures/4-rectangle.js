#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let initial;
    const  initial = this.width;
    this.width = this.height;
    this.height = initial;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
