#!/usr/bin/env python3
"""A program that looks for files larger than given size (100MB by default)."""

import os


def delete_unneeded(folder, size='100MB'):
	sizes = {
		'kb': 1024,
		'mb': 1048576,
		'gb': 1073741824,
	}
	num_size = sizes[size[-2:].lower()] * float(size[:-2])

	print('Files and folders larger than %s in %s:' % (size, folder))
	for dirpath, dirnames, filenames in os.walk(folder):
		try:
			for filename in filenames:
				if os.path.getsize(os.path.join(dirpath, filename)) > num_size:
					print(os.path.join(dirpath, filename))
		except FileNotFoundError:
			continue
