# -*- coding: utf-8 -*-
import sys
import os
from osgeo import gdal
from osgeo import ogr
from osgeo import osr

class OrnithoGeopackage:
  """Geopackage to hold data from Ornitho"""

  def __init__(self, pathGPKG, layername):
    print(int(gdal.VersionInfo('VERSION_NUM')))
    if int(gdal.VersionInfo('VERSION_NUM')) < 2020000:
      raise Exception('Geopackage requires GDAL >= 2.2')

    self.srs = osr.SpatialReference()
    self.srs.ImportFromEPSG(4326)

    cwd = os.getcwd()
    path, file = os.path.split(pathGPKG)
    # Now change the directory
    os.chdir( path )

    self.ds = ogr.GetDriverByName('GPKG').CreateDataSource(file)
    self.lyr = self.ds.CreateLayer(layername, self.srs, geom_type = ogr.wkbPoint)

    # Table definition
    self.lyr.CreateField(ogr.FieldDefn('ID_SIGHTING', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('ID_SPECIES', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('NAME_SPECIES', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('OBSERVER_ID', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('LATIN_SPECIES', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('TRA_NAME', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('FAMILY_NAME', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('SYS_ORDER', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE', ogr.OFTDate))
    self.lyr.CreateField(ogr.FieldDefn('DATE_DAY', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_MONTH', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_YEAR', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_JDAY', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_PENTADE', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_DECADE', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DATE_WEEK', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('TIME_START', ogr.OFTTime))
    self.lyr.CreateField(ogr.FieldDefn('TIME_START_HOUR', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('TIME_START_MIN', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('TIME_STOP', ogr.OFTTime))
    self.lyr.CreateField(ogr.FieldDefn('TIME_STOP_HOUR', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('TIME_STOP_MIN', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('FULL_FORM', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('TIMING', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ID_PLACE', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('PLACE', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('MUNICIPALITY', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COUNTY', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COUNTRY', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COORD_LAT', ogr.OFTReal))
    self.lyr.CreateField(ogr.FieldDefn('COORD_LON', ogr.OFTReal))
    self.lyr.CreateField(ogr.FieldDefn('COORD_LAT_DMS', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COORD_LON_DMS', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COORD_F', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('COORD_E', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('COORD_N', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('PRECISION', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ALTITUDE', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('ESTIMATION_CODE', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('TOTAL_COUNT', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('DETAIL', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ATLAS_CODE', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('HIDDEN', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ADMIN_HIDDEN', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ID_RESTING_HABITAT', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('RESTING_HABITAT', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('ID_ACCURACY_LOCATION', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('ACCURACY_LOCATION', ogr.OFTInteger))
    self.lyr.CreateField(ogr.FieldDefn('ID_OBSERVATION_DETAIL', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('OBSERVATION_DETAIL', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_DAK', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_LHK', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKBW', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_BAK', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKBB', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKH', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_SKMV', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKN', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKNW', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKRP', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKSL', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKS', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKST', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKSHH', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKT', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_HAK', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMITTEE_AKB', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('SURNAME', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('NAME', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('NO_COMMERCIAL_USE', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('FORM_ID', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('TRA_SURNAME', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('COMMENT', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('PRIVATE_COMMENT', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('DAILY_TEXT_COMMENT_REM', ogr.OFTString))
    self.lyr.CreateField(ogr.FieldDefn('INSERT_DATE', ogr.OFTDateTime))
    self.lyr.CreateField(ogr.FieldDefn('UPDATE_DATE', ogr.OFTDateTime))
    self.lyr.CreateField(ogr.FieldDefn('PROTOCOL_NAME', ogr.OFTString))

    os.chdir(cwd)


test = OrnithoGeopackage("w:\Develop\OrnithoXLSXmporter\Data\jok_test_new.gpkg","ornitho");
