#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (typeof (num) !== 'number') {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
