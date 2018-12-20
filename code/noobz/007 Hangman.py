import random



def intro():
	wordbank = ["chicken", "bear", "cat", "human", "money", "water"]
	word = str(random.choice(wordbank))
	print("The word has {} letters".format(len(word)))
	wlength = int(len(word))
	print("You have {} guesses".format(wlength))
	word_letter = list(word)

	return word, wlength, word_letter


def guesses():
	global word_letter
	guesses = 0
	triedletters = []
	while guesses < wlength:
		letter = input("Input your guess: ")
		comp = list(letter)
		triedletters.append(letter)
		print("\nTried Letters: ")
		print(triedletters)
		print("\n Correct Letters: ")
		print(set(word_letter).intersection(triedletters))
		if bool(set(word_letter).intersection(comp)) == True:
			print("Correct")
		if bool(set(word_letter).intersection(comp)) == False:
			print("Wrong")
			guesses +=1

		print("\n")
		print("That was your {} guess".format(guesses))
		if set(triedletters) == set(word_letter):
			print("You win")

	return triedletters


def render_word(word, triedletters):
	unguessed = [x for x in word if x not in triedletters]
	for missing in unguessed:
		word = word.replace(missing, '_')
	return ' '.join(word)




word, wlength, word_letter = intro()
triedletters = guesses()

print(render_word(word, triedletters))



