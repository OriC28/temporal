def stutter(word):
	new_word = ""
	for i in range(2):
		new_word+=word[:2] + "..."
	new_word = "{} {}?".format(new_word, word)
	return new_word

print(stutter("excelente"))