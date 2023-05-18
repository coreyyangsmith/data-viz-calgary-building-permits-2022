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
#### DATA IMPORT & MANAGEMENT
###############################################################################

#Importing bp and creating bp_trimmed
bp_file = "building_permits.csv"
bp = gpd.read_file(bp_file)

bp.drop('Location', axis=1, inplace=True)
bp.drop('LocationCount', axis=1, inplace=True)
bp.drop('LocationTypes', axis=1, inplace=True)
bp.drop('LocationAddresses', axis=1, inplace=True)
bp.drop('LocationsGeoJSON', axis=1, inplace=True)

bp_dtypes = pd.DataFrame()


#Creating .unique values dataframe
print("\nUnique Perrmit Types")
PermitType = pd.DataFrame()
PermitType['PermitType'] = bp['PermitType'].unique()

print("\nUnique Perrmit Type Mapped")
PermitTypeMapped = pd.DataFrame()
PermitTypeMapped['PermitTypeMapped'] = bp['PermitTypeMapped'].unique()

print("\nPermit Class")
PermitClass = pd.DataFrame()
PermitClass['PermitClass'] = bp['PermitClass'].unique()

print("\nPermit Class Group")
PermitClassGroup = pd.DataFrame()
PermitClassGroup['PermitClassGroup'] = bp['PermitClassGroup'].unique()

print("\nPermit Class Mapped")
PermitClassMapped = pd.DataFrame()
PermitClassMapped['PermitClassMapped'] = bp['PermitClassMapped'].unique()

print("\nWork Class")
WorkClass = pd.DataFrame()
WorkClass['WorkClass'] = bp['WorkClass'].unique()

print("\nWork Class Group")
WorkClassGroup = pd.DataFrame()
WorkClassGroup['WorkClassGroup'] = bp['WorkClassGroup'].unique()

print("\nWork Class Mapped")
WorkClassMapped = pd.DataFrame()
WorkClassMapped['WorkClassMapped'] = bp['WorkClassMapped'].unique()

print("\nApplicant Name")
ApplicantName = pd.DataFrame()
ApplicantName['ApplicantName'] = bp['ApplicantName'].unique()

print("\nContractor Name")
ContractorName = pd.DataFrame()
ContractorName['ContractorName'] = bp['ContractorName'].unique()

bp_dtypes = pd.concat([PermitType, PermitTypeMapped, PermitClass,
                       PermitClassGroup, PermitClassMapped,
                       WorkClass, WorkClassGroup, WorkClassMapped,
                       ApplicantName, ContractorName], axis=1)


# Creating bp_res_only
bp_res_only = bp[bp['PermitClassMapped'] == "Residential"] # this line doesnt work


# Save Files
bp_dtypes.to_csv("bp_dtypes.csv")
bp.to_file("bp_trimmed.csv")
bp_res_only.to_file("bp_res_only.csv") # this line is not working because of the above line

print("#############")
print("Code Complete")
print("#############")

######################################################################
##### BAR CHART #####
#####################
##### COMPARING PermitType (by Quantity) AND (by Construction Cost)
##### % Single Construction Permit
##### % Residential Improvement Project
##### % Demolition
##### % Commercial / Multi Family Project
##### % Environmental Restoration Permit
######################################################################

######################################################################
##### PermitTypeMapped (by Quantity) AND (by Construction Cost)
######################################################################

######################################################################
#### PermitClass (by Type) AND (by Construction Cost)
######################################################################

######################################################################
#### PermitClassGroup (by Type) AND (by Construction Cost)
######################################################################

######################################################################
#### Create bp_res_only
#### Map out information previous with residential only...?
######################################################################

######################################################################
#### WorkClass (by Type) AND (by Construction Cost) AND (Avg Construction Cost?)
######################################################################