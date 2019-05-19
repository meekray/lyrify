from flask import Flask, session, jsonify, send_from_directory, render_template, redirect, request, url_for
from uuid import uuid4
from flask_cors import CORS
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import sys
import json
from urllib.parse import quote

from lyrify.genius import Song
from lyrify.keys import *

app = Flask(__name__, static_folder='../build')

app.secret_key = APP_SECRET_KEY

REDIRECT_URI = 'http://localhost:7082/callback'
AUTHORITY = 'https://accounts.spotify.com/authorize?'

# CORS(app)

@app.route('/login', methods=['GET'])
def get_user_permission():
    print ('Requesting user permision...')
    query = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-currently-playing'
    }
    session['uuid'] = uuid4()
    session['access_token'] = "NO ACCESS TOKEN"
    endpoint = AUTHORITY + _query_build(query)
    print ('Redirecting...')
    return redirect(endpoint)

@app.route('/callback')
def get_access_token():
    if 'error' in  request.args:
        ERROR = true # DEFINE ERROR STATE
        exit(1)

    # User has auhtorized within scope
    AUTH_TOKEN = request.args['code']
    session['auth_token'] = AUTH_TOKEN
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(AUTH_TOKEN),
        "redirect_uri": REDIRECT_URI,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    }
    post_request = requests.post("https://accounts.spotify.com/api/token", data=code_payload)    

    response_data = json.loads(post_request.text)
    access_token = response_data['access_token']
    session['access_token'] = access_token
    return redirect("/")

@app.route('/current_lyrics')
def get_song_lyrics():    
    data = access_current_playing_song() #enabled multithreading
    song = Song(data)
    pprint (song.lyrics)
    return jsonify({'lyrics': song.lyrics})

@app.route('/')
def index():
    #pylint: disable=unused-argument
    return send_from_directory(app.static_folder, 'index.html')

def access_current_playing_song(): 
    ACCESS_TOKEN = session['access_token']

    if ACCESS_TOKEN == 'NO ACCESS TOKEN':
        return jsonify({"error": "There's been a server side error."})

    data = {}

    authorization_header = {"Authorization": "Bearer {}".format(ACCESS_TOKEN)}

    CURRENTLY_PLAYING_ENDPOINT = 'https://api.spotify.com/v1/me/player/currently-playing'

    current_song_response = requests.get(CURRENTLY_PLAYING_ENDPOINT, headers=authorization_header)
    
    if current_song_response.status_code == 200:
        current_song_data = json.loads(current_song_response.text) 
        data["song"] = current_song_data["item"]["name"]
        data["artist"] = current_song_data["item"]["artists"][0]["name"] # Get lead artist
        data["album"] = current_song_data["item"]["album"]["name"]
        # print (data["song"])
        return data

    elif current_song_response.status_code == 204:
        return jsonify({"error": "No song currently playing, or on private mode."})
  
    else:
        return jsonify({"error": "There's been a server side error."})

def _query_build(params):
    return "&".join(["{}={}".format(param, quote(value)) for param, value in params.items()])
