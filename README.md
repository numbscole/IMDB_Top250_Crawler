# IMDB_Top250_Crawler

"Main" file to run the program is IMDB250_Crawler

This was designed to gather information from IMDB on each movie among the top 250 movie list. 
It also collects information from a subset of the people who worked on each movie by using IMDB's API. 
It stores all information collected in text separate text files to refer to later. 
(NOTE: This program takes at least 2.5+ hours to run)

To run this you will need to make sure you have the modules: BeautifulSoup, requests, json

*UPDATE
The format for a movie's soundtrack has changed since this crawler was orignially designed. Running the code as is should still collect all of the information EXCEPT for any information regarding the soundtrack.
