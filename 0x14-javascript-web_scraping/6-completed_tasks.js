#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const dic = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed) {
        if (dic[task.userId]) {
          dic[task.userId]++;
        } else {
          dic[task.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
