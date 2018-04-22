from bs4 import BeautifulSoup
import requests
from Person import Person

def getIDsFromTable(table, number = 3):
    a_tags = table.findAll('tr')
    count = 0
    IDs_toReturn = []
    for tag in a_tags:
        if tag.a != None and count < number:
            split_link = tag.a['href'].split('/')
            ID = split_link[2]
            # print(ID)
            IDs_toReturn.append(ID)
            count = count + 1
    return IDs_toReturn

def getCreditDictionary(tconst):
    link = 'http://www.imdb.com/title/'+tconst+'/fullcredits'
    m_source = requests.get(link).text
    soup = BeautifulSoup(m_source,'lxml')
    info = soup.find('div',class_='header')
    departments_headers = info.findAll('h4')
    tables = info.findAll('table')
    departments = []
    dictionary = {}
    for d in range(len(departments_headers)):
        # d.remove(' by')
        txt = departments_headers[d].text.strip().split('\n')
        dep = txt[0]
        if ' by' in dep:
            dep = dep.rstrip('by').strip()
            departments.append(dep)
            dictionary[dep] = getIDsFromTable(tables[d])
        elif ' By' in dep:
            dep = dep.rstrip('By').strip()
            departments.append(dep)
            dictionary[dep] = getIDsFromTable(tables[d])
        elif 'Writing' in dep:
            departments.append('Writing')
            dictionary[dep] = getIDsFromTable(tables[d])
        elif 'Cast' in dep:
            if dep == 'Cast':
                dictionary[dep] = getIDsFromTable(tables[d],30)
            else:
                dictionary[dep] = getIDsFromTable(tables[d])
            departments.append(dep)
        # print(dep)

    if 'Thanks' in departments:
        departments.remove('Thanks')
    if 'Other crew' in departments:
        departments.remove('Other crew')
    # print(departments)
    # print(dictionary)
    # print(info)
    return dictionary

class People:
    def __init__(self, tconst):
        self.movieId = tconst
        dictionary = getCreditDictionary(tconst)
        self.highlight_people = self.findPeople(dictionary,tconst)

    def __str__(self):
        toString = ''
        for p in self.highlight_people:
            try:
                toString = toString + p.__str__() + '\n'
            except Exception as err:
                print('Exception happened '+str(err))
        return toString

    def findPeople(self, dic, tconst):
        thePeople = []
        keys = list(dic.keys())
        for dep in keys:
            dep_IDs = dic[dep]
            for ID in dep_IDs:
                try:
                    p = Person(ID,dep,tconst)
                    thePeople.append(p)
                    # print(p)
                except:
                    print('Error getting data for person '+str(ID)+' and has been thrown out of the search on movie '+str(tconst))
        return thePeople

    def getPeople(self):
        return self.highlight_people
