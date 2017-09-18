#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:54:23 2017

@author: ryandennick
"""

# designing a class to determine a players Wins Above Replacement

"""
class League(object):
    
    def __init__(self,lgwOBA,wOBAScale,R_PA,lgwRC,lgPA,lgBattingRuns,lgBsR,lgFldRuns,lgPosAdj,MLBrunsScored,MLBInningsPitched):
        self.lgwOBA = lgwOBA
        self.wOBAScale = wOBAScale
        self.R_PA = R_PA
        self.lgwRC = lgwRC
        self.lgPA = lgPA
        self.lgBattingRuns = lgBattingRuns
        self.lgBsR = lgBsR
        self.lgFldRuns = lgFldRuns
        self.lgPosAdj = lgPosAdj
        self.MLBrunsScored = MLBrunsScored
        self.MLBInningsPitched = MLBInningsPitched
"""   
    
    

class PlayerWar:
    
    def __init__(self,playerName,team,wOBA,PA,baseRuns,uzr,lgwOBA,wOBAScale,R_PA,lgwRC,lgPA,lgBattingRuns,lgBsR,lgFldRuns,lgPosAdj,MLBrunsScored,MLBInningsPitched):
        self.playerName = playerName
        self.Park_Factor = self.set_Park_Factor(team)
        self.wOBA = wOBA
        self.PA = PA
        self.baseRuns = baseRuns
        self.uzr = uzr
        self.lgwOBA = lgwOBA
        self.wOBAScale = wOBAScale
        self.R_PA = R_PA
        self.lgwRC = lgwRC
        self.lgPA = lgPA
        self.lgBattingRuns = lgBattingRuns
        self.lgBsR = lgBsR
        self.lgFldRuns = lgFldRuns
        self.lgPosAdj = lgPosAdj
        self.MLBrunsScored = MLBrunsScored
        self.MLBInningsPitched = MLBInningsPitched
        
    def set_Park_Factor(self,team):
        if team.title() in ["Angels","Dodgers","Giants","Mets"]:
            self.Park_Factor = 95
            return self.Park_Factor
        elif team.title() in ["Athletics","Mariners","Padres","Pirates"]:
            self.Park_Factor = 96
            return self.Park_Factor
        elif team.title() == "Rays":
            self.Park_Factor = 97
            return self.Park_Factor
        elif team.title() in ["Astros","Cardinals","Marlins"]:
            self.Park_Factor = 98
            return self.Park_Factor
        elif team.title() in ["Braves","Cubs","Phillies"]:
            self.Park_Factor = 99
            return self.Park_Factor
        elif team.title() == "Nationals":
            self.Park_Factor = 100
            return self.Park_Factor
        elif team.title() in ["Reds","Tigers","White Sox","Yankees"]:
            self.Park_Factor = 101
            return self.Park_Factor
        elif team.title() in ["Blue Jays","Indians","Orioles","Twins"]:
            self.Park_Factor = 102
            return self.Park_Factor
        elif team.title() in ["Brewers","Royals"]:
            self.Park_Factor = 103
            return self.Park_Factor
        elif team.title() == "Rangers":
            self.Park_Factor = 104
            return self.Park_Factor
        elif team.title() in ["Diamondbacks","Red Sox"]:
            self.Park_Factor = 105
            return self.Park_Factor
        elif team.title() == "Rockies":
            self.Park_Factor = 118
            return self.Park_Factor
        
        
    def battingRuns(self):
        wRAA = ((self.wOBA-self.lgwOBA)/self.wOBAScale)*self.PA
        return round(wRAA + (self.R_PA - ((self.Park_Factor/100.0)*self.R_PA))*self.PA + (self.R_PA-(self.lgwRC/self.lgPA))*self.PA,0)
       
    def positionalAdjustment(self,InningsPlayed1,runValue1,InningsPlayed2 = False,runValue2 = False,InningsPlayed3 = False,runValue3 = False):
        primary = ((InningsPlayed1/9)/162)*runValue1
        backup = ((InningsPlayed2/9)/162)*runValue2
        emergency = ((InningsPlayed3/9)/162)*runValue3
        positions = primary + backup + emergency
        return positions - .14
        
    def leagueAdjustment(self):
        return round(((-1)*(self.lgBattingRuns+self.lgBsR+self.lgFldRuns+self.lgPosAdj)/self.lgPA)*self.PA,1)

      
    
    def replacementRuns(self,MLBgames):
        runs = ((570*(MLBgames/2430.0))*(self.runsPerWin()/self.lgPA)*self.PA)
        return round(runs,1)
        
    def runsPerWin(self):
        return round(9*(self.MLBrunsScored/self.MLBInningsPitched)*1.5+3,3)
    # does not work correctly yet
    def WAR(self):    
        return (self.battingRuns()+self.baseRuns+self.uzr+self.positionalAdjustment(InningsPlayed1,runValue1,InningsPlayed2 = False,runValue2 = False,InningsPlayed3 = False,runValue3 = False)+self.leagueAdjustment()+self.replacementRuns(self.MLBgames))/self.runsPerWin()
    
#NL = League(.318,1.212,.118,10783,87564,-696.5,42.7,-14.3,516.8,21744,43306.1)
Murph = PlayerWar("Daniel Murphy","Nationals",.408,582,3.4,-7.9,.318,1.212,.118,10783,87564,-696.5,42.7,-14.3,516.8,21744,43306.1)

print(Murph.runsPerWin())
print(Murph.battingRuns())
print(Murph.leagueAdjustment())
print(Murph.positionalAdjustment(1016.1,2.5,151.1,-12.5))
print(Murph.replacementRuns(2428))
print(Murph.baseRuns)
print(Murph.WAR())

"""
print(Murph.playerBattingRuns(battingRuns,.318,1.212,.118,118.0,10783.0,87564.0))
print(Murph.playerBaserunningRuns(baseRuns,-0.4))
print(Murph.playerFieldingRuns(fieldingRuns,-3.0))
print(Murph.playerPositionalAdj(positionalAdjustment,1242.2,2.5))
print(Murph.playerLeagueAdj(leagueAdjustment,-696.5,42.7,-14.3,516.8,87546,582))
print(Murph.playerRunsPerWin(runsPerWin,21744,43306.1))
print(Murph.playerReplacementLvlRuns(replacementRuns,2428,184578,635))
"""






#,582,.318,1.212,.118,100,10783,87564.0,3.4,-7.9,-696.5,42.7,-14.3,516.8,21744,43306.1,2428,1016.1,151.1,2.5,-12.5,184578
