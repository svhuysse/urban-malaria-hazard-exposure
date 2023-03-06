#!/usr/bin/env python

"""
Function to check if a directory already exists and to create it if needed
"""

import os

def check_create_dir(path):
	if os.path.exists(path):
		print("The directory '%s' already exists"%path)
	else: 
		os.makedirs(path) 
		print("The directory '%s' has been created"%path)
		
