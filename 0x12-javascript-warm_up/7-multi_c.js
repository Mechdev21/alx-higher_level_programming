#!/usr/bin/node
const arg = process.argv[2];
const real = parseInt(arg);

if (isNaN(real)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < real; i++) {
    console.log('C is fun');
  }
}
