#!/usr/bin/node

const process = require('process');
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8',  (err) => {
  if (err) {
    console.error('error:', err);
  }
})
