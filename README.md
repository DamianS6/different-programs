# Simple programs

A bunch of different programs, usually automating some simple tasks. Ideas come mostly from the book Automate the Boring Stuff with Python (hereinafter referred to as "the book") by Al Sweigart, however except for few (which is marked in description and has been for learning purpose) I've written them myself, not copied from the book.

### List of programs:
<ul>
  <li> <b> quiz_gen </b> - Generates a number of randomized geography quiz about European capitals. Made with the book, changed from USA Capitals quiz to European by me.
  <li> <b> backup_to_zip </b> - Copies an entire folder (or files with/without given extensions) into a ZIP file in current directory or given one. Started with the book, added my own functionalities.
  <li> <b> filename_remove0s </b> - Removes zeros from filenames in given directory. Doesn't remove single zeros, zeros that initialize filename or that resemble to be a part of a number (eg. 2400, 56002).
  <li> <b> find_url </b> - Find website URLs in the copied text. Requires pyperclip module.
  <li> <b> mad_libs </b> - A popular word game in which without reading the story you have to substitute some words. The program reads in a text file and lets the user replace word ADJECTIVE, NOUN, ADVERB or VERB with their own text.
  <li> <b> mcb.pyw </b> - Multiclipboard, saves and loads pieces of text to the clipboard using given keywords. Usage instructions are provided inside the file. Made with the book, improved by myself with delete functions. Requires pyperclip module.
  <li> <b> pesel_validation </b> - Checks the validity of given Polish national identification number (PESEL).
  <li> <b> phoneandemail </b> - Finds phone numbers and email addresses on the clipboard. Returns found numbers and emails to the clipboard. Requires pyperclip module. Made with the book.
  <li> <b> regex_search </b> - Opens all .txt files in a given folder and searches for any line that matches a user-supplied regular expression.
  <li> <b> regex_strip </b> - Using regex does the same thing as the built-in strip() method. Usage instructions are in the file.
  <li> <b> remove_typos </b> - Remove common typos: repeated words, multiple spaces and punctuation signs. Takes a text from the clipboard and returns the corrected one. Requires pyperclip module.
  <li> <b> rename_dates </b> - Renames filenames in given directory
with American MM-DD-YYYY date format to European DD-MM-YYYY. Made with the book.
  <li> <b> selective_copy.py </b> - Walks through a folder tree and copy files with certain file extension to a new folder of given or default name.
  <li> <b> strong_pass_check </b> - Using regex checks if password is strong - has at least 8 characters containing both upper and lowercase letters and at least one digit.
</ul>
