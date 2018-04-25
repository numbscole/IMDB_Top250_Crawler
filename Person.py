# Nick Scoles
# 4/17/18
# Collects a person who contributed to the relevant movie using
#   IMDB's person API
import requests
import json
import time
import os

def collectAPI_Info(self):
    url = 'https://www.theimdbapi.org/api/person?person_id='+self.Id
    response = requests.get(url)
    response.raise_for_status()
    personData = json.loads(response.text)
    return personData

# Alternate API provided by themoviedb.org
def collectAltAPI_Info(self,moviedb_Id = None, flag = False):
    # must create an account and request a key from their website
    #   the key used for this program was stored as an os environment variable
    #   and referenced through the os module
    key = os.getenv('API_movieDB_key')
    if moviedb_Id == None:
        # Can 'find' a person with imdb's id
        url = 'https://api.themoviedb.org/3/find/'+self.Id+'?api_key='+key+'&language=en-US&external_source=imdb_id'
    elif flag == False:
        # Can collect more information on a person through the id associated with themoviedb.org
        url = 'https://api.themoviedb.org/3/person/'+moviedb_Id+'?api_key='+key+'&language=en-US'
    elif flag == True:
        # several different requests can be sent to thmoviedb.org for information on a person/movie
        url = 'https://api.themoviedb.org/3/person/'+moviedb_Id+'/movie_credits?api_key='+key+'&language=en-US'
    response = requests.get(url)
    response.raise_for_status()
    personData = json.loads(response.text)
    return personData

class Person:
    def __init__(self,Id, department, tconst):
        self.Id = Id
        self.department = department
        self.movie = tconst
        self.gender = 'NULL'
        self.name = ''
        self.birthday = ''
        self.firstDirectedYear = 'NULL'

        # Had some issues with IMDB API not responding, was going to try and use
        #   an alternate API as a backup but decided to just fully use the
        #   alternate API instead.
        # Leaving the original code commented for reference

        # flag = False
        # try:
        #     start_time = time.time()
        #     data = collectAPI_Info(self)
        #     self.setAPI_Info(self,data)
        #     # IMDB might ban our ip address if we exceed 100 requests per minute
        #     #   that's 1.67 requests per second on average so we'll just
        #     #   make sure we dont go faster than .85 seconds of time per request
        #     #********************
        #     end_time = time.time()
        #     total_time = end_time - start_time
        #     while total_time < 0.85:
        #         time.sleep(.05)
        #         total_time = time.time() - start_time
        # except:
        #     flag = True
        # # If we fail to get a response from the official IMDB API, we will access an alternate API
        # if(flag == True):
        start_time = time.time()
        data = collectAltAPI_Info(self)
        self.setAltAPI_Info(data)
        end_time = time.time()
        total_time = end_time - start_time
        # Cant exceed 4 requests per second, this script makes a max of 3 requests
        while total_time < 0.75:
            time.sleep(.01)
            total_time = time.time() - start_time


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

    def setAPI_Info(self,data):
        self.name = data['title']
        self.setBirthday(data['birthday'])
        roles = data['type']
        if 'Actress' in roles:
            self.gender = 'Female'
        if 'Actor' in roles:
            self.gender = 'Male'
        if 'Director' in roles:
            self.setFRY(data['filmography'])

    def setFRY(self, filmography):
        directed_list = filmography['director']
        n = len(directed_list) - 1
        first_movie = directed_list[n]['title']
        self.firstDirectedYear = directed_list[n]['year']

    def setAltAPI_Info(self,data):
        person = data['person_results'][0]

        try:
            gender_num = person['gender']
            if gender_num == 1:
                self.gender = 'Female'
            elif gender_num == 2:
                self.gender = 'Male'
        except:
            pass
        self.name = person['name']
        try:
            moviedb_Id = str(person['id'])
            data_details = collectAltAPI_Info(self, moviedb_Id)
            try:
                self.setBirthday(data_details['birthday'])
            except:
                print('No birthday on record for '+self.name+' moviedb-id: '+moviedb_Id)
                self.birthday = 'NULL'
            try:
                if self.department == 'Directed':
                    self.setAltFRY(collectAltAPI_Info(self, moviedb_Id, True))
            except:
                self.firstDirectedYear = 'NULL'
        except:
            self.birthday = 'NULL'
            self.firstDirectedYear = 'NULL'

    def setAltFRY(self, data):
        # collect every movie this person was involved (excluding cast roles)
        movies = data['crew']
        movie_release_dates = []
        # recod the release date of any movie this person directed
        for m in movies:
            if m['job'] == 'Director' and m['release_date']!="":
                movie_release_dates.append(m['release_date'])
        split_dates_str = []
        for yd in movie_release_dates:
            # yyyy-mm-dd to [yyyy, mm, dd]
            s = yd.split('-')
            split_dates_str.append(s)
        # Changing string elements to integers
        split_dates_int = [list(map(int,x)) for x in split_dates_str]
        # Sorting by the years
        split_dates_int.sort(key = lambda x: x[0])
        # should be sorted, get first release year at front of array
        self.firstDirectedYear = str(split_dates_int[0][0])

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
