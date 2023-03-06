#!\\usr\\bin\\env python

"""
This script contains all configuration parameters and paths to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
indata = {}
outdata = {}
rules = {}

## Config parameters
## Do not edit when working on Dakar
config_parameters['location'] = 'DAKAR_32628'
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['locationepsg'] = '32628' #  EPSG code Dakar

## Config parameters
## Edit according to your config
config_parameters['GISBASE'] = 'C:\\OSGeo4W64\\apps\\grass\\grass78'  # The GRASSGIS application folder
config_parameters['PYTHONLIB'] = 'C:\\Users\\ADMIN_HOME\\anaconda3\\python.exe'  # The python executable of ANACONDA
config_parameters['GDAL_DATA'] = 'C:\\OSGeo4W64\\share\\epsg_csv' # The file containing information of EPSG codes
config_parameters['gisdb'] = 'D:\\User\\urban_malaria\\GRASSDATA' # Path to GRASSDATA folder
config_parameters['notebook_dir'] = 'D:\\User\\urban_malaria\\notebook'


## Paths to input geodata
## Edit according to your directory organisation
indata['geodata'] = "D:\User\urban_malaria\input_geodata"
indata['image'] = os.path.join(indata['geodata'],'image.tif')
indata['aoi'] = os.path.join(indata['geodata'],'aoi.shp')
indata['aoi4validation'] = os.path.join(indata['geodata'],'aoi4validation.shp')
indata['aoi4tests'] = os.path.join(indata['geodata'],'aoi4tests.shp')
indata['landcover'] = 'os.path.join(indata['geodata'],'landcover.tif')
indata['landuse'] = os.path.join(indata['geodata'],'landuse.tif')
indata['dtm_5m'] = os.path.join(indata['geodata'],'dtm.img')
indata['dtm_5m_maskfailed'] = os.path.join(indata['geodata'],'dtm_mask_failed.tif')
indata['soil_ph_30m'] = os.path.join(indata['geodata'],'soil_ph.tif')
indata['twi'] = os.path.join(indata['geodata'],'twi.tif')
indata['pop'] = os.path.join(indata['geodata'],'pop.tif')
indata['streams'] = os.path.join(indata['geodata'],'streams.shp')
indata['marine_waters'] = os.path.join(indata['geodata'],'marine_waters.shp')
indata['lc_waterbodies'] = os.path.join(indata['geodata'],'waterbodies.tif')
indata['larvae_presence'] = os.path.join(indata['geodata'],'larvae_presence_points.shp')

## Paths to input pairwise comparison matrices
## Edit according to your directory organisation
indata['matrices_larvae'] = 'D:\\User\\urban_malaria\\input_matrices_larvae'
indata['matrices_adults'] = 'D:\\User\\urban_malaria\\input_matrices_adults'
indata['matrices_larvae_intra'] = 'D:\\User\\urban_malaria\\input_matrices_larvae\\intrafactor'
indata['matrices_larvae_inter'] = 'D:\\User\\urban_malaria\\input_matrices_larvae\\interfactor'
indata['matrices_adults_intra'] = 'D:\\User\\urban_malaria\\input_matrices_adults\\intrafactor'
indata['matrices_adults_inter'] = 'D:\\User\\urban_malaria\\input_matrices_adults\\interfactor'

## Path to output geodata
## Edit according to your directory organisation
outdata['outputdir'] = 'D:\\User\\urban_malaria\\output_geodata'

## Path to VIF analysis results
## Edit according to your directory organisation
outdata['output_vif_analysis'] = 'D:\\User\\urban_malaria\\output_vif_analysis'


## Path to matrices analysis results
## Edit according to your directory organisation
outdata['output_matrices_analysis'] = 'D:\\User\\urban_malaria\\output_matrices_analysis'

## Path to validation-related files
## Edit according to your directory organisation
outdata['output_validation'] = 'D:\\User\\urban_malaria\\output_validation_data'


## Paths to rules directory and txt files
## Edit according to your directory organisation
rules['rules_dir'] = 'D:\\User\\urban_malaria\\rules'
rules['colors_lc_10cl'] = os.path.join(rules['rules_dir'],'colors_lc_10cl.txt')
rules['colors_lc_12cl'] = os.path.join(rules['rules_dir'],'colors_lc_12cl.txt')
rules['colors_lc_14cl'] = os.path.join(rules['rules_dir'],'colors_lc_14cl.txt')
rules['classes_larvae_lc'] = os.path.join(rules['rules_dir'],'classes_larvae_lc.txt')
rules['classes_larvae_lu'] = os.path.join(rules['rules_dir'],'classes_larvae_lu.txt')
rules['classes_larvae_lf'] = os.path.join(rules['rules_dir'],'classes_larvae_lf.txt')
rules['classes_adults_lc'] = os.path.join(rules['rules_dir'],'classes_adults_lc.txt')
rules['classes_adults_lu'] = os.path.join(rules['rules_dir'],'classes_adults_lu.txt')
rules['recode_lc'] = os.path.join(rules['rules_dir'],'recode_lc.txt')
rules['recode_lca'] = os.path.join(rules['rules_dir'],'recode_lcadults.txt')
rules['reclass_lc2buildings'] = os.path.join(rules['rules_dir'], 'reclass_lc2buildings.txt')
rules['reclass_lc2trees'] = os.path.join(rules['rules_dir'],'reclass_lc2trees.txt')
rules['reclass_lc2dumpsites'] = os.path.join(rules['rules_dir'],'reclass_lc2dumpsites.txt')
rules['reclass_hsi2classes'] = os.path.join(rules['rules_dir'],'reclass_hsi2classes.txt')
rules['recode_pop2classes'] = os.path.join(rules['rules_dir'],'recode_poplog2classes.txt')
rules['recode_larvalhsi2classes'] = os.path.join(rules['rules_dir'],'recode_larvaehsi2classes.txt')
rules['recode_adultshsi2classes'] = os.path.join(rules['rules_dir'],'recode_adultshsi2classes.txt')

