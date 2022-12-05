#!/usr/bin/node

let num = Number(process.argv[2]);

if (!num) {
	num = 1;
}
function factorial (num) {
	if (num === 0 || num === 1) {
		return 1;
	} else {
		return num * factorial(num - 1);
	}
}
console.log(factorial(num));
