#!/usr/bin/env python3
"""Launches a weather forecast from the command line
for a given city (Wrocław if argument is not given)."""

import webbrowser
import sys

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
	webbrowser.open('https://www.google.com/search?client=ubuntu&channel=fs&q=pogoda+'
					+ address + '&ie=utf-8&oe=utf-8')
else:
	webbrowser.open('https://www.google.com/search?client=ubuntu&channel=fs&q='
                    'pogoda+wroc%C5%82aw&ie=utf-8&oe=utf-8')
