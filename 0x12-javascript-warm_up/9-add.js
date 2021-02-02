#!/usr/bin/node
function add (a, b) {
  return (Number.parseInt(a) + Number.parseInt(b));
}
console.log(add(process.argv[2], process.argv[3]));
