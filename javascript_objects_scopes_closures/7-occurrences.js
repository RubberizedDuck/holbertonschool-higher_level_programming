#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const num of list) {
    if (num === searchElement) {
      count += 1;
    }
  }
  return count;
};
