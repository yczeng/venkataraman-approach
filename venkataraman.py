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

	if n == 0:
		return 0;

	for i in range(0, n):
		# i+1 is different from Venkataraman's because you have to account for how i stops at n - 1
		bestCost[i] = evalWord(utterance[0:i+1])
		prevBoundary[i] = -1

		for j in range(i):
			if j+1 != i:
				word = utterance[j+1:i]
				evalWordResult = evalWord(word)
				cost = bestCost[j] + evalWordResult

				if cost < bestCost[i-1]:
					# print("HOWDY PARTNER")
					bestCost[i] = cost
					prevBoundary[i] = j

	print(prevBoundary)
	print(bestCost)

	i = n - 1
	while i > 0:
		insertWordBoundary(utterance, prevBoundary[i])
		i = prevBoundary[i]

	# print(newWord, bestCost[n-1])
	return bestCost[n-1]

def insertWordBoundary(utterance, bestSegpoint):
	if bestSegpoint == -1:
		newWord = utterance
	else:
		newWord = utterance[bestSegpoint::]

	if newWord in lexicon:
		lexicon[newWord] += 1
	else:
		lexicon[newWord] = 1
		phonemes[" "] += 1

	for phoneme in newWord:
		phonemes[phoneme] += 1

	print("new word is", newWord)

def evalWord(word):
	'''
	Calculates a log score for word

	Args:
		word: word w[0..k] where w[i] are the phonemes in it. Word is a string
	Returns:

	'''
	score = 0

	if len(word) == 0:
		return score

	# unigram
	if word in lexicon:
		P_W = lexicon[word] / (sum(lexicon.values()) + len(lexicon))
		score += -math.log(P_W)
		print("Cost1("+ word + ") = " + str(score))
		return score
	else:
		# back off to phonemes
		if len(lexicon) != 0:
			# print("SCORE ADDITION", -math.log(len(lexicon) / (sum(lexicon.values()) + len(lexicon))))
			score += -math.log(len(lexicon) / (sum(lexicon.values()) + len(lexicon)))

	# this parts calculate probability based on phonemes
	# print("phonemes[' '] is", phonemes[' '])
	# print("sum(phonemes.values() is", sum(phonemes.values()))

	P_0 = phonemes[' '] / sum(phonemes.values())
	prob = P_0 / (1-P_0)

	for i in range(len(word)):
		prob *= float(phonemes[word[i]]) / sum(phonemes.values())

	score += -math.log(prob)

	# I believe this calculation is correct. Not where the error is.
	print("Cost0("+ word + ") = " + str(score))
	return score

if __name__ == "__main__":
	with open('data/small-Bernstein-Ratner87', "r") as text:
		for count, line in enumerate(text):
			processedLine = line.replace('\n', '').replace(' ', '')

			evalUtterance(processedLine)

			print(phonemes)
			print("length of phonemes", len(phonemes))
			print(lexicon)
			print("length of lexicon", len(lexicon))

	with open('data/result1.txt','a') as result:
		result.write(str(lexicon))
		result.write(str(phonemes))

	