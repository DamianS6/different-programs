import re


def check_password(passw):
	"""Checks if password is strong (at least 8 characters, both upper
	and lowercase letters, at least one digit) using regex."""

	lowre = re.compile(r'[a-z]+')
	upre = re.compile(r'[A-Z]+')
	digre = re.compile(r'\d+')

	if lowre.search(passw) and upre.search(passw) and digre.search(passw) \
			and len(passw) >= 8:
		print("Your password is strong enough.")
		return True
	else:
		print("Please provide another password.")
		return False


if __name__ == '__main__':
	assert check_password('dsfsdADFASDF3423423') is True
	assert check_password('argergSFFDFSS') is False
	assert check_password('aB1%_,./') is True
	assert check_password('aA1') is False