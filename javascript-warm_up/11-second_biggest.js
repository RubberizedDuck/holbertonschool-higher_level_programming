#!/usr/bin/node
const arr = process.argv.splice(2);

if (arr.length < 2) {
  console.log('0');
} else {
	// sorts and flips the array to be in descending order
  arr.sort(function (a, b) { return b - a });
  console.log(arr[1]);
}
