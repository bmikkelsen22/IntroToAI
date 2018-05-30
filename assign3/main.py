import string

class Review():
  def __init__(self, sentence, rating):
    self.sentence = sentence
    self.rating = rating

def main():
  file = open("trainingSet.txt", "r")
  trainingSet = file.read().strip().lower()
  trainingSet = trainingSet.translate(str.maketrans("","", string.punctuation))
  trainingSetLines = trainingSet.split("\n")
  reviews = []
  words = {}
  for line in trainingSetLines:
    review = parseLine(line)
    reviews.append(review)
    reviewWords = review.sentence.split(" ")
    #print(reviewWords)
    for word in reviewWords:
      if word not in words: 
        words[word] = True
  sortedWords = list(words)
  print(sortedWords)

def parseLine(line):
  sentence, rating = line.split("\t")
  review = Review(sentence, int(rating))
  return review

main()
