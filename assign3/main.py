import string
import collections

class Review():
  def __init__(self, sentence, rating):
    self.sentence = sentence
    self.rating = rating
    self.words = []
	
  def find_words(trainingDict):
		  for x in trainingDict.len():
				  words[x] = 0


def main():
  file = open("trainingSet.txt", "r")
  trainingSet = file.read()
  nopunc = trainingSet.translate(string.maketrans("",""), string.punctuation)
  lowercase = nopunc.lower() 
  trainingLines = lowercase.split("\n")
  trainingLines.pop() 

  trainingReviewList = []
  for line in trainingLines:
		  review = parseLine(line)
		  trainingReviewList.append(review);

  trainingDict = {} 
  for r in trainingReviewList:
		  for word in r.sentence.split():
				  trainingDict[word] = "true"

  trainingDict = collections.OrderedDict(sorted(trainingDict.items()))

  for key, value in trainingDict.items():
		  print key + ", ", 


def parseLine(line):
  lineArray = line.split("\t")
  review = Review(lineArray[0], lineArray[1]);
  return review

main()
