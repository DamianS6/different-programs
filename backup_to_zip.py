"""
A program that copies an entire folder and its contents
into a ZIP file whose filename increments.

folder - where to look for files to copy
restrict - copy just files with certain extensions
exclude - copy files except those with certain extensions
directory - path where you want the copy to be created, optional;
			by default current program directory

'restrict' and 'exclude' are optional and have to be lists with strings like '.xxx'.
Obviously it doesn't make much sense to give these two optional arguments in the same run.
"""

import zipfile
import os


def zip_backup(folder, restrict=None, exclude=None, directory=None):

	# If path is given, changes the directory where copy will be created.
	if directory:
		os.chdir(os.path.abspath(directory))

	# Make sure folder is absolute.
	folder = os.path.abspath(folder)

	# Figure out the filename this code should use based on what files already exist.
	n = 1
	while True:
		zip_filename = os.path.basename(folder) + '_' + str(n) + '.zip'
		if not os.path.exists(zip_filename):
			break
		n += 1

	# Create the ZIP file.
	print(f'Creating {zip_filename}...')
	backup_zip = zipfile.ZipFile(zip_filename, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for foldername, subfolders, filenames in os.walk(folder):
		print(f'Adding files in {foldername}...')

		# Add the current folder to the ZIP file.
		backup_zip.write(foldername)

		for filename in filenames:
			# Don't backup the backup ZIP files.
			newbase = os.path.basename(folder) + '_'
			if filename.startswith(newbase) and filename.endswith('.zip'):
				continue

			if restrict:
				for ext in restrict:
					if filename.endswith(ext):
						backup_zip.write(os.path.join(foldername, filename))

			elif exclude:
				for ext in exclude:
					if filename.endswith(ext):
						continue
					backup_zip.write(os.path.join(foldername, filename))

			# If neither restrict nor exclude is given, copy all the files.
			else:
				backup_zip.write(os.path.join(foldername, filename))

	backup_zip.close()
	print('Done.')
