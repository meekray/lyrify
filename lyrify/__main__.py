"""Interacting with the Spotify and Genius APIs"""

from bs4 import BeautifulSoup
from flask import Flask
from pprint import pprint
from lyrify import CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN
import requests
import sys

class SpotifyAPI():
    album = None
    artist = None
    song = None

    def __init__(self):
        self.song = "Street lights"
        self.artist = "Kanye West"

class GeniusAPI():
    authority = 'https://api.genius.com/'

    @classmethod
    def get_song_url(self, artist, song, album = None):
        query = ''.join([artist, ' ', song])
        if album:
            query += album
        
        search_endpoint = ''.join([self.authority, 'search?q=', query, '&access_token=', CLIENT_ACCESS_TOKEN])
        response = requests.get(search_endpoint).json()

        if response['meta']['status'] == 200 and len(response["response"]["hits"]) > 0:
            return (response["response"]["hits"][0]['result']['url'])
        else:
            return None

    @classmethod
    def scrap_song_url(self, url):
        song = requests.get(url)
        html = BeautifulSoup(song.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics

def main(args=None):
    spotify = SpotifyAPI()
    genius = GeniusAPI()
    print (genius.get_song_url(spotify.artist, spotify.song))
    # print (genius.scrap_song_url('https://genius.com/Drake-jungle-lyrics'))

if __name__ == "__main__":
    main()