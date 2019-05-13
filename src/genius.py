from bs4 import BeautifulSoup
import requests

def scrap_song_url(url):
    song = requests.get(url)
    html = BeautifulSoup(song.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics
    
if __name__ == "__main__":
    print (scrap_song_url('https://genius.com/Drake-jungle-lyrics'))