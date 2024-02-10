import requests, json, os
from Consolly import consoler
from colorama import Fore, init
from time import strftime, time, gmtime
from datetime import datetime
from flask import Flask, request, jsonify, redirect, render_template, url_for

from Spotify.SpotifyOAuth import SpotifyAuth
from Spotify.SpotifyNowPlaying import NowPlaying
from Spotify.Credentials import Credentials

bearer = Credentials()
spotify = SpotifyAuth()
console = consoler()
init()

class Main:
    def __init__(self) -> None:
        self.files = ['Credentials.json']
        self.content = {"grant_type": "authorization_code","redirect_uri": "http://localhost:7777/callback","client_id": "","client_secret": ""}
        self.status = '400'
        self.now = datetime.now()
        self.Checkfiles()
        self.GetFileContent()

    def Checkfiles(self):
        for i in self.files:
            if not os.path.exists(i):
                with open(i, 'w') as f:
                    json.dump(self.content, f, indent=4)
    
    def time(self):
        return self.now.strftime('%H:%M:%S')
    
    def GetFileContent(self):
        with open('Credentials.json', 'r') as f:
            content = json.load(f)
        
        if content['client_id'] is None or content['client_id'] == '':
            print(f'{Fore.RED}{self.time()} {Fore.LIGHTWHITE_EX}| ¡Error!, enter the CLIENT ID to continue | Error: CLIENT ID not found in Credentials.json')
            os.system('pause')
        else:
            if content['client_secret'] is None or content['client_secret'] == '':
                print(f'{Fore.RED}{self.time()} {Fore.LIGHTWHITE_EX}| ¡Error!, enter the CLIENT SECRET to continue | Error: CLIENT SECRET not found in Credentials.json')
                os.system('pause')
            else:
                pass
        
        return [content['client_id'], content['client_secret']]

mainer = Main()
data = mainer.GetFileContent()
app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'static'

@app.route('/playing')
def index():
    return render_template('index.html', token=bearer.GetLastToken()[0], selected_css='style#2.css')

@app.route('/get_song_info')
def play():
    try:
        play = NowPlaying(bearer=bearer.GetLastToken()[0])

        if 'Expired' in play.GetCurrentPlaying():
            refresh_url = 'https://accounts.spotify.com/api/token'
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            
            payload = {
                'grant_type': 'refresh_token',
                'refresh_token': bearer.GetLastToken()[2],
                'client_id': bearer.GetC()[0],
                'client_secret': bearer.GetC()[1]
            }

            response = requests.post(refresh_url, data=payload, headers=headers)
            token = response.json()['access_token']

            with open('Renewed.json', 'w') as f:
                json.dump(response.json(), f, indent=4)

            bearer.RenewToken(token=token)
        else:
            if play.GetCurrentPlaying()[3] == True:
                song_name = f'{play.GetCurrentPlaying()[0]} ~ (paused)'
            else:
                song_name = f'{play.GetCurrentPlaying()[0]}'
            return jsonify({'song_name': song_name, 'artist_name': play.GetCurrentPlaying()[1], 'album_cover_url': play.GetCurrentPlaying()[2]})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/')
def OAuthToken():
    return redirect(spotify.OAuth())

@app.route('/callback')
def AuthToken():
    global token_data
    code = request.args.get('code')

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:7777/callback',
        'client_id': bearer.GetC()[0],
        'client_secret': bearer.GetC()[1]
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    token_data = response.json()['access_token']
    
    bearer.FileNotExists(token=token_data, retoken=response.json()['refresh_token'])
    ident = bearer.GetLastToken()
    
    return redirect(f'/playing?i={ident[1]}')

app.run(port=7777, debug=True)