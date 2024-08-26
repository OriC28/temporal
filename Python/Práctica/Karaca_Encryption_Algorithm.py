
word = "alpaca"

def karaca_encrpyt(word):
	word_reversed = ""
	vowels = {'a':'0','e':'1','i':'2','o':'2','u':'3'}
	i = -1
	while(i>=len(word)*(-1)):
		word_reversed+=word[i]
		i-=1
	for i in word_reversed:
		for j in list(vowels.keys()):
			if i == j:
				word_reversed =	word_reversed.replace(i, vowels[j])
	return word_reversed + "aca"

print(karaca_encrpyt(word))
