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

//build words table (key=word, value = array of )
const wordsTable = {};
reviews.forEach((r, i) => {
  const sentenceWords = r.sentence.split(" ");
  sentenceWords.forEach(w => {
    if (!wordsTable[w]) {
      wordsTable[w] = new Array(reviews.length).fill(0);
    }
    wordsTable[w][i] = 1;
  });
});

delete wordsTable[""];

const allWords = Object.keys(wordsTable).sort();

reviews.forEach((r, i) => {
  r.words = allWords.map(w => 
    wordsTable[w][i]
  );
  //TODO: change this!
  r.words.push(String(r.rating));
});

//print out preprocessed training data
const allWordsString = [...allWords, "classlabel"].join(",");
const wordsInReviews = reviews.map(r => r.words.join(",")).join("\n");
fs.writeFileSync("preprocessed_train.txt", allWordsString + "\n" + wordsInReviews);

//loop through each word, check if each use is positive or negative, store in object
const probabilities = allWords.map(w => {
  let numPos = 0;
  let numNeg = 0;
  let notInPos = 0;
  let notInNeg = 0;
  wordsTable[w].forEach((inReview, idx) => {
    if (inReview && reviews[idx].rating === 1) {
      numPos++;
    } else if (inReview && reviews[idx].rating === 0) {
      numNeg++;
    } else if (!inReview && reviews[idx].rating === 1) {
      notInPos++;
    } else if (!inReview && reviews[idx].rating === 0) {
      notInNeg++;
    }
  });

  return { numPos, numNeg, notInPos, notInNeg }
})

console.log(JSON.stringify(reviews[2].words));
