import requests
from colorama import Fore, init
from time import sleep, strftime
from datetime import datetime
from Consolly import consoler
console = consoler()

class NowPlaying:
    def __init__(self, bearer):
        self.token = bearer
        self.api = 'https://api.spotify.com/v1/me/player/currently-playing'
        self.last_song = ''
        self.last_artist = ''
        self.last_url = ''
        self.last_pause = False
        self.now = datetime.now()
    
    def time(self):
        return self.now.strftime('%H:%M:%S')

    def GetCurrentPlaying(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        data = requests.get(self.api, headers=headers)

        if data.status_code == 200: 
            song_name = data.json()['item']['name']
            artist_name = ', '.join([artist['name'] for artist in data.json()['item']['artists']])
            album_cover_url = data.json()['item']['album']['images'][0]['url']

            if album_cover_url is None or album_cover_url == '':
                album_cover_url = r'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Apple_Music_icon.svg/361px-Apple_Music_icon.svg.png'
            else:
                album_cover_url = album_cover_url

            self.last_artist = ', '.join([artist['name'] for artist in data.json()['item']['artists']])
            self.last_url = data.json()['item']['album']['images'][0]['url']
            self.last_song = data.json()['item']['name']

            if '"pausing" : true' in data.text:
                pause = True
            else:
                pause = False

            if self.last_song == song_name:
                pass
            else:
                print(f'{Fore.LIGHTGREEN_EX}{self.time()} {Fore.LIGHTGREEN_EX}| {song_name} by {artist_name}')

            return song_name, artist_name, album_cover_url, pause
        elif data.status_code == 429:
            song_name = self.last_song
            artist_name = self.last_artist
            album_cover_url = self.last_url
            pause = self.last_pause

            return song_name, artist_name, album_cover_url, pause
        elif '"message": "The access token expired"':
            return 'Expired'