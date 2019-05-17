import re


def regstrip(string, char_to_remove=None):
	"""Does the same thing as the strip() method using regex:
	- without 2nd argument it removes all the whitespace characters
	- 2nd argument provides possibility to remove custom characters
		and it must be given as a string"""

	if char_to_remove:
		pattern = str('[' + char_to_remove + ']')
		repl = re.compile(pattern)
	else:
		repl = re.compile(r'^\s+|\s+$')
	done = repl.sub('', string)
	return done


if __name__ == '__main__':
	assert regstrip('\n\nabrakadab12312ra    ', 'aa \n3') == 'brkdb1212r'
	assert regstrip('dsfsfsd sdfsd sdffsd') == 'dsfsfsd sdfsd sdffsd'
	assert regstrip('. .', '.') == ' '
