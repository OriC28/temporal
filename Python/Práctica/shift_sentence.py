
def shift_sentence(text):
	result = 0
	if text.islower():
		# *** INITIALIZING VARIABLES
		text = text.strip()
		new_text = ""
		pos = [0]
		first_letters = [text[0]]
		# *** GET FIRST LETTERS EACH WORD
		for i in range(len(text)):
			if text[i] == " ":
				pos.append(i+1)
				first_letters.append(text[i+1])
		
		if len(first_letters)>1:	
			# *** ORDER THE FIRST LETTERS IN THE NECESSARY ORDER
			letters_ordened = [first_letters[-1],first_letters[0]]
			
			for k in first_letters[1:len(first_letters)-1]:
				letters_ordened.append(k)
			
			# *** CHANGE THE FIRST LETTERS BETWEEN WORDS
			for i in range(len(text)):
				for j in range(len(letters_ordened)):
					if i == pos[j]:
						new_text+=letters_ordened[j]
				if i not in pos:
					new_text+=text[i]	
			result = new_text
		else:
			result = text

	return result

print(shift_sentence(""))

