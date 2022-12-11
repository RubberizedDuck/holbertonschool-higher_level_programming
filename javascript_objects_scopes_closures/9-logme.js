#!/usr/bin/node
// creating a global variable to increment everytime the function is called
let index = 0;
exports.logMe = function (item) {
  console.log(index + ': ' + item);
  index++;
};
