#!/usr/bin/node
const number = Number.parseInt(process.argv[2]);
if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
