#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const dic = {};
    let numTasks = 1;
    const data = JSON.parse(body);
    let userId = data[0].userId;
    for (const task of data) {
      if (task.userId !== userId) {
        numTasks = 1;
        userId = task.userId;
      }
      if (task.completed) {
        dic[userId] = numTasks++;
      }
    }
    console.log(dic);
  }
});
