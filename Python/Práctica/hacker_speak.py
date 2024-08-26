
# a = 4, e = 3, i = 1, o = 0, s = 5

def hacker_speak(string):
	letters = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5'}
	for i in string:
		for j in list(letters.keys()):	
			if i == j:
				string = string.replace(i, letters[j])
	return string

print(hacker_speak("programming is fun"))


