import json
import os
import random
import string

class Credentials:
    def __init__(self):
        pass

    def GetC(self):
        with open('Credentials.json') as f:
            data = json.load(f)
        
        client_id = data['client_id']
        secret = data['client_secret']
        
        return client_id, secret

    def GetLastToken(self):
        with open('Bearer/token.json') as f:
            data = json.load(f)
        
        token = data['token']
        ident = data['ident']
        refresh = data['re-token']
        
        return token, ident, refresh
    
    def ident_gen(length=6, parts=4):
        pattern = ''
        for _ in range(4):
            part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            pattern += part + '-'
        return pattern.rstrip('-')
    
    def FileNotExists(self, token, retoken):
        if not os.path.exists('Bearer'):
            os.mkdir('Bearer')

            with open('Bearer/token.json', 'w') as f:
                json.dump({"token": token, "ident": str(self.ident_gen()), "re-token": retoken}, f, indent=4)
    
    def RenewToken(self, token):
        with open('Bearer/token.json') as f:
            data = json.load(f)
        
        data['token'] = token

        with open('Bearer/token.json', 'w') as f:
            json.dump(data, f, indent=4)        