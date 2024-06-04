#!/usr/bin/node

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, body) => {
	if (err) {
		console.error('error:', err);
	}
	console.log(body);
});
