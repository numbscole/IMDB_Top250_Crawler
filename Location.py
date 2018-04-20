#Class to hold location data

class Location:
    def __init__(self, tconst, country, city, state=None):
        self.country = country
        self.city = city
        self.state = state
        self.tconst = tconst
    def __str__(self):
        toString = 'Movie '+self.tconst+' was shot in '+self.city+ ' of '
        if self.state != None:
            toString = toString + self.state + ', '
        toString = toString + self.country
        return toString

    def getCity(self):
        return self.city
    def getState(self):
        return self.state
    def getCountry(self):
        return self.country
