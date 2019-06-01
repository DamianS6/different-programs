#!/usr/bin/env python3
"""A program to remove zeros from filenames in given directory."""

import shutil
import os
import re

zeropattern = re.compile(r'^(.*?)([^\d]*?)(0{2,})(\d+)(.*?)$')
checkpattern = re.compile(r'[^\d]0{2,}\d+')


def remove0s(path):

	for filename in os.listdir(path):
		while checkpattern.search(filename):
			mobj = zeropattern.search(filename)

			if mobj is None:
				continue

			beforepart = mobj.group(1)
			nonumpart = mobj.group(2)
			numpart = mobj.group(4)
			afterpart = mobj.group(5)

			newname = beforepart + nonumpart + numpart + afterpart

			abs_working_dir = os.path.abspath(path)
			oldname = os.path.join(abs_working_dir, filename)
			newname = os.path.join(abs_working_dir, newname)
			filename = newname

			shutil.move(oldname, newname)
