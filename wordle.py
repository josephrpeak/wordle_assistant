file = open("/usr/share/dict/american-english")
clean_dictionary = []
dictionary = file.readlines()

for word in dictionary:
	word = word.strip()
	if(len(word) == 5):
		word = word.upper()
		clean_dictionary.append(word)

charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current = ""
unknown = []
permutation = []
possible = []

for i in range(5):
	print("Enter char " + str(i) + ":")
	letter = str(input())
	while(not letter or letter not in charlist and letter != "?" and letter != "\s"):
		print("Invalid entry. Try again: ")
		letter = str(input())
	current+=letter

current = list(current)
charlist = list(charlist)

for i in range(5):
	if current[i] == "?":
		unknown.append(i)

if(len(unknown) == 1):
	for i in range(len(charlist)):
		current[unknown[0]] = charlist[i]
		permutation.append("".join(current))
elif(len(unknown) == 2):
	for i in range(len(charlist)):
		for j in range(len(charlist)):
			current[unknown[0]] = charlist[i]
			current[unknown[1]] = charlist[j]
			permutation.append("".join(current))
elif(len(unknown) == 3):
	for i in range(len(charlist)):
		for j in range(len(charlist)):
			for k in range(len(charlist)):
				current[unknown[0]] = charlist[i]
				current[unknown[1]] = charlist[j]
				current[unknown[2]] = charlist[k]
				permutation.append("".join(current))
elif(len(unknown) == 4):
	for i in range(len(charlist)):
		for j in range(len(charlist)):
			for k in range(len(charlist)):
				for l in range(len(charlist)):
					current[unknown[0]] = charlist[i]
					current[unknown[1]] = charlist[j]
					current[unknown[2]] = charlist[k]
					current[unknown[3]] = charlist[l]
					permutation.append("".join(current))

for guess in permutation:
	if guess in clean_dictionary:
		print(guess)
		possible.append(guess)

if(len(possible) == 0):
	print("No results found in dictionary.")
else:
	while(len(possible) > 1):
		print("Eliminate letter: ")
		eliminate = str(input())

		removed = []
		for word in possible:
			for char in word:
				if(char == eliminate and word not in removed):
					removed.append(word)

		possible = [word for word in possible if word not in removed]
		for word in possible:
			print(word)

	print("Answer: " + str(possible))