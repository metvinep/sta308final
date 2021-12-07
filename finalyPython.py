#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:30:56 2021

@author: elliotmetviner
"""

import pandas

census_region = pandas.read_csv("censusRegions.csv")
Opioid_deaths = pandas.read_csv("state_Opioid_deaths2019.csv")
state_abb = pandas.read_csv("state_abb_codes.csv")



Opioid_deaths= pandas.DataFrame(Opioid_deaths)
print(Opioid_deaths)

## rename column location as state to allow for merge:
Opioid_deaths= Opioid_deaths.rename(columns={"Location": "State"})

## merges state_abb data set with Opioid_data set by state:
merge1 = state_abb.merge(Opioid_deaths, on="State")

## mimizes data set to only contain Age Adjusted Rate and Code:
merge1 = merge1.loc[:,['Age adjusted Rate', 'Code']]

## renames columns "code" to "state" to allow for next merge:
merge1 = merge1.rename(columns={"Code": "State"})

## merges censuse_region data with the original merge1 data on state:
Opioid_region = census_region.merge(merge1, on="State")

## Re-names Age adjusted rate to AAR to allow for computation:
Opioid_region = Opioid_region.rename(columns={"Age adjusted Rate": "AAR"})

## minimizes data to contain AAR and Region
Opioid_region = Opioid_region.loc[:,['AAR', 'Region']]

## create data set that groups by Region and summarizes the mean:
Opioid_regionmean = Opioid_region.groupby('Region')['AAR'].mean()

## create data set that groups by Region and summarizes the Standard Deviation
Opioid_regionSTD = Opioid_region.groupby('Region')['AAR'].std()

## turn the last two lists into data frames to allow for a merge:
Opioid_regionSTD = pandas.DataFrame(Opioid_regionSTD)
Opioid_regionmean = pandas.DataFrame(Opioid_regionmean)

## Create new data set that merges the two previous data frames:
Opioid_data = Opioid_regionSTD.merge(Opioid_regionmean, on="Region")

## Renames AAR_x and AAR_y that were created in the merge to create relevant variable names
Opioid_data = Opioid_data.rename(columns={"AAR_x": "Standard_Deviation", "AAR_y": "Mean"})

## Computes the Coefficient of variation and creates a variable from it:
Opioid_data = Opioid_data.assign(COV_AAR = Opioid_data.Standard_Deviation / Opioid_data.Mean)












