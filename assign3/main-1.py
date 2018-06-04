import string
import collections
import math

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
		  for word in self.sentence.split():
				  if word in trainingDict:
						  self.words[trainingDict.keys().index(word)] = 1

		  #for key, value in trainingDict.items():
			#	  for word in self.sentence.split():
			#			  if key == word:
			#					  self.words[i] = 1
			#	  i += 1

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
		  trainingReviewList.append(review)

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

    #read in from the testSet file and strip/modify the lines as needed
  testSet = f.read()
  nopunc = testSet.translate(string.maketrans("",""), string.punctuation)
  lowercase = nopunc.lower()
  testLines = lowercase.split("\n")
  testLines.pop()

    #create the list of test review objects with sentences parsed
  testReviewList = []
  for line in testLines:
      review = parseLine(line)
      testReviewList.append(review)

  #output the dictionary to training file
  for key, value in trainingDict.items():
		  test_file.write(key + ", ")
  test_file.write("classlabel \n")

#get the feature vector for each review and output to the training file
  for r in testReviewList:
      r.find_words(trainingDict)
      r.print_wordarray(test_file)


  num_training_r = len(trainingReviewList)
  num_test_r = len(testReviewList)

  num_train_pos = 0
  num_train_neg = 0

  for r in trainingReviewList:
      if r.rating == 0:
          num_train_neg += 1
      else:
          num_train_pos += 1

  prob_r_pos = float(num_train_pos)/float(num_training_r)
  prob_r_neg = float(num_train_neg)/float(num_training_r)

  #increase these nums for dirichlet priors
  num_train_neg += 2
  num_train_pos += 2



  #time to start predictions!

  #training set predictions
  word_val = 0
  predictions = []
  for r in trainingReviewList:
      c_neg_prob = 0
      c_pos_prob = 0
      for c in range(2):
          i = 0
          if c == 0:
              c_neg_prob = math.log(prob_r_neg)
          else:
              c_pos_prob = math.log(prob_r_pos)
          for word in r.words:
              word_val = word
              match = 1
              cond_prob = 0
              for p in trainingReviewList:
                  if p.words[i] == word_val and p.rating == c:
                      match += 1
              if c == 0:
                  cond_prob = float(match)/float(num_train_neg)
                  cond_prob = math.log(cond_prob)
                  c_neg_prob += cond_prob
              else:
                  cond_prob = float(match)/float(num_train_pos)
                  cond_prob = math.log(cond_prob)
                  c_pos_prob += cond_prob
              i += 1
      if c_neg_prob > c_pos_prob:
          predictions.append(0)
      else:
          predictions.append(1)

  #print(predictions)
  i = 0
  correct = 0
  for r in trainingReviewList:
      if r.rating == predictions[i]:
          correct += 1
      i += 1

  accuracy = float(correct)/float(num_training_r)
  print(accuracy)


  #testing set predictions
  word_val = 0
  predictions = []
  for r in testReviewList:
      c_neg_prob = 0
      c_pos_prob = 0
      for c in range(2):
          i = 0
          if c == 0:
              c_neg_prob = math.log(prob_r_neg)
          else:
              c_pos_prob = math.log(prob_r_pos)
          for word in r.words:
              word_val = word
              match = 1
              cond_prob = 0
              for p in trainingReviewList:
                  if p.words[i] == word_val and p.rating == c:
                      match += 1
              if c == 0:
                  cond_prob = float(match)/float(num_train_neg)
                  cond_prob = math.log(cond_prob)
                  c_neg_prob += cond_prob
              else:
                  cond_prob = float(match)/float(num_train_pos)
                  cond_prob = math.log(cond_prob)
                  c_pos_prob += cond_prob
              i += 1
	  if c_neg_prob > c_pos_prob:
			  predictions.append(0)
	  else:
			  predictions.append(1)

#print(predictions)
  i = 0
  correct = 0
  for r in testReviewList:
      if r.rating == predictions[i]:
          correct += 1
      i += 1

  accuracy = float(correct)/float(num_test_r)
  print(accuracy)



#parses the line into the sentence and classifier and puts it in a review object
def parseLine(line):
  lineArray = line.split("\t")
  review = Review(lineArray[0], int(lineArray[1]));
  return review

main()
