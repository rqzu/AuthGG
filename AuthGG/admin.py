import requests

from AuthGG import error_handler

class AdminClient:
    def __init__(self, auth_key: str):
        """ 
        #### Requires a authorization key which can be found in the application settings
        """
        self.authorization = auth_key

    def fetchUserInfo(self, username: str):
        """ 
        ## Fetches information about the given user
        ```
        from AuthGG.admin import AdminClient
        
        client = AdminClient("authorization_key")
        
        username = input("Username: ")

        try:
            status = client.fetchUserInfo(username)
            print(status['email']) # prints out the email
        except Exception as e:
            print(e)            
        ```
        You can replace 'email' with the following options
        ### Available Options
        - username
        - email
        - rank
        - hwid
        - variable 
        - lastlogin
        - lastip
        - expiry
        """

        r = requests.get(f"https://developers.auth.gg/USERS/?type=fetch&authorization={self.authorization}&user={username}")             
        if r.json()['status'] == "success":
            information = {
                "username": r.json()['username'],
                "email": r.json()['email'],
                "rank": r.json()['rank'],
                "hwid": r.json()['hwid'],
                "variable": r.json()['variable'],
                "lastlogin": r.json()['lastlogin'],
                "lastip": r.json()['lastip'],
                "expiry": r.json()['expiry']
            }
            return information
        else:
            raise error_handler.FailedTask(message="Failed Fetching User Information!")

    def changeUserPassword(self, username: str, password: str):
        """
        ## Changes the provided users password 
        ```
        from AuthGG.admin import AdminClient

        client = AdminClient("authorization_key")

        try:
            client.changeUserPassword(username='razu', password='razu')        

            # continue
        except Exception as e:
            print(e)   
        ```
        """

        r = requests.get(f"https://developers.auth.gg/USERS/?type=changepw&authorization={self.authorization}&user={username}&password={password}")             
        if r.json()['status'] == "success":
            return True
        else:
            raise error_handler.FailedTask(message="Failed Changing Users Password!")

    def getHWID(self, username: str):
        """
        Grabs the users HWID
        ```
        from AuthGG.admin import AdminClient

        client = AdminClient("authorization_key")

        try:
            client.getHWID(username='razu')

            # continue
        except Exception as e:
            print(e)
        ```
        """

        r = requests.get(f"https://developers.auth.gg/HWID/?type=fetch&authorization={self.authorization}&user={username}")             
        if r.json()['status'] == "success":
            return r.json()['value']
        else:
            raise error_handler.FailedTask(message="Failed Grabbing Users HWID!")        

    def resetHWID(self, username: str):
        """
        ## Reset the provided users HWID
        ```
        from AuthGG.admin import AdminClient

        client = AdminClient("authorization_key")

        try:
            client.resetHWID(username='razu')        

            # continue
        except Exception as e:
            print(e)            
        ```
        """
        r = requests.get(f"https://developers.auth.gg/HWID/?type=reset&authorization={self.authorization}&user={username}")             
        if r.json()['status'] == "success":
            return True
        else:
            raise error_handler.FailedTask(message="Failed Resetting Users HWID!")        

    def deleteUser(self, username: str):
        """
        Deletes a user from your Auth.GG application
        ```
        from AuthGG.admin import AdminClient
        
        client = AdminClient("authorization_key")
        
        username = input("Username: ")

        try:
            status = client.deleteUser(username)
            
            # continue
        except Exception as e:
            print(e)        
        ```
        """

        r = requests.get(f"https://developers.auth.gg/USERS/?type=delete&authorization={self.authorization}&user={username}")             
        if r.json()['status'] == "success":
            return True
        else:
            raise error_handler.FailedTask(message="Failed Deleting User!")

    def getUserCount(self):
        """
        Get the user count of your application
        ```
        from AuthGG.admin import AdminClient

        client = AdminClient("authorization_key")

        try:
            status = client.getUserCount()
            print(status)
        except Exception as e:
            print(e)        
        ```
        """
        r = requests.get(f"https://developers.auth.gg/USERS/?type=count&authorization={self.authorization}")
        if r.json()['status'] == "success":
            jsonResponse = r.json()["value"]
            return jsonResponse
        else:
            raise error_handler.ErrorConnecting()

