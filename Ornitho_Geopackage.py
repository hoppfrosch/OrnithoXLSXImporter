# -*- coding: utf-8 -*-
import sys
import os
import collections
from osgeo import gdal
from osgeo import ogr
from osgeo import osr


class OrnithoGeopackage:
    """Geopackage to hold data from Ornitho"""

    def __init__(self, pathGPKG, layername):
        # print(int(gdal.VersionInfo('VERSION_NUM')))

        if int(gdal.VersionInfo('VERSION_NUM')) < 2020000:
            raise Exception('Geopackage requires GDAL >= 2.2')

        self.srs = osr.SpatialReference()
        self.srs.ImportFromEPSG(4326)

        cwd = os.getcwd()
        path, file = os.path.split(pathGPKG)
        # Now change the directory
        os.chdir(path)

        self.ds = ogr.GetDriverByName('GPKG').CreateDataSource(file)
        self.lyr = self.ds.CreateLayer(
            layername, self.srs, geom_type=ogr.wkbPoint)

        os.chdir(cwd)
        for k, v in self.coltypes().items():
            self.lyr.CreateField(ogr.FieldDefn(k, v))

    def columns(self):
        """Mapping of column descriptions to column names and datatypes"""

        # Todo: Parse descriptions, names and datatypes from XLSX sheet
        # Use VarType-Function to get the datatypes
        # https://support.office.com/en-us/article/vartype-function-1e08636c-1892-40c2-aff3-2b894389e82d?ocmsassetID=HA001228932&CorrelationId=0ab63060-52ed-4ca0-abc3-12202ff5d02f&ui=en-US&rs=en-US&ad=US

        cols = []
        cols.append(('ID_SIGHTING',             'A', 'integer'))
        cols.append(('ID_SPECIES',              'B', 'integer'))
        cols.append(('NAME_SPECIES',            'C', 'string'))
        cols.append(('OBSERVER_ID',             'D', 'integer'))
        cols.append(('LATIN_SPECIES',           'E', 'string'))
        cols.append(('TRA_NAME',                'F', 'string'))
        cols.append(('FAMILY_NAME',             'G', 'string'))
        cols.append(('SYS_ORDER',               'H', 'integer'))
        cols.append(('DATE',                    'I', 'date'))
        cols.append(('DATE_DAY',                'J', 'integer'))
        cols.append(('DATE_MONTH',              'K', 'integer'))
        cols.append(('DATE_YEAR',               'L', 'integer'))
        cols.append(('DATE_JDAY',               'M', 'integer'))
        cols.append(('DATE_PENTADE',            'N', 'integer'))
        cols.append(('DATE_DECADE',             'O', 'integer'))
        cols.append(('DATE_WEEK',               'P', 'integer'))
        cols.append(('TIME_START',              'Q', 'time'))
        cols.append(('TIME_START_HOUR',         'R', 'integer'))
        cols.append(('TIME_START_MIN',          'S', 'integer'))
        cols.append(('TIME_STOP',               'T', 'time'))
        cols.append(('TIME_STOP_HOUR',          'U', 'integer'))
        cols.append(('TIME_STOP_MIN',           'V', 'integer'))
        cols.append(('FULL_FORM',               'W', 'integer'))
        cols.append(('TIMING',                  'X', 'string'))
        cols.append(('ID_PLACE',                'Y', 'integer'))
        cols.append(('PLACE',                   'Z', 'string'))
        cols.append(('MUNICIPALITY',           'AA', 'string'))
        cols.append(('COUNTY',                 'AB', 'string'))
        cols.append(('COUNTRY',                'AC', 'string'))
        cols.append(('COORD_LAT',              'AD', 'real'))
        cols.append(('COORD_LON',              'AE', 'real'))
        cols.append(('COORD_LAT_DMS',          'AF', 'string'))
        cols.append(('COORD_LON_DMS',          'AG', 'string'))
        cols.append(('COORD_F',                'AH', 'integer'))
        cols.append(('COORD_E',                'AI', 'integer'))
        cols.append(('COORD_N',                'AJ', 'integer'))
        cols.append(('PRECISION',              'AK', 'string'))
        cols.append(('ALTITUDE',               'AL', 'integer'))
        cols.append(('ESTIMATION_CODE',        'AM', 'string'))
        cols.append(('TOTAL_COUNT',            'AN', 'integer'))
        cols.append(('DETAIL',                 'AO', 'string'))
        cols.append(('ATLAS_CODE',             'AP', 'string'))
        cols.append(('HIDDEN',                 'AQ', 'string'))
        cols.append(('ADMIN_HIDDEN',           'AR', 'string'))
        cols.append(('ID_RESTING_HABITAT',     'AS', 'string'))
        cols.append(('RESTING_HABITAT',        'AT', 'string'))
        cols.append(('ID_ACCURACY_LOCATION',   'AU', 'integer'))
        cols.append(('ACCURACY_LOCATION',      'AV', 'integer'))
        cols.append(('ID_OBSERVATION_DETAIL',  'AW', 'string'))
        cols.append(('OBSERVATION_DETAIL',     'AX', 'string'))
        cols.append(('COMMITTEE_DAK',          'AY', 'string'))
        cols.append(('COMMITTEE_LHK',          'AZ', 'string'))
        cols.append(('COMMITTEE_AKBW',         'BA', 'string'))
        cols.append(('COMMITTEE_BAK',          'BB', 'string'))
        cols.append(('COMMITTEE_AKBB',         'BC', 'string'))
        cols.append(('COMMITTEE_AKH',          'BD', 'string'))
        cols.append(('COMMITTEE_SKMV',         'BE', 'string'))
        cols.append(('COMMITTEE_AKN',          'BF', 'string'))
        cols.append(('COMMITTEE_AKNW',         'BG', 'string'))
        cols.append(('COMMITTEE_AKRP',         'BH', 'string'))
        cols.append(('COMMITTEE_AKSL',         'BI', 'string'))
        cols.append(('COMMITTEE_AKS',          'BJ', 'string'))
        cols.append(('COMMITTEE_AKST',         'BK', 'string'))
        cols.append(('COMMITTEE_AKSHH',        'BL', 'string'))
        cols.append(('COMMITTEE_AKT',          'BM', 'string'))
        cols.append(('COMMITTEE_HAK',          'BN', 'string'))
        cols.append(('COMMITTEE_AKB',          'BO', 'string'))
        cols.append(('SURNAME',                'BP', 'string'))
        cols.append(('NAME',                   'BQ', 'string'))
        cols.append(('NO_COMMERCIAL_USE',      'BR', 'string'))
        cols.append(('FORM_ID',                'BS', 'string'))
        cols.append(('TRA_SURNAME',            'BT', 'string'))
        cols.append(('COMMENT',                'BU', 'string'))
        cols.append(('PRIVATE_COMMENT',        'BV', 'string'))
        cols.append(('DAILY_TEXT_COMMENT_REM', 'BW', 'string'))
        cols.append(('INSERT_DATE',            'BX', 'datetime'))
        cols.append(('UPDATE_DATE',            'BY', 'datetime'))
        cols.append(('PROTOCOL_NAME',          'BZ', 'string'))

        return cols

    def coltypes(self):
        """Returns an ordered dict with column descriptions and colum datatypes"""
        cols = self.columns()
        coltypes = collections.OrderedDict()
        for col in cols:
            if col[2] == 'string':
                type = ogr.OFTString
            elif col[2] == 'integer':
                type = ogr.OFTInteger
            elif col[2] == 'datetime':
                type = ogr.OFTDateTime
            elif col[2] == 'real':
                type = ogr.OFTReal
            elif col[2] == 'time':
                type = ogr.OFTTime

            coltypes[col[0]] = type

        return coltypes

    def colnames(self):
        """Returns an ordered dict with column descriptions and colum names"""
        cols = self.columns()
        colnames = collections.OrderedDict()
        for col in cols:
            coltypes[col[0]] = col[1]

        return colnames


# test = OrnithoGeopackage(
#    "w:\Develop\OrnithoXLSXmporter\Data\jok_test_new.gpkg", "ornitho")
