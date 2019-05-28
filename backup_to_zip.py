"""A program that copies an entire folder and its contents
into a ZIP file whose filename increments."""

import zipfile
import os


def zip_backup(folder):
	# Backup the entire contents of "folder" into a ZIP file.

	folder = os.path.abspath(folder)    # make sure folder is absolute

	# Figure out the filename this code should use based on
	# what files already exist.
	n = 1
	while True:
		zip_filename = os.path.basename(folder) + '_' + str(n) + '.zip'
		if not os.path.exists(zip_filename):
			break
		n += 1

	# Create the ZIP file.
	print('Creating %s...' % zip_filename)
	backup_zip = zipfile.ZipFile(zip_filename, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % foldername)
		# Add the current folder to the ZIP file.
		backup_zip.write(foldername)
		# Add all the files in this folder to the ZIP file.
		for filename in filenames:
			newbase = os.path.basename(folder) + '_'
			if filename.startswith(newbase) and filename.endswith('.zip'):
				continue
			# don't backup the backup ZIP files
			backup_zip.write(os.path.join(foldername, filename))
	backup_zip.close()
	print('Done.')
