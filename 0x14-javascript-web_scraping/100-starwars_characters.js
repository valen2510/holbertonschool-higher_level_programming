#!/usr/bin/node

const request1 = require('request');
const request2 = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request1(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    for (const character of JSON.parse(body).characters) {
      request2(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
