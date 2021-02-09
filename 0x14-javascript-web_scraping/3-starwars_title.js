#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
