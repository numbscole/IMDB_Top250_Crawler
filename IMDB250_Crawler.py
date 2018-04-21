# Module requests is used to collect html info from a url
import requests
# Module bs4 (or BeautifulSoup4) is used to easily pull data from html code
#   It also makes the code much easier to read if you plan on printing or writing
#   the code to a file to read through.
from bs4 import BeautifulSoup
import time
from People import People
from Person import Person
from Movie import Movie
from Location import Location
from Award import Award
from Music import Music
from Song import Song


def setTitle(movie):
    try:
        # title is found withing the <tr> tag at
        #
        # <td class="titleColumn">
        #   1.
        #   <a href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&amp;pf_rd_r=1GESCSA65V4EF94TKR7W&amp;pf_rd_s=center-1&amp;pf_rd_t=15506&amp;pf_rd_i=top&amp;ref_=chttp_tt_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">
        #       The Shawshank Redemption
        #   </a>
        # :
        # </td>
        #
        return movie.find('td',class_='titleColumn').a.text
    except:
        print('Movie '+title+' hit problem at title')
        return str(-1)

def setRating(movie):
    # Rating found at (within the <tr> tag)
    # <td class="ratingColumn imdbRating">
    #     <strong title="9.2 based on 1,922,220 user ratings">
    #         9.2
    #     </strong>
    # </td>
    try:
        return movie.find('td',class_='ratingColumn imdbRating').strong.text
    except:
        print('Movie '+title+' hit problem at imdbRating')
        return str(-1)

def setTconst(movie):
    # tconst is found at (within the <tr> tag)
    # <div class="wlb_ribbon" data-recordmetrics="true" data-tconst="tt0111161">
    # </div>
    try:
        # t-constant is imdb's ID for the movie
        tconst = movie.find('div',class_='wlb_ribbon')['data-tconst']
        # print(movie.find('div',class_='wlb_ribbon'))
        return tconst
    except:
        print('url for movie '+title+' is broke')
        return str(-1)

def writeToFiles(movie_info, similar_info, genre_info, location_info,
            plays_in_info, cast_info, crew_info, works_on_info, writers_info,
            creates_info, music_info, artist_info, heard_in_info, award_record_info):
    movieFile = open('Data\movie.txt','a')
    similarFile = open('Data\similar.txt','a')
    genreFile = open('Data\genre.txt','a')
    locationFile = open('Data\location.txt','a')
    plays_inFile = open('Data\plays_in.txt','a')
    castFile = open('Data\cast.txt','a')
    crewFile = open('Data\crew.txt','a')
    works_onFile = open('Data\works_on.txt','a')
    writersFile = open('Data\writers.txt','a')
    createsFile = open('Data\creates.txt','a')
    musicFile = open('Data\music.txt','a')
    artistFile = open('Data\\artist.txt','a')
    heard_inFile = open('Data\heard_in.txt','a')
    award_recordFile = open('Data\\award_record.txt','a')
    try:
        for e in movie_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            movieFile.write(toWrite)
        for e in similar_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            similarFile.write(toWrite)

        for e in genre_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            genreFile.write(toWrite)

        for e in location_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            locationFile.write(toWrite)

        for e in plays_in_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            plays_inFile.write(toWrite)

        for e in cast_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            castFile.write(toWrite)

        for e in crew_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            crewFile.write(toWrite)

        for e in works_on_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            works_onFile.write(toWrite)

        for e in writers_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            writersFile.write(toWrite)

        for e in creates_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            createsFile.write(toWrite)

        for e in award_record_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            award_recordFile.write(toWrite)

        for e in music_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            musicFile.write(toWrite)

        for e in artist_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            artistFile.write(toWrite)

        for e in heard_in_info:
            toWrite = ''
            for n in range(len(e)):
                try:
                    toWrite = toWrite+e[n]+',\t'
                except:
                    toWrite = toWrite+''
            toWrite = toWrite+'\n'
            heard_inFile.write(toWrite)

    except:
        print('Error writing to file')

    movieFile.close()
    similarFile.close()
    genreFile.close()
    locationFile.close()
    plays_inFile.close()
    castFile.close()
    crewFile.close()
    works_onFile.close()
    writersFile.close()
    createsFile.close()
    musicFile.close()
    artistFile.close()
    heard_inFile.close()
    award_recordFile.close()


