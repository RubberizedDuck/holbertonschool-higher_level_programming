#!/usr/bin/node
const arr = process.argv.splice(2)

if (arr.length < 2) {
  console.log('0');
} else {
  arr.sort(function (a, b) { return b - a }); // sorts and flips the array to be in descending order
  console.log(arr[1]);
}
