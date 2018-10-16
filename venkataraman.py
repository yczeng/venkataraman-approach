''' Implements dynamic search algorithm from Venkataraman '''

import math

# lexicon is a dictionary or words and their respective frequencies
lexicon = {}

# phonemes is a dictionary of phonemes and their respective frequencies.
phonemes = {" ": 1, "#": 1, "%": 1, "&": 1, "(": 1, ")": 1, "*": 1, "3": 1, "6": 1, "7": 1, "9": 1, "A": 1, "D": 1, "E": 1, "G": 1, "I": 1, "L": 1, "M": 1, "N": 1, "O": 1, "Q": 1, "R": 1, "S": 1, "T": 1, "U": 1, "W": 1, "Z": 1, "a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1, "k": 1, "l": 1, "m": 1, "n": 1, "o": 1, "p": 1, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1, "w": 1, "y": 1, "z": 1, "~": 1}

def evalUtterance(utterance):
	n = len(utterance)
	bestCost = [0] * n
	prevBoundary = [0] * n

	#finally... now we have a base case
	if n == 0:
		return 0;

	for i in range(1, n):
		bestCost[i] = evalWord(utterance[0:i])
		prevBoundary[i] = -1

		for j in range(0, i):
			if j+1 != i:
				word = utterance[j+1:i]
				cost = bestCost[j] + evalWord(word)

				if cost < bestCost[i]:
					bestCost[i] = cost
					prevBoundary[i] = j

	print(prevBoundary)
	i = n - 1
	# not sure what the point of this is. It seems to just set i to 0?
	
	while i > 0:
		newWord = insertWordBoundary(utterance, prevBoundary[i])
		i = prevBoundary[i]

	# print(newWord, bestCost[n-1])
	return bestCost[n-1], newWord

def insertWordBoundary(utterance, bestSegpoint):
	if bestSegpoint == -1:
		newWord = utterance
	else:
		newWord = utterance[bestSegpoint::]

	if newWord in lexicon:
		lexicon[newWord] += 1
	else:
		lexicon[newWord] = 1

	for phoneme in newWord:
		phonemes[phoneme] += 1

	print("new word is", newWord)
	return newWord

def evalWord(word):
	'''
	Calculates a log score for word

	Args:
		word: word w[0..k] where w[i] are the phonemes in it. Word is a string
	Returns:

	'''
	score = 0

	# this parts calculate probability based on phonemes
	if word not in lexicon:
		# this makes no sense?!
		P_0 = phonemes['#'] / sum(phonemes.values())
		prob = P_0 / (1-P_0)

		for i in range(len(word)):
			prob *=  phonemes[word[i]] / sum(phonemes.values())

		score += -math.log(prob)

	else:
		P_W = lexicon[word] / (len(lexicon) + sum(lexicon.values()))
		score += -math.log(P_W)
	print("Cost("+ word + ") = " + str(score))
	return score

if __name__ == "__main__":
	with open('data/small-Bernstein-Ratner87', "r") as text:
		for count, line in enumerate(text):
			processedLine = line.replace('\n', '').replace(" ", "")

			newWord = evalUtterance(processedLine)[1]
			print(phonemes)
			print("length of phonemes", len(phonemes))
			print(lexicon)
			print("length of lexicon", len(lexicon))

			# with open('dump/results1.txt','a') as progress:
			# 	progress.write(newWord + "\n")

	with open('data/result1.txt','a') as result:
		result.write(str(lexicon))
		result.write(str(phonemes))

	