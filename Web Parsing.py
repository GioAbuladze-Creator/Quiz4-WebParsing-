import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


page = 1
while page < 6:

    main_link = f"http://geo.saitebi.ge/cat/3/{page}/anime.html"

    resp = requests.get(main_link)
    text = resp.text
    soup = BeautifulSoup(text, 'html.parser')

    file = open('movies.csv', 'a', encoding='utf-8_sig')
    headings = 'სახელი,სახელი ინგლისურად,გამოშვების წელი,ლინკი \n'
    file.write(headings)

    all_movies = soup.findAll("div", {"class": "movie-items-wraper"})
    for movie in all_movies:
        title_bar = movie.find('a', {"class": "movie-items"})
        title = title_bar.h4.text
        titleInEnglish = title_bar.find("h4", {"class": "b"}).text
        url = ('http://geo.saitebi.ge/' + title_bar.attrs['href']).replace(' ', '')

        year = title_bar.span.text
        file.write(title + ',' + titleInEnglish + ',' + year + ',' + url + '\n')

    print(main_link)
    page+=1
    # sleep(randint(15,20))





