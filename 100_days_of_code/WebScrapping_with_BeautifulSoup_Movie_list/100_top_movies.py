from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
best_movies_site = response.text

soup = BeautifulSoup(best_movies_site, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

with open("100_top_movies.txt", "w") as file:
    all_movies.reverse()
    for title in all_movies:
        movie = title.getText()
        file.write(f"{movie} \n")

# Udemy solution
# movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles[::-1])