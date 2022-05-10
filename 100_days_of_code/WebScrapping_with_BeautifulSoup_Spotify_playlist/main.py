import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "43dd4750cb8e41f18ae2e54275f131a4"
SPOTIPY_CLIENT_SECRET = "b43f2a3505584ad9a968c31d96c5bb41"

user_input = input("Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")
url_billboard = f"https://www.billboard.com/charts/hot-100/{user_input}/"
response = requests.get(url=url_billboard)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")
song_titles = soup.select(selector="li #title-of-a-story")
top_100_song = [song.get_text().strip() for song in song_titles]
print(top_100_song)

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

