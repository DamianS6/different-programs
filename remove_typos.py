import re
import pyperclip


def remove_typos():
	"""Remove common typos: repeated words,
	multiple spaces and punctuation signs.
	Takes a text from the clipboard and returns the corrected one."""
	multregex = re.compile(r'([,.:;!?]|\s)\1+')
	repeatregex = re.compile(r'(\b\S+\b)\s+\b\1\b')
	new = repeatregex.sub(r'\1', pyperclip.paste())
	new = multregex.sub(r'\1', new)
	return pyperclip.copy(new)
