import sys

lexicon = {}
corpusAddress = str(sys.argv[1])

with open( corpusAddress, "r" ) as corpus:
	for count, line in enumerate(corpus):

		listOfWords = line.replace('\n', '').split(' ')

		for word in listOfWords:
			if word in lexicon:
				lexicon[word] += 1
			else:
				lexicon[word] = 1

print(lexicon)

with open( corpusAddress + '-lexicon','w') as lexiconFile:
	lexiconFile.write(str(lexicon))