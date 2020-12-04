import requests
import subprocess

from .errors import error_handler

class Client:
    def __init__(self, api_key, aid, application_secret):
        """
        API key can be found in the user settings
        AID can also be found in the user settings
        Application Secret can be easily found on the home page of https://auth.gg/
        """

        self.api_key = api_key
        self.aid = aid
        self.application_secret = application_secret

    def login(self, username: str, password: str):
        """
        Allow the user to login
        """

        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()        
        data = {
            "type": "login",
            "secret": self.application_secret,
            "apikey": self.api_key,
            "aid": self.aid,
            "username": username,
            "password": password,
            "hwid": hwid
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post("https://api.auth.gg/v1/", data=data, headers=headers)
        response = r.json()
        if response["result"] == "success":
            return True
        elif response["result"] == "invalid_details":
            raise error_handler.InvalidPassword()
        elif response["result"] == "invalid_hwid":
            raise error_handler.InvalidHWID()
        elif response["result"] == "time_expired":
            raise error_handler.SubscriptionExpired()
        elif response["result"] == "hwid_updated":
            return True
        else:
            raise error_handler.ErrorConnecting()

    def register(self, license_key: str, email:str, username: str, password: str):
        """
        Easily register users
        """

        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()         
        data = {
            "type": "register",
            "secret": self.application_secret,
            "apikey": self.api_key,
            "aid": self.aid,
            "username": username,
            "password": password,
            "hwid": hwid,
            "email": email,
            "license": license_key
        }       
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post("https://api.auth.gg/v1/", data=data, headers=headers)        
        response = r.json()["result"]
        if response == "success":
            return True
        elif response == "invalid_license":
            raise error_handler.InvalidLicense()
        elif response == "email_used":
            raise error_handler.UserError(message="email_used")
        elif response == "invalid_username":
            raise error_handler.UserError(message="invalid_username")               
        else:
            raise error_handler.ErrorConnecting()         

    def forgotPassword(self, username: str):
        """
        Sends a reset password email to the given user
        """

        data = {
            "type": "forgotpw",
            "secret": self.application_secret,
            "apikey": self.api_key,
            "aid": self.aid,
            "username": username
        }           
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post("https://api.auth.gg/v1/", data=data, headers=headers)        
        response = r.json()["result"]  
        info = r.json()["info"]      
        if response == "success":
            return True
        elif response == "failed":
            return f"{info}"
        else:
            raise error_handler.ErrorConnecting()

    def changePassword(self, username: str, password: str, newPassword: str):
        """
        Changes the password for that user.
        """

        data = {
            "type": "changepw",
            "secret": self.application_secret,
            "apikey": self.api_key,
            "aid": self.aid,
            "username": username,
            "password": password,
            "newpassword": newPassword
        }           
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post("https://api.auth.gg/v1/", data=data, headers=headers)       
        response = r.json()["response"]
        if response == "success":
            return True
        elif response == "invalid_details":
            raise error_handler.UserError(message="invalid_details")
        else:
            raise error_handler.ErrorConnecting()
