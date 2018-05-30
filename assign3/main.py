class Review():
  def __init__(self, sentence, rating):
    self.sentence = sentence
    self.rating = rating

def main():
  file = open("trainingSet.txt", "r")
  trainingSet = file.read()
  trainingSetLines = trainingSet.split("\n")



def parseLine(line):
  lineArray = line.split("\t")
  review = Review(lineArray[0], lineArray[1]);
  

main()