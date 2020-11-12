import requests
import subprocess

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
            return "Invalid Details"
        elif response["result"] == "invalid_hwid":
            return "Invalid HWID"
        elif response["result"] == "time_expired":
            return "Subscription Expired"
        elif response["result"] == "hwid_updated":
            return "HWID Updated"
        else:
            return "Error contacting Auth.GG"

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
            return "Invalid license"
        elif response == "email_used":
            return "Email already used"
        elif response == "invalid_username":
            return "Invalid Or taken username"                                    
        else:
            return "Error Contacting Auth.GG"            

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
            return "Error Contacting Auth.GG"   

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
            return "Invalid credentials"
        else:
            return "Error Contacting Auth.GG"
