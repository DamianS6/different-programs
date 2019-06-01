#!/usr/bin/env python3

import re
import pyperclip


def findurl():
	"""Find website URLs in the copied text."""
	urlregex = re.compile(r'http[s]?://[^\s,]*')
	if urlregex.findall(str(pyperclip.paste())):
		print("Links found in the copied text:")
		for link in urlregex.findall(str(pyperclip.paste())):
			print(link)
	else:
		print("There are no links in the copied content.")


if __name__ == '__main__':
	findurl()
