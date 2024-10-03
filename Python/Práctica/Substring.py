import random

def factorial(n):
	return 1 if (n == 1 or n == 0) else factorial(n-1)*n

def permutation(words):
	permu_words = []
	same_size = True
	size_item = len(words[0])

	for i in words:
		if len(i) == size_item:
			size_item = len(i)
		else:
			same_size = False
			break
	
	if same_size:
		l = 0
		word = ""
		r = factorial(len(words))
		while(l<r):
			for i in range(len(words)):
				w = random.choice(words)
				if w not in word:
					word+=w
				else:
					w = random.choice(words)

			if word not in permu_words and len(word)==len(words)*size_item:
				permu_words.append(word)
				l+=1
			word = ""
	return permu_words

def find_substring(string, words):
	permu_words = permutation(words)
	positions = []
	for word in permu_words:
		if string.find(word)!=-1:
			positions.append(string.find(word))
	return positions

print(find_substring("barfoothefoobarman", ["bar", "foo"]))
