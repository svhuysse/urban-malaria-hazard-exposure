#!/usr/bin/env python

"""
Function that checks if a GRASS GIS add-on is installed, and installs it if needed
"""

import grass.script as gscript

def check_install_addon(addon):
	# 
	if addon not in gscript.parse_command('g.extension', flags="a"):
		gscript.run_command('g.extension', extension="%s"%addon)
		print("%s have been installed on your computer"%addon)
	else: print("%s is already installed on your computer"%addon)
