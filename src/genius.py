from bs4 import BeautifulSoup
import requests

def genius():
    url = 'https://genius.com/Ed-sheeran-and-justin-bieber-i-dont-care-lyrics'

    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    print (bs.prettify())
    
if __name__ == "__main__":
    genius()