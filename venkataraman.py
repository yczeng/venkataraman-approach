''' Implements dynamic search algorithm from Venkataraman '''

import math

# lexicon is a dictionary of tuples where tuples are phonemes representing words and the values represent frequency
lexicon = {}

# this is probably just strings as keys and frequencies as values
phonemes = {'I': 1,'E': 1,'&': 1,'A': 1,'a': 1,'O': 1,'U': 1,'6': 1,'i': 1,'e': 1,'9': 1,'Q': 1,'u': 1,'o': 1,'7': 1,'3': 1,'R': 1,'#': 1,'%': 1,'*': 1,'(': 1,')': 1,'p': 1,'b': 1,'m': 1,'t': 1,'d': 1,'n': 1,'k': 1,'g': 1,'N': 1,'f': 1,'v': 1,'T': 1,'D': 1,'s': 1,'z': 1,'S': 1,'Z': 1,'h': 1,'c': 1,'G': 1,'l': 1,'r': 1,'L': 1,'~': 1,'M': 1,'y': 1,'w': 1,'W': 1}

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

		for j in range(i):
			if j+1 != i:
				word = utterance[j+1:i]
				cost = bestCost[j] + evalWord(word)

				if cost < bestCost[i]:
					bestCost[i] = cost
					prevBoundary[i] = j

	i = n - 1
	while i > 0:
		# insertWordBoundary(u, prevBoundary[i])
		i = prevBoundary[i]
	return bestCost[n-1]


# def evalUtterance(utterance):
# 	n = len(utterance)

# 	best_segment = n
# 	bestCost = evalWord(utterance[0:n])
# 	bestSegpoint = 0

# 	for i in range(1, n):
# 		subUtterance = utterance[0:i]
# 		word = utterance[i::]
# 		cost = evalUtterance(subUtterance) + evalWord(word)
# 		if cost < bestCost:
# 			bestCost = cost
# 			bestSegpoint = i

# 	# print("bestSegpoint is at", bestSegpoint)
# 	# insertWordBoundary(utterance, bestSegpoint)

# 	print(utterance, bestCost)
# 	return bestCost

def insertWordBoundary(utterance, bestSegpoint):
	# for inserting into word boundary


	# newWord = utterance[bestSegpoint::]
	# if newWord in lexicon:
	# 	lexicon[newWord] += 1
	# else:
	# 	lexicon[newWord] = 1

	for phoneme in newWord:
		if phoneme in phonemes:
			phonemes[phoneme] += 1
		else:
			phonemes[phonemes] = 0


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

		if len(lexicon) == 0:
			escape = 0
		else:
			escape = len(lexicon) / len(lexicon) + sum(lexicon.values())

		# this makes no sense?!
		P_0 = phonemes['#'] / sum(phonemes.values())
		prob = P_0 / (1-P_0)

		for i in range(len(word)):
			prob *= 2* ( phonemes[word[i]] / sum(phonemes.values()) )

		score += -math.log(prob)

	else:
		P_W = lexicon[word] / (len(lexicon) + sum(lexicon.values()))
		score += -math.log(P_W)
	print("Cost("+ word + ") = " + str(score) + "\n")
	return score

if __name__ == "__main__":
	with open('data/small-Bernstein-Ratner87', "r") as text:
		for count, line in enumerate(text):
			processedLine = line.replace('\n', '').replace(" ", "")
			print(processedLine)
			evalUtterance(processedLine)

			print("we are at line: " + str(count))
			with open('data/progress1.txt','a') as progress:
				progress.write("We are at line: " + str(count) + "\n")

	with open('data/result1.txt','a') as result:
		result.write(str(lexicon))
		result.write(str(phonemes))

	