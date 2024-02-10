import requests
from urllib.parse import urlencode
from datetime import datetime, timedelta
from Spotify.Credentials import Credentials

cd = Credentials()

class SpotifyAuth:
    def __init__(self) -> None:
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.access_token = None
        self.token_expiry = None
        self.refresh_token = None
    
    def OAuth(self):  
        auth_headers = {
            "client_id": cd.GetC()[0],
            "response_type": "code",
            "redirect_uri": "http://localhost:7777/callback",
            "scope": "user-read-currently-playing"
        }
        return "https://accounts.spotify.com/authorize?" + urlencode(auth_headers)