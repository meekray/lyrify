"""Interacting with the Spotify and Genius APIs"""

from bs4 import BeautifulSoup
from flask import Flask
from pprint import pprint
from lyrify import CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN
import requests
import sys

class SpotifyAPI():
    def __init__(self):
        _ = 0

class GeniusAPI():
    api_base_url = 'https://api.genius.com/'
    headers = { 
        'Authorization': 'Bearer ' + CLIENT_ACCESS_TOKEN 
        }
    def __init__(self):
        _ = 0

    @classmethod
    def get_song_url(self, artist, song, album = None):
        query = artist + ' ' + song
        search_endpoint = self.api_base_url + 'search?q=' + query + '&access_token=' + CLIENT_ACCESS_TOKEN
        response = requests.get(search_endpoint)
        if response.json()['meta']['status'] == 200 and len(response.json()["response"]["hits"]) > 0:
            return (response.json()["response"]["hits"][0]['result']['url'])
        else:
            return None

    @classmethod
    def scrap_song_url(self, url):
        song = requests.get(url)
        html = BeautifulSoup(song.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics
        

def main(args=None):
    genius = GeniusAPI()
    print (genius.get_song_url("Kanye West", "Street lights"))
    # print (genius.scrap_song_url('https://genius.com/Drake-jungle-lyrics'))

if __name__ == "__main__":
    main()