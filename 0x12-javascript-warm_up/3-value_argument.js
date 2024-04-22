#!/usr/bin/node
const para = process.argv[2];
if (para === undefined) {
  console.log('No argument');
} else {
  console.log(para);
}
