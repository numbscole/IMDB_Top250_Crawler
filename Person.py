# Nick Scoles
# 4/17/18
# Collects a person who contributed to the relevant movie using
#   IMDB's person API
import requests
import json

def collectAPI_Info(self):
    url = 'https://www.theimdbapi.org/api/person?person_id='+self.Id
    response = requests.get(url)
    response.raise_for_status()
    personData = json.loads(response.text)
    return personData

class Person:
    def __init__(self,Id, department, tconst):
        self.Id = Id
        self.department = department
        self.movie = tconst
        self.gender = 'null'
        data = collectAPI_Info(self)
        self.name = data['title']
        self.birthday = ''
        self.setBirthday(data['birthday'])
        self.firstDirectedYear = 'NULL'

        roles = data['type']
        if 'Actress' in roles:
            self.gender = 'Female'
        if 'Actor' in roles:
            self.gender = 'Male'
        if 'Director' in roles:
            self.setFRY(data['filmography'])

    def __str__(self):
        toString = self.name + ' was born in '+self.birthday+' and worked as a(n) '
        toString = toString + self.department + ', '
        toString = toString + 'working in the movie(s) '
        toString = toString + self.movie
        return toString

    def getDepartment(self):
        return self.department
    def getMovie(self):
        return self.movie
    def getID(self):
        return self.Id
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender


    def setFRY(self, filmography):
        directed_list = filmography['director']
        n = len(directed_list) - 1
        first_movie = directed_list[n]['title']
        self.firstDirectedYear = directed_list[n]['year']
    def getFRY(self):
        return self.firstDirectedYear

    def setBirthday(self,string):
        # Setting birthday to Oracle DATE string
        try:
            s = string.split('-')
            yy = s[0][2:]
            MON = ''
            if(s[1] == '1'):
                MON = 'JAN'
            elif(s[1] == '2'):
                MON = 'FEB'
            elif(s[1] == '3'):
                MON = 'MAR'
            elif(s[1] == '4'):
                MON = 'APR'
            elif(s[1] == '5'):
                MON = 'MAY'
            elif(s[1] == '6'):
                MON = 'JUN'
            elif(s[1] == '7'):
                MON = 'JUL'
            elif(s[1] == '8'):
                MON = 'AUG'
            elif(s[1] == '9'):
                MON = 'SEP'
            elif(s[1] == '10'):
                MON = 'OCT'
            elif(s[1] == '11'):
                MON = 'NOV'
            else:
                MON = 'DEC'
            dd = ''
            if(len(s[2]) == 1):
                dd = '0'+s[2]
            else:
                dd = s[2]

            self.birthday = dd + '-' + MON + '-' + yy
        except:
            self.birthday = 'NULL'

    def getBirthday(self):
        return self.birthday
