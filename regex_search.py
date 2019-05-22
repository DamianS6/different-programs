"""
A program that opens all .txt files in a given folder and searches
for any line that matches a user-supplied regular expression.
"""

import os
import re


def regex_search(path):

	pattern = input(r'Enter a regular expression you want to look for: ')
	regex = re.compile(pattern)
	count = 0
	os.chdir(path)

	for filename in os.listdir('.'):
		if filename.endswith('.txt'):
			with open(filename) as file:
				if regex.search(file.read()):
					print('\n\n' + filename)
				file.seek(0)
				lines = file.readlines()
				for line in lines:
					if regex.search(line):
						print(line, end='')
						count += 1

	if count == 0:
		print("\nI'm sorry but I can't find this regular expression "
		      "in files in given directory.")
