class Review():
  def __init__(self, sentence, rating):
    self.sentence = sentence
    self.rating = rating

def main():
  file = open("trainingSet.txt", "r")
  trainingSet = file.read()
  out = s.translate(string.maketrans("",""), string.punctuation)
  trainingSetLines = trainingSet.split("\n")
  for line in trainingSetLines:
    parseLine(line)

def parseLine(line):
  lineArray = line.split("\t")
  review = Review(lineArray[0], lineArray[1])
  return review

main()
