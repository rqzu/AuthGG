import requests
import socket

from AuthGG import error_handler

class Logging:
    def __init__(self, aid: str, apikey: str, secret: str):
        self.aid = aid
        self.apikey = apikey
        self.secret = secret


    def sendData(self, username: str, message: str):
        """ 
        Enable Custom Logs.
        ```
        from AuthGG.logging import Logging
        client = Loggging(aid='', apikey='', secret='')
        try:
            client.sendData(username='AuthGG', message='Deleted User')
        except:
            pass   
        ```
        """

        data = {
            "type": "log",
            "action": message,
            "pcuser": socket.gethostname(),
            "username": username,
            "aid": self.aid,
            "secret": self.secret,
            "apikey": self.apikey
        }
        r = requests.post(f"https://api.auth.gg/v1/", data=data)        
        response = r.json()
        if response['result'] == "success":
            return True
        else:
            raise error_handler.ErrorConnecting()
