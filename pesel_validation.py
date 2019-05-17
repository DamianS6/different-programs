import sys


def validate(pesel):
	"""Checks if number PESEL is valid based on given number (11-digits)."""
	try:
		if len(str(pesel)) != 11:
			raise ValueError
		p = [int(n) for n in list(str(pesel))]
		sum = 9*(p[0]+p[4]+p[8]) + 7*(p[1]+p[5]+p[9]) + 3*(p[2]+p[6]) + p[3] + p[7]
		if str(sum)[-1] == str(p[-1]):
			print("This number PESEL is valid.")
			return 1
		print("This number PESEL is invalid.")
		return 0
	except ValueError:
		sys.stderr.write('ERROR: Number PESEL must have 11 digits.\n')


validate(94073091467)