#!/usr/bin/node

const arrayData = require('./100-data').list;

const arrayDataIndex = arrayData.map(function (currentValue, index) { return currentValue * index; });
console.log(arrayData);
console.log(arrayDataIndex);
