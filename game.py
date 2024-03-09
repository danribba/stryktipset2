import math



class Game:
    def __init__(self, homeTeam, awayTeam, homeGoals, awayGoals, xpGoalsHomeTeam, xpGoalsAwayTeam):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homeGoals = homeGoals
        self.awayGoals = awayGoals
        self.expectedHG = xpGoalsHomeTeam 
        self.expectedAG = xpGoalsAwayTeam
        self.homeProb = 0
        self.drawProb = 0
        self.awayProb = 0
        self.bet = None


    