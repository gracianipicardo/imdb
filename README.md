# IMDb reconciliation workflow

Attempt to use the IMDb API to reconcile our posters digital collection with IMDb (http://www.imdb.com/) records and retrieve additional metadata (cast, country, genre, etc...). I am not a python expert so the code might have some flaws and there are probably more efficient ways of doing it, but it works for this project.

It uses Davide Alberani's python package IMDbPY to retrieve and manage the data of the IMDb movie database. Information about installing and woring with IMDbPY can be found here: https://github.com/alberanid/imdbpy

The script imdb_movieID.py, reads all the titles from a .csv file, sends the request to IMDb, and writes the retrieved information on a second .csv file. This script just retrieves the top 4 title matches on the Db and includes imdbID, title, and year.

Next step will be altering the search strategy so there are two matching factors, title and year.

More to come...
