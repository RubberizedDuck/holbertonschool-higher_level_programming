#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, resp, body) => {
  if (!err) {
    let count = 0;
    const result = JSON.parse(body).results;
    for (const item in result) { // loops through each item in API
      const character = result[item].characters; // creates a variable with all characters
      for (const found in character) { // loops through each character
        if (character[found].includes('18')) { // if character matches '18' will increment count
          count++;
        }
      }
    }
    console.log(count);
  }
});
