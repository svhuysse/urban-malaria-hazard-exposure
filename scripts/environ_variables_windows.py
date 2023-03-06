#!/usr/bin/env python

"""
Functions related to configuration of environment variables
"""

import os,sys
from __main__ import config_parameters


def setup_environment_variables():
	"""	Set the environment variables allowing to use GRASS GIS python libraries 
	Documentation available on: https://grass.osgeo.org/grass64/manuals/variables.html
	Please change the directory paths according to your own system configuration.
	Hereafter are the paths used on a WINDOWS 10 computer.
    """
	# Check if environment variables exist and create them (empty) if they do not exist.
	if not 'PYTHONPATH' in os.environ:
		os.environ['PYTHONPATH']=''
	if not 'LD_LIBRARY_PATH' in os.environ:
		os.environ['LD_LIBRARY_PATH']=''
	
	# Set environment variables
	os.environ['GISBASE'] = config_parameters['GISBASE']
	
	os.environ['PYTHONPATH'] = os.path.join(os.environ['GISBASE'],'etc','python')
	
	
	os.environ['PATH'] += os.pathsep + 'C:\\OSGeo4W64\\bin'  # For .dll files
	os.environ['PATH'] += os.pathsep + 'C:\\OSGeo4W64\\lib'  
	
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'bin')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'lib')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'scripts')
	
	os.environ['PATH'] += os.pathsep + 'C:\\Users\\ADMIN_HOME\\AppData\\Roaming\\GRASS7\\addons\\bin'
	os.environ['PATH'] += os.pathsep + 'C:\\Users\\ADMIN_HOME\\AppData\\Roaming\\GRASS7\\addons\\scripts'
	os.environ['PATH'] += os.pathsep + 'C:\\Users\\ADMIN_HOME\\AppData\\Roaming\\GRASS7\\addons\\etc\\r.learn.ml2'
	
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python','grass','bin')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python','grass','lib')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python','grass','script')
	
	os.environ['PATH'] += os.pathsep + 'C:\\Users\\ADMIN_HOME\\anaconda3\\envs\\mosquimap\\Lib'
	os.environ['PATH'] += os.pathsep + 'C:\\Users\\ADMIN_HOME\\anaconda3\\envs\\mosquimap\\Lib\\site-packages'
	
	os.environ['PATH'] += os.pathsep + 'C:\\OSGeo4W64\\apps\\Python37\\lib'
	os.environ['PATH'] += os.pathsep + 'C:\\OSGeo4W64\\apps\\Python37\\lib\\site-packages'

	
	os.environ['GRASS_PYTHON'] = 'C:\\OSGeo4W64\\apps\\Python37\\python.exe'
	os.environ['PYTHONLIB'] = config_parameters['PYTHONLIB']
	os.environ['LD_LIBRARY_PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'lib')
	os.environ['GIS_LOCK'] = '$$'
	os.environ['GISRC'] = 'C:\\Users\\ADMIN_HOME\\AppData\\Roaming\\GRASS7\\rc'

	## Define GRASS-Python environment
	sys.path.append(os.path.join(os.environ['GISBASE'],'etc','python'))

	
	#os.environ['GDAL_DATA'] = config_parameters['GDAL_DATA'] # For EPSG csv files

	#Necessary?
	#os.environ['PYTHONPATH'] = 'C:\\Users\\ADMIN_HOME\\anaconda3\\Lib'
	#os.environ['PYTHONPATH'] = 'C:\\OSGeo4W64\\apps\\Python37\\lib'

	


def print_environment_variables():
	"""
	Display the current environment variables of your computer.
	"""
	## Display the currently defined environment variables
	for key in os.environ.keys():
		print("%s = %s \t" % (key,os.environ[key]))