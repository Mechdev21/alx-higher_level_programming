#!/usr/bin/node

const request = require('request');
const process = require('process');

const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(baseUrl + id, (err, response, body) => {
  if (err) {
    throw (err);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
