

from bs4 import BeautifulSoup
import requests
from Song import Song

class Music:
    def __init__(self,url):
        self.songList = []
        self.soupify(url)
        self.collectSongs()
        # self.lyrics

    def __str__(self):
        toString = 'Album contains: \n'
        for song in self.songList:
            toString = toString + song.getTitle() + '\n'
            toString = toString + '\tBy: '+song.getAuthor()+' @ length: '+song.getlength()+'\n'
        return toString

    def songs(self):
        return self.songList

    def soupify(self,url):
        source = requests.get(url).text
        self.soup = BeautifulSoup(source,'lxml')

    def collectSongs(self):
        script = self.soup.find('span',class_='ab_widget').text
        parsed = script.split(',')
        title_list_fluff = []
        artist_list_fluff = []
        duration_list_fluff = []
        title_list = []
        artist_list = []
        duration_list = []
        for p in parsed:
            if 'trackTitle' in p:
                title_list_fluff.append(p)
            if 'artists' in p:
                artist_list_fluff.append(p)
            if 'duration' in p:
                duration_list_fluff.append(p)
        #Garbage value
        del artist_list_fluff[0]
        for n in range(len(title_list_fluff)):
            title = title_list_fluff[n].split(':')
            title_list.append(title[1].replace('"',''))

            artist = artist_list_fluff[n].split(':')
            artist_list.append(artist[1].replace('"',''))

            duration = duration_list_fluff[n].split(':',1)
            duration_list.append(duration[1].replace('"',''))
        # print(title_list)
        # print(artist_list)
        # print(duration_list)
        for n in range(len(title_list)):
            newSong = Song(title_list[n],artist_list[n],duration_list[n])
            self.songList.append(newSong)
