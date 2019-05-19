"""Interacting with the Spotify and Genius APIs"""

from bs4 import BeautifulSoup
from pprint import pprint
from lyrify.keys import *
import requests
import sys

class Song():
    AUTHORITY = 'https://api.genius.com/'

    def __init__(self, data):
        print (data)
        self.title = data['song']
        self.artist = data['artist']
        self.album = data['album']
        self.url = self.get_song_url(self)
        self.lyrics = self.get_lyrics(self)

    @staticmethod
    def get_song_url(self):
        query = ''.join([self.artist, ' ', self.title])
        
        search_endpoint = ''.join([self.AUTHORITY, 'search?q=', query, '&access_token=', GENIUS_CLIENT_ACCESS_TOKEN])
        response = requests.get(search_endpoint).json()

        if response['meta']['status'] == 200 and len(response["response"]["hits"]) > 0:
            return (response["response"]["hits"][0]['result']['url'])
        else:
            return None

    @staticmethod
    def get_lyrics(self):
        song = requests.get(self.url)
        html = BeautifulSoup(song.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics

def test():
    data = {}
    data["song"] = "Crew Love"
    data["artist"] = "Drake"
    data["album"] = "Take Care"
    song = Song(data)
    print (song.url)
    pprint (song.lyrics)
    return 0
    
if __name__ == "__main__":
    test()