#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:33:17 2017

@author: ryandennick

This code calculates the BaseRuns formula to get a better sense of a teams
'true talent'
As of October 5th 2017, National League Runs = 11,139
                        American League Runs = 11,443
"""

#Inuputs:
    # Hits
    # Walks
    # Hit by pitch
    # Intentional Walks
    # Home runs
    # Doubles
    # Triples
    # Stolen bases
    # Caught stealing
    # Grounded into double play
    # Plate appearances
    # Sac flies
    # Sac hits
    # league runs scored
    # league raw BaseRuns
    # Games played

def rawBaseRuns(H,BB,HBP,IBB,HR,DBL,TPL,SB,CS,GDP,PA,SF,SH):
    # raw baseruns calculates non-league adjusted baseruns for a team
    #TB = total bases
    TB = (H-DBL-TPL-HR)+(DBL*2)+(TPL*3)+(HR*4)
    A = (H + BB + HBP - (0.5*IBB) - HR)
    B = 1.1*(1.4*TB-0.6*H-3*HR+0.1*(BB+HBP-IBB)+0.9*(SB-CS-GDP))
    C = (PA-BB-SF-SH-HBP-H+CS+GDP)
    D = HR
    rawBaseRuns = ((A*B)/(B+C)) + D
    return round(rawBaseRuns,2)
    
def baseRuns(values,lgRuns,G):
    # team values as inputs
    teamValues = [i[0] for i in values]
    # league values as inputs
    lgValues = [i[1] for i in values]
    teamRawBaseRuns = rawBaseRuns(*teamValues)
    lgRawBaseRuns = rawBaseRuns(*lgValues)
    # BaseRuns league adjustment
    baseRunsLA = (lgRuns)/(lgRawBaseRuns)
    baseRuns = round(teamRawBaseRuns*baseRunsLA,2)
    return round(baseRuns/G,2)
#######################################################################

#Houston Astros Test Data
#Astros data  stats in index 0, American League data starts in index 1
astrosBatting = ((1581,21229),(509,7785),(70,884),(27,361),
          (238,3170),(346,4194),(20,334),(98,1272),
          (42,458),(139,1958),(6271,92622),(61,614),(11,272))
americanLeagueRuns = 11443
games = 162
print(baseRuns(astrosBatting,americanLeagueRuns,games)
#######################################################################
#Cincinnati Reds Test Data
#Reds data stats in index 0, National League stats in index 1
redsPitching = ((1390,20985),(565,8044),(72,879),(41,609),(219,2935),(249,4203),
            (38,461),(120,1255),(39,476),(116,1846),(6213,92673),(42,554),
            (50,653))
nationalLeagueRuns = 11139
games = 162
print(baseRuns(redsPitching,nationalLeagueRuns,games)
    

    
    
