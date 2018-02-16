import csv
from imdb import IMDb
ia = IMDb()

reader_test = open('reader_test.csv')
reader = csv.reader(reader_test)

titles = []
for row in reader:
    movie = ia.search_movie(row[0], results=3)
    titles.append(movie)


writer_test = open('writer_test.csv', 'w')


writer = csv.writer(writer_test)
for item in titles:
    writer.writerow([item])
