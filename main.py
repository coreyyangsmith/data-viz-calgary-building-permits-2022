#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:02:52 2023

@author: corey
"""

###############################################################################
#
#
# Building Permit Analysis
# Calgary
#
# Corey Yang-Smith
# May 16th, 2023
#
# Data Set
# https://data.calgary.ca/Business-and-Economic-Activity/Building-Permits-by-Community/kr8b-c44i
#
#
###############################################################################

####
# Purpose of this program is to analyze the new building permits in Calgary 2022
# The goal would be to pull useful analytics on a number of factors
# Some visualizations may include the distribution of work and estimated construction
#   costs for different contractors and housing types, different locations/neighbourhoods,
#   and more.
# Additionally I would like to practice using markers and points, and implementing
#   group markers.
# I would hope to have a number of exports from this list.
####

###############################################################################
#### IMPORTING PACKAGES
###############################################################################

import pandas as pd
import geopandas as gpd
import folium

###############################################################################
#### DATA IMPORT
###############################################################################

bp_file = "building_permits.csv"
bp = gpd.read_file(bp_file)

bp.drop('Location', axis=1, inplace=True)
bp.drop('LocationCount', axis=1, inplace=True)
bp.drop('LocationTypes', axis=1, inplace=True)
bp.drop('LocationAddresses', axis=1, inplace=True)
bp.drop('LocationsGeoJSON', axis=1, inplace=True)

print(bp.dtypes)

print("\nUnique Perrmit Types")
print(bp['PermitType'].unique())

print("\nUnique Perrmit Type Mapped")
print(bp['PermitTypeMapped'].unique())

print("\nPermit Class")
print(bp['PermitClass'].unique())

print("\nPermit Class Group")
print(bp['PermitClassGroup'].unique())

print("\nPermit Class Mapped")
print(bp['PermitClassMapped'].unique())

print("\nWork Class")
print(bp['WorkClass'].unique())

print("\nWork Class Group")
print(bp['WorkClassGroup'].unique())

print("\nWork Class Mapped")
print(bp['WorkClassMapped'].unique())

print("\nApplicant Name")
print(bp['ApplicantName'].unique())

print("\nContractor Name")
print(bp['ContractorName'].unique())