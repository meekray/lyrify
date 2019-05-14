
"""Interacting with the Spotify and Genius APIs"""

from bs4 import BeautifulSoup
from flask import Flask
from lyrify import CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN
import requests
import sys
class GeniusAPI():
    def __init__(self):
        _ = 0

    @classmethod
    def get_song_url(artist, song, album = None):
        url = ''
        return url

    @staticmethod
    def scrap_song_url(url):
        song = requests.get(url)
        html = BeautifulSoup(song.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics
        
# if __name__ == "__main__":
    # genius = GeniusAPI()
    # genius_url = get_song_url("Drake", "Jungle")

def main(args=None):
    genius = GeniusAPI()
    print (genius.scrap_song_url('https://genius.com/Drake-jungle-lyrics'))

if __name__ == "__main__":
    main()