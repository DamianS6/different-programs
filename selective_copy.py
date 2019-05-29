"""
A program that copies files with a certain extension from given folder
to a new one in given directory (or current by default).

'folder' - an absolute path from where the copies are made
'extension' - a string like '.xxx'
'new_folder_name' - a string, optional name of new folder for the copies
'directory' - an absolute path where the new folder for copies will
				be created
"""

import os
import shutil


def copy(folder, extension, new_folder_name=None, directory=os.getcwd()):
	# Make a folder of given name.
	if new_folder_name:
		os.mkdir(os.path.join(directory, new_folder_name))
	# Make a default 'copies' folder.
	else:
		os.mkdir(os.path.join(directory, 'copies'))

	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			if filename.endswith(extension):
				print(f'Copying files from {foldername}...')

				# Copy files to new folder of given name.
				if new_folder_name:
					shutil.copy(os.path.join(foldername, filename),
					            os.path.join(directory, new_folder_name, filename))

				# Copy files to default 'copies' folder
				else:
					shutil.copy(os.path.join(foldername, filename),
					            os.path.join(directory, 'copies', filename))
