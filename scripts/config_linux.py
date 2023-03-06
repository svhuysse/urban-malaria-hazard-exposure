#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}


## Please update the following paths according to your own configuration
config_parameters['GISBASE'] = '/usr/lib/grass78'
config_parameters['PYTHONLIB'] = '/usr/bin/python2'
#config_parameters['GDAL_DATA'] = 'C:/OSGeo4W64/share/epsg_csv' #For EPSG csv files
config_parameters['locationepsg'] = '32737' #  EPSG code Nairobi

## The following parameters should not be changed  
config_parameters['gisdb'] = os.path.join(os.environ['HOME'], 'GRASSDATA') # path to the GRASSDATA folder
#config_parameters['gisdb'] = '/home/user/Téléchargements/GRASSDATA' # path to GRASSDATA folder
config_parameters['location'] = 'nc_spm_08_grass7'
#config_parameters['location'] = 'DAKAR_32628'
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['locationepsg'] = '32628' #  EPSG code Dakar
config_parameters['outputfolder'] = '..\\..\\results'
config_parameters['inputdir'] = '..\\..\\input_data'
