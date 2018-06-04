import string
import collections

class Review():
  def __init__(self, sentence, rating):
    self.sentence = sentence
    self.rating = rating
    self.words = []
	
	#creates the feature vector for the review
  def find_words(self, trainingDict):
		  for x in trainingDict.items():
				  self.words.append(0) 

		  i = 0
		  for key, value in trainingDict.items():
				  for word in self.sentence.split():
						  if key == word:
								  self.words[i] = 1
				  i += 1

  #outputs the feature vector to a file
  def print_wordarray(self, f):
		  for x in self.words:
				  f.write(str(x) + ", ")
		  f.write(str(self.rating) + "\n") 


def main():
	#open the files we will need to use
  file = open("trainingSet.txt", "r")
  f = open("testSet.txt", "r") 
  train_file = open("preprocessed_train.txt", "w")
  test_file = open("preprocessed_test.txt", "w")

  #read in from the training file and strip/modify the lines as needed
  trainingSet = file.read()
  nopunc = trainingSet.translate(string.maketrans("",""), string.punctuation)
  lowercase = nopunc.lower() 
  trainingLines = lowercase.split("\n")
  trainingLines.pop() 

  #create the list of review objects with sentences parsed
  trainingReviewList = []
  for line in trainingLines:
		  review = parseLine(line)
		  trainingReviewList.append(review);

  #create the training dictionary of words
  trainingDict = {} 
  for r in trainingReviewList:
		  for word in r.sentence.split():
				  trainingDict[word] = "true"

  #order the dictionary in alphabetical order
  trainingDict = collections.OrderedDict(sorted(trainingDict.items()))

  #output the dictionary to training file
  for key, value in trainingDict.items():
		  train_file.write(key + ", ")
  train_file.write("classlabel \n")

  #get the feature vector for each review and output to the training file
  for r in trainingReviewList:
		  r.find_words(trainingDict) 
		  r.print_wordarray(train_file) 


#parses the line into the sentence and classifier and puts it in a review object
def parseLine(line):
  lineArray = line.split("\t")
  review = Review(lineArray[0], int(lineArray[1]));
  return review

main()
