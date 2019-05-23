"""
Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
"""

import shutil
import os
import re

# Create a regex that matches files with the American date format.
datepattern = re.compile(r"""
	^(.*?)          # all text before the date
	([01]?\d)-      # one or two digits for the month
	([0123]?\d)-    # one or two digits for the day
	((19|20)\d\d)   # four digits for the year
	(.*?)$          # all text after the date
	""", re.VERBOSE)

# Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
	mobj = datepattern.search(amer_filename)

	# Skip files without a date.
	if mobj is None:
		continue

	# Get the different parts of the filename.
	beforepart = mobj.group(1)
	monthpart = mobj.group(2)
	daypart = mobj.group(4)
	yearpart = mobj.group(6)
	afterpart = mobj.group(8)

	# Form the European-style filename.
	euro_filename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart

	# Get the full, absolute file paths.
	abs_working_dir = os.path.abspath('.')
	amer_filename = os.path.join(abs_working_dir, amer_filename)
	euro_filename = os.path.join(abs_working_dir, euro_filename)

	# Rename the files.
	shutil.move(amer_filename, euro_filename)