def getInfo(dictionary, movies):
    ErrorFile = open('Data\errors.txt','a')
    scannedMovies = []
    num_in_line = 0
    movie_count = len(movies)
    for movie in movies:
        num_in_line = num_in_line + 1
        try:
            # Creating lists containing information to be written to a file
            movie_info = []
            similar_info = []
            genre_info = []
            location_info = []
            plays_in_info = []
            cast_info = []
            crew_info = []
            works_on_info = []
            writers_info = []
            creates_info = []
            music_info = []
            artist_info = []
            heard_in_info = []
            award_record_info = []

            start_time = time.time()
            title = setTitle(movie)
            rating = setRating(movie)
            tconst = setTconst(movie)
            thisMovie = Movie(title,rating,tconst)
            dictionary[tconst] = title
            persons = People(tconst).getPeople()
            director = None
            cast = []
            writers = []
            crew = []
            for p in range(len(persons)):
                try:
                    if(persons[p].getDepartment() == 'Directed'):
                        director = persons[p]
                        del persons[p]
                    elif(persons[p].getDepartment() == 'Cast'):
                        cast.append(persons[p])
                    elif(persons[p].getDepartment() == 'Writing Credits'):
                        writers.append(persons[p])
                    else:
                        crew.append(persons[p])
                except:
                    print('\n\n\nerr\n\n\n')

            movie_info.append([title,thisMovie.getRD_date(),thisMovie.getTime_len(),
                            thisMovie.getContentRating(),rating,thisMovie.getBO_GrossUSA(),
                            thisMovie.getBO_GrossWorld(), thisMovie.getBudget(),thisMovie.getON_Earnings(),
                            thisMovie.getON_Date(), director.getName(), director.getFRY(), director.getBirthday()])
            sims = thisMovie.getSimilarMovieTitles()
            for s in sims:
                similar_info.append([title, s])
            genres = thisMovie.getGenres()
            for g in genres:
                genre_info.append([title, g])
            locations = thisMovie.getLocations()
            for local in locations:
                location_info.append([title, local.getCountry(), local.getCity(), local.getState()])
            for p in cast:
                plays_in_info.append([p.getName(), title])
                cast_info.append([p.getName(),p.getGender(), p.getBirthday()])
            for c in crew:
                crew_info.append([c.getName(),c.getDepartment(),c.getBirthday()])
                works_on_info.append([c.getName(),title])
            for w in writers:
                writers_info.append([w.getName(), w.getBirthday()])
                creates_info.append([w.getName(), title])

            awards = thisMovie.getAwards()
            for a in awards:
                award_record_info.append([title,a.getAward(),a.getYear(),a.getCategory()])

            music = thisMovie.getMusic()
            if music != None:
                song_list = music.songs()
                for song in song_list:
                    music_info.append([song.getTitle(), song.getlength()])
                    artist_info.append([song.getTitle(), song.getAuthor()])
                    heard_in_info.append([title, song.getTitle()])

            writeToFiles(movie_info, similar_info, genre_info, location_info,
            plays_in_info, cast_info, crew_info, works_on_info, writers_info,
            creates_info, music_info, artist_info, heard_in_info, award_record_info)

            # Movie was successfuly scanned for information
            scannedMovies.append(movie)

            end_time = time.time()
            print('\nEnded search in '+str(end_time-start_time)+' seconds on movie '+title +' , movie number '+str(num_in_line)+' out of '+str(movie_count))

        except Exception as err:
            toWrite = 'Failed to scan movie '+setTitle(movie)
            toWrite = toWrite + '\n\tError due to '+str(err)
            ErrorFile.write(toWrite)
    ErrorFile.close()
    return scannedMovies

if __name__ == '__main__':
    print('Crawling now')
    start_time = time.time()
    # Collect the html code
    source = requests.get('http://www.imdb.com/chart/top').text
    # Soupify the code
    soup = BeautifulSoup(source,'lxml')

    # Each movie on the list in the html code is contained within the tag <tr>..<\tr>
    movies = soup.findAll('tr')
    # A few junk values of 'tr' have to be deleted to only have movie info in the list
    del movies[-1]
    del movies[-1]
    del movies[0]

    # Creating a dictionary to connect tconst and a movie's title
    dictionary = {}


    scannedMovies = []
    scannedCount = 0
    count = 0

    scannedMovies = getInfo(dictionary, movies)
    # while(len(movies) >= 1 or count <= 25):
    #     scannedMovies = getInfo(dictionary, movies)
    #     count = count + 1
    #     scannedCount = scannedCount + len(scannedMovies)
    #     print('Number of scanned movies: '+str(scannedCount))
    #     print('After '+str(count)+' loops\n')
    #     for m in scannedMovies:
    #         try:
    #             movies.remove(m)
    #         except:
    #             print('movie '+getTitle(m)+ ' not in current list')

    end_time = time.time()
    total_time = end_time - start_time
    print('stopped at:'+str(total_time))
