#!/usr/bin/node

const myNum = Number(process.argv[2]);

if (myNum) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
