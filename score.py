#!/usr/bin/python

import sys
import ast

# arg1 = lexicon from segmenting a corpus
# arg2 = model lexicon to score testing lexicon

segmentedLexicon = str(sys.argv[1])
modelLexicon = str(sys.argv[2])

segmentedLexiconDict = {}
modelLexiconDict = {}

with open(segmentedLexicon, "r") as lexicon:
	for line in lexicon:
		segmentedLexiconDict = ast.literal_eval(line)

with open(modelLexicon, "r") as lexicon:
	for line in lexicon:
		modelLexiconDict = ast.literal_eval(line)

# Calculate precision
# number of correct words found out of all words found
allWordsFound = len(segmentedLexiconDict)
numCorrectWords = 0
for word in segmentedLexiconDict:
	if word in modelLexiconDict:
		numCorrectWords += 1

precision = numCorrectWords / allWordsFound

# Calculate recall 
# number of correct itmes found out of all correct items
allCorrectWords = len(modelLexiconDict)
recall = numCorrectWords / allCorrectWords

# Calcilate the F1 score
f1Score = (2 * precision * recall) / (precision + recall)

print("Precision:", precision)
print("Recall:", recall)
print("f1 Score:", f1Score)