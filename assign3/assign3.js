const fs = require("fs");

//deal with training data
const trainingReviews = parseData("trainingSet.txt");
const trainingWords = buildWordsTable(trainingReviews);
const sortedTrainingWords = Object.keys(trainingWords).sort();
addWordsArray(trainingReviews, sortedTrainingWords, trainingWords);
printOutResults(sortedTrainingWords, trainingReviews, "preprocessed_train.txt");
const trainingProbs = getProbabilities(
  sortedTrainingWords,
  trainingWords,
  trainingReviews
);
const trainingPredictions = makePredictions(
  sortedTrainingWords,
  trainingProbs,
  trainingReviews
);

//deal with test data
const testReviews = parseData("testSet.txt");
const testPredictions = makePredictions(
  sortedTrainingWords,
  trainingProbs,
  testReviews
);
addWordsArrayForTest(testReviews, sortedTrainingWords);
printOutResults(sortedTrainingWords, testReviews, "preprocessed_test.txt");

const results = `Training data: trainingSet.txt, Testing data: trainingSet.txt
Accuracy: ${calculateAccuracy(trainingReviews, trainingPredictions)}

Training data: trainingSet.txt, Testing data: testSet.txt
Accuracy: ${calculateAccuracy(testReviews, testPredictions)}
`;
fs.writeFileSync("results.txt", results);

function parseData(fileName) {
  const trainingSet = fs
    .readFileSync(fileName)
    .toString()
    .toLowerCase()
    .replace(/[^\w\s]|_/g, "");

  const reviews = trainingSet.split("\n").map(line => {
    const [s, r] = line.split("\t");
    return { sentence: s, rating: Number(r) };
  });
  if (!reviews[reviews.length - 1].sentence) {
    reviews.pop();
  }

  return reviews;
}

//build words table (key=word, value=array of whether word in review)
function buildWordsTable(reviewArray) {
  const wordsTable = {};
  reviewArray.forEach((r, i) => {
    const sentenceWords = r.sentence.split(" ");
    sentenceWords.forEach(w => {
      if (!wordsTable[w]) {
        wordsTable[w] = new Array(reviewArray.length).fill(0);
      }
      wordsTable[w][i] = 1;
    });
  });

  delete wordsTable[""];

  return wordsTable;
}

/** add array of if words are in review to the review*/
function addWordsArray(reviews, sortedWords, wordsTable) {
  reviews.forEach((r, i) => {
    r.words = sortedWords.map(w => wordsTable[w][i]);
  });
}

function addWordsArrayForTest(reviews, sortedWords) {
  reviews.forEach(r => {
    const reviewWords = r.sentence.split(" ");
    r.words = sortedWords.map(w => reviewWords.includes(w) ? 1 : 0);
  });
}

/** print out preprocessed data */
function printOutResults(sortedWords, reviews, fileName) {
  const allWordsString = [...sortedWords, "classlabel"].join(",");
  const wordsInReviews = reviews
    .map(r => [...r.words, r.rating].join(","))
    .join("\n");
  fs.writeFileSync(
    fileName,
    allWordsString + "\n" + wordsInReviews
  );
}

/** loop through each word, check if each use is positive or negative, store in object*/
function getProbabilities(sortedWords, wordsTable, reviews) {
  return sortedWords.map(w => {
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

    return { numPos, numNeg, notInPos, notInNeg };
  });
}

function makePredictions(sortedTrainingWords, trainingProbs, reviews) {
  const probPosOverall =
    reviews.filter(r => r.rating === 1).length / reviews.length;

  const predictions = reviews.map(r => {
    const reviewWords = r.sentence.split(" ");
    sumPosProb = Math.log(probPosOverall);
    sumNegProb = Math.log(1 - probPosOverall);

    sortedTrainingWords.forEach((tw, idx) => {
      if (reviewWords.includes(tw)) {
        sumPosProb += Math.log(trainingProbs[idx].numPos);
        sumNegProb += Math.log(trainingProbs[idx].numNeg);
      } else {
        sumPosProb += Math.log(trainingProbs[idx].notInPos);
        sumNegProb += Math.log(trainingProbs[idx].notInNeg);
      }
    });

    return sumPosProb > sumNegProb ? 1 : 0;
  });

  return predictions;
}

function calculateAccuracy(reviews, predictions) {
  let correct = 0;
  predictions.forEach((p, i) => {
    if (reviews[i].rating === p) {
      correct += 1;
    }
  });
  return correct / reviews.length;
}