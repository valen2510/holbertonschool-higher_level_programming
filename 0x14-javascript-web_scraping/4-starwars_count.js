#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (error, response, body) {
  let counter = 0;
  if (!error) {
    const data = JSON.parse(body).results;
    for (const i in data) {
      if (data[i].characters.includes(wedge)) {
        counter++;
      }
    }
  }
  console.log(counter);
});
