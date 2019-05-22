#!/usr/bin/env python3

"""
Multiclipboard - saves and loads pieces of text to the clipboard.
Usage:  python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
		python3 mcb.pyw <keyword> - Loads keyword to clipboard.
		python3 mcb.pyw list - Loads all keywords to clipboard.
		python3 mcb.pyw delete <keyword> - Deletes a keyword from the shelf.
		python3 mcb.pyw delete-all - Deletes all keywords.
"""

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcb_shelf[sys.argv[2]] = pyperclip.paste()
	elif sys.argv[1].lower() == 'delete':
		del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcb_shelf.keys())))
	elif sys.argv[1].lower() == 'delete-all':
		sure = input('Are you sure you want to delete ALL keywords?'
		             'Type "Yes" to proceed. ')
		if sure == 'Yes':
			mcb_shelf.clear()
	elif sys.argv[1] in mcb_shelf:
		pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
