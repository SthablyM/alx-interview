#!/usr/bin/node
const fetch = require('node-fetch');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

fetch(apiUrl)
  .then((response) => response.json())
  .then((filmData) => {
    const characterUrls = filmData.characters;
    characterUrls.forEach((url) => {
      fetch(url)
        .then((response) => response.json())
        .then((characterData) => console.log(characterData.name))
        .catch((error) => console.error('Error fetching character:', error));
    });
  })
  .catch((error) => console.error('Error fetching movie:', error));
