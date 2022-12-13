#!/usr/bin/node
const request = require('request');
const filmNum = process.argv[2];
const film = 'https://swapi-api.hbtn.io/api/films/';
request(film + filmNum, (err, resp, body) => {
  if (!err) {
    const character = JSON.parse(body).characters;
    character.forEach(element => {
      request(element, (err, resp, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
