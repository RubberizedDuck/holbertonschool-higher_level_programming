#!/usr/bin/node
const fs = require('fs');
const fileInput = process.argv[3];
fs.writeFile(process.argv[2], fileInput, (err) => {
  if (err) {
    console.error(err);
  }
});
