#!/usr/bin/node
const myNum = Number(process.argv[2]);

if (myNum) {
  let x = 0;
  while (x < myNum) {
    if (myNum < 0) {
      break;
    } else {
      console.log('X'.repeat(myNum));
      x++;
    }
  }
} else {
  console.log('Missing size');
}
