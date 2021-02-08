#!/usr/bin/node

const arrayData = require('./100-data').list;

const array2 = arrayData.map(element => element * arrayData.indexOf(element));
console.log(arrayData);
console.log(array2);
