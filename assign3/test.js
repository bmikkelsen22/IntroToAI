const fs = require("fs");

const trainingSet = fs
  .readFileSync("trainingSet.txt")
  .toString()
  .toLowerCase()
  .replace(/[^\w\s]|_/g, "");

const reviews = trainingSet.split("\n").map(line => {
  const [s, r] = line.split("\t");
  return { sentence: s, rating: Number(r) };
});

const wordsTable = {};
reviews.forEach((r, i) => {
  const sentenceWords = r.sentence.split(" ");
  sentenceWords.forEach(w => {
    if (!wordsTable[w]) {
      wordsTable[w] = new Array(reviews.length).fill(false);
    }
    wordsTable[w][i] = true;
  });
});

console.log();