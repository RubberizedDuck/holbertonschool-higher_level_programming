#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filename = process.argv[3];
const url = process.argv[2];
let infoToWrite = '';
request(url, (error, resp, body) => {
  if (!error) {
    infoToWrite = body;
    fs.writeFile(filename, infoToWrite, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
