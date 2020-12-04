import requests

from .errors import error_handler

class AdminClient:
    def __init__(self, auth_key: str):
        """ 
        Requires a authorization key which can be found in the application settings
        """

        self.authorization = auth_key

    def deleteUser(self, username: str):
        """
        Deletes a user from your Auth.GG application
        """

        r = requests.get(f"https://developers.auth.gg/USERS/?type=delete&authorization={self.authorization}&user={username}")             
        if r.json()['status'] == "success":
            return True
        else:
            raise error_handler.FailedTask(message="Failed Deleting User!")

    def getUserCount(self):
        """
    
        """
        r = requests.get(f"https://developers.auth.gg/USERS/?type=count&authorization={self.authorization}")
        if r.json()['status'] == "success":
            jsonResponse = r.json()["value"]
            return True and jsonResponse
        else:
            raise error_handler.ErrorConnecting()

