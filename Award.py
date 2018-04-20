class Award:
    def __init__(self,tconst,Award,Year,Category):
        self.tconst = tconst
        self.Award = Award
        self.Year = Year
        self.Category = Category
    def __str__(self):
        toString = 'Movie: '+self.tconst+', recieved a '+self.Award+' in '+self.Year
        toString=toString+' in the category: '+self.Category
        return toString

    def getAward(self):
        return self.Award
    def getYear(self):
        return self.Year
    def getCategory(self):
        return self.Category
    def gettconst(self):
        return self.tconst
