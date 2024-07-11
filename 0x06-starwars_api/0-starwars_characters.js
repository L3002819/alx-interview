#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
request(
  'https://swapi-api.alx-tools.com/api/films/' + movieId + '/',
  async function (error, response, body) {
    if (error) return console.error(error);
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (err, res, content) {
          if (err) return console.error(err);
          console.log(JSON.parse(content).name);
          resolve();
        });
      });
    }
  }
);
