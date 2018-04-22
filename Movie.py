# Nick Scoles
# 3/5/2018

from bs4 import BeautifulSoup
import requests
# import csv
from Music import Music
from Location import Location
from Award import Award

def imdb_link(tconst):
    link = 'http://www.imdb.com/title/' + tconst
    m_source = requests.get(link).text
    return BeautifulSoup(m_source,'lxml')

def date_full(m_soup):
    try:
        Release_fluff = m_soup.find(text='Release Date:')
        a = Release_fluff.parent.next_sibling.strip()
        return a.split(' ')
        # RD_day = b[0]
        # RD_month = b[1]
        # RD_year = b[2]
    except:
        return [str(-1),str(-1),str(-1)]

class Movie:
    def __init__(self, title, imdb_rating, tconst):
        soup = imdb_link(tconst)
        self.title = title
        self.imdb_rating = imdb_rating
        self.Locations = []
        self.Genres = []
        self.Awards = []
        self.SimilarMovieTitles = []
        self.setSimilarMovieTitles(soup)
        self.setAwards(tconst)
        self.setGenre(soup)
        self.setLocations(tconst)
        self.rated = self.content(soup)
        date = date_full(soup)
        self.setDate(date)
        self.length = self.time_len(soup)
        self.BO_GrossUSA = self.GUSA(soup)
        self.BO_GrossWorld = self.GWorld(soup)
        self.BO_Budget = self.Budget(soup)
        self.ON_Earnings = self.open_earn(soup)
        self.ON_Date = self.open_date(soup)
        self.setMusic(tconst)

    def __str__(self):
        # This function is comparable to Java's toString method
        a = self.title + ' has an imdb rating of ' + self.imdb_rating + ' and is rated ' + self.rated
        b = '\n\tIt\'s release date was '+self.RD_day+' of '+self.RD_month+ ', '
        c = self.RD_year+', and has grossed '+self.BO_GrossWorld+' in the world.'
        return a+b+c

    def content(self,m_soup):
        # is the movie pg13, R, pg, etc.
        try:
            return m_soup.find(itemprop="contentRating").next_sibling.strip()
        except:
            return 'NULL'
    def getContentRating(self):
        return self.rated

    def setDate(self,date_full):
        try:
            # Check if first index contains a number value for the day
            has_day = int(date_full[0])
            # If our current try statement hasn't failed, then we have the actual day
            # Set the dates
            self.RD_day = date_full[0]
            self.RD_month = date_full[1]
            self.RD_year = date_full[2]
        except:
            # no day value found (every movie in list still has release month and year)
            self.RD_day = '1'   # Setting day to 1
            self.RD_month = date_full[0]
            self.RD_year = date_full[1]
    def getRD_date(self):
        # Reformatting to string as DD-MON-YY for Oracle
        date = ''
        if len(self.RD_day) == 1:
            date = '0'+self.RD_day+'-'
        else:
            date = self.RD_day+'-'
        MON = self.RD_month[:3].upper()
        yy = self.RD_year[2:]
        date = date + MON + '-' + yy
        return date

    def time_len(self,m_soup):
        # Returns the length of the movie
        try:
            return m_soup.find(itemprop='duration').text.strip()
        except:
            return 'NULL'
    def getTime_len(self):
        return self.length

    def GUSA(self,m_soup):
        # Returns Gross USA
        try:
            BO_GrossUSA = m_soup.find(text='Gross USA:').parent.next_sibling.strip()
            return BO_GrossUSA.replace(',','')
        except:
            return 'NULL'
    def getBO_GrossUSA(self):
        return self.BO_GrossUSA

    def GWorld(self,m_soup):
        # Returns Gross World
        try:
            BO_GrossWorld = m_soup.find(text='Cumulative Worldwide Gross:').parent.next_sibling.strip()
            return BO_GrossWorld.replace(',','')
        except:
            return 'NULL'
    def getBO_GrossWorld(self):
        return self.BO_GrossWorld

    def Budget(self,m_soup):
        # Returns Budget
        try:
            BO_Budget = m_soup.find(text='Budget:').parent.next_sibling.strip()
            return BO_Budget.replace(',','')
        except:
            return 'NULL'
    def getBudget(self):
        return self.BO_Budget

    def open_earn(self,m_soup):
        # Returns money earned on opening day
        try:
            opening_wknd = m_soup.find(text='Opening Weekend USA:')
            ON_Earnings = opening_wknd.parent.next_sibling.strip()
            return ON_Earnings.replace(',','')
        except:
            return str('NULL')
    def getON_Earnings(self):
        return self.ON_Earnings

    def open_date(self,m_soup):
        # Returns date of opening weekend as a string in Orcale DATE format
        try:
            opening_wknd = m_soup.find(text='Opening Weekend USA:')
            strings = opening_wknd.parent.next_sibling.next_sibling.text.split()
            date = ''
            if len(strings[0]) == 1:
                date = '0'+strings[0]+'-'
            else:
                date = strings[0]+'-'
            MON = strings[1][:3].upper()
            yy = strings[2][2:]
            date = date + MON + '-' + yy
            return date
        except:
            return str('NULL')
    def getON_Date(self):
        return self.ON_Date

    def setMusic(self,tconst):
        try:
            # Follows the link to the soundtrack for the movie
            sublink = tconst + '/soundtrack'
            url = 'http://www.imdb.com/title/' + sublink
            # Music will take the url and collect a list of songs from the link
            self.music = Music(url)
        except:
            print('\t*M Error getting music for '+self.title+' IMDB-id: '+tconst)
            self.music = None
    def getMusic(self):
        return self.music

    def setLocations(self,tconst):
        sublink = tconst + '/locations'
        url = 'http://www.imdb.com/title/' + sublink
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        # print(soup.prettify())
        # Grab all of the filming location data
        locations_O = soup.findAll('div',class_='soda sodavote odd')
        # locations_O = locations_O.find('dt')
        locations_E = soup.findAll('div',class_='soda sodavote even')
        # locations_E = locations_E.findAll('dt')
        locations_html = locations_O + locations_E

        countrys = []
        citys = []
        for local in locations_html:
            locations = []
            l = local.find('dt').a.text
            locations = l.split(',')

            if len(locations) >= 3:
                # some info may contain extra info like a street address or landmark
                #   however the order of the last three elements is always city,state,country
                country = locations[-1].rstrip('\n')
                state = locations[-2]
                city = locations[-3]
                if country not in countrys and city not in citys:
                    countrys.append(country)
                    citys.append(city)
                    self.Locations.append(Location(tconst,country,city,state))
            elif len(locations) == 2:
                # May only have info on the country and either city or state (classified as city)
                country = locations[1].rstrip('\n')
                city = locations[0]
                if country not in countrys and city not in citys:
                    countrys.append(country)
                    citys.append(city)
                    self.Locations.append(Location(tconst,country,city, 'NULL'))

    def getLocations(self):
        return self.Locations

    def setGenre(self,m_soup):
        titleBar = m_soup.find('div',class_='subtext')
        temp = titleBar.select('.itemprop')
        genres = []
        for t in temp:
            genres.append(t.text.strip())
        self.Genres = genres
    def getGenres(self):
        return self.Genres

    def setAwards(self,tconst):
        sublink = tconst + '/awards'
        url = 'http://www.imdb.com/title/' + sublink
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        main_soup = soup.find('div', class_='article listo')
        ceremonys = main_soup.findAll('h3')
        tables = main_soup.findAll('table')
        years = []
        tables_of_interest = []
        # first value is not an actual ceremony
        del ceremonys[0]
        # Only interested in a few ceremonys
        for n in range(len(ceremonys)):
            if 'Academy Awards, USA' in ceremonys[n].text:
                tables_of_interest.append(tables[n])
                years.append(ceremonys[n].a.text)
            elif 'Golden Globes, USA' in ceremonys[n].text:
                tables_of_interest.append(tables[n])
                years.append(ceremonys[n].a.text)
            elif 'BAFTA Awards' in ceremonys[n].text:
                tables_of_interest.append(tables[n])
                years.append(ceremonys[n].a.text)


        for tbl in range(len(tables_of_interest)):
            tags = tables_of_interest[tbl].findAll('tr')
            year = years[tbl].strip()
            # print(tags)
            flag = False
            award = None
            for tg in tags:
                # print('\n\n')
                # print(tg)
                try:
                    outcome = tg.find('td',class_='title_award_outcome').b.text.split()
                    flag = True
                except:
                    flag = False

                if(flag == True):
                    if('Winner' in outcome):
                        award = tg.find('span').text
                    else:
                        award = None
                if(award != None):
                    category = tg.find('td',class_='award_description').text.split('\n')[1].strip()
                    # print(self.title + ' won a '+award+' in '+year+' for')
                    # print(category)
                    self.Awards.append(Award(tconst,award,year,category))
    def getAwards(self):
        return self.Awards

    def setSimilarMovieTitles(self,m_soup):
        slide = m_soup.find('div',class_='rec_slide')
        elements = slide.findAll('img')
        for e in elements:
            self.SimilarMovieTitles.append(e['title'])
    def getSimilarMovieTitles(self):
        return self.SimilarMovieTitles
