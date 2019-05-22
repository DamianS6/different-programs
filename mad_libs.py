"""
A popular word game in which without reading the story you have to substitute some words.
The program reads in a text file and lets the user replace word
ADJECTIVE, NOUN, ADVERB or VERB with their own text.
"""


def mad_libs(filename):
	with open(filename, 'r') as file:
		filedata = file.read()

	for word in filedata.split():
		if word.strip('.,!?"\'()') == 'ADJECTIVE':
			adj = input('Enter an adjective:\n')
			filedata = filedata.replace('ADJECTIVE', adj, 1)
		if word.strip('.,!?"\'()') == 'NOUN':
			noun = input('Enter a noun:\n')
			filedata = filedata.replace('NOUN', noun, 1)
		if word.strip('.,!?"\'()') == 'VERB':
			verb = input('Enter a verb:\n')
			filedata = filedata.replace('VERB', verb, 1)
	print(filedata)

	with open(filename, 'w') as file:
		file.write(filedata)