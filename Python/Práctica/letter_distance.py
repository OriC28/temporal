
def letter_distance(word1, word2):
	distance = 0
	length_min = min(len(word1), len(word2))
	for i in range(length_min):
		distance += abs(ord(word1[i]) - ord(word2[i]))
	distance+=len(word1) - len(word2)
	return distance

print(letter_distance("abcde", "abcdef"))



