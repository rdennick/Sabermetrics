#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:33:17 2017

@author: ryandennick

This code calculates the BaseRuns formula to get a better sense of a teams
'true talent'
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

# Milwaukee Brewers stats in index 0, National League stats in index 1
batting = ((1446,20978),(450,7723),(52,881),(29,590),
          (206,2657),(221,4101),(17,502),(110,1388),
          (38,553),(97,1804),(5683,92539),(21,607),(24,675))
# Milwaukee Brewers stats in index 0, National League stats in index 1
pitching = ((1440,20978),(432,7723),(61,881),(38,590),(164,2657),(216,4101),
            (16,502),(91,1388),(26,553),(109,1804),(5701,92539),(25,607),
            (24,675))
    

    
    