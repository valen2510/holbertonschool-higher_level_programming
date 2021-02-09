#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    for (const i of JSON.parse(body).results) {
      if (i.characters.includes(wedge)) {
        counter++;
      }
    }
    console.log(counter);
  }
});
