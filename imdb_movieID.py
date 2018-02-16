import csv
from imdb import IMDb
ia = IMDb()

posters_reader = open('posters_reader.csv')
reader = csv.reader(posters_reader)

titles = []
for row in reader:
    movie = ia.search_movie(row[1], results=4)
    titles.append(movie)


posters_writer = open('posters_writer.csv', 'w')


writer = csv.writer(posters_writer)
for item in titles:
    writer.writerow([item])
