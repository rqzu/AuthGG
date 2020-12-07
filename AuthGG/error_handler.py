class InvalidPassword(Exception):
    """Raised when the users password is incorrect"""
    def __init__(self):
        self.message = "The given password is incorrect!"
        super().__init__(self.message)

class InvalidLicense(Exception):
    """Raised when the provided license is invalid!"""
    def __init__(self):
        self.message = "The given license is invalid!"
        super().__init__(self.message)

class ErrorConnecting(Exception):
    """Raised when the connection to Auth.GG is unstable or offline"""
    def __init__(self):
        self.message = "We had problems connecting to Auth.GG!"
        super().__init__(self.message)        

class SubscriptionExpired(Exception):
    """Raised when a users subscription is expired"""
    def __init__(self):
        self.message = "Your subscription is expired!"
        super().__init__(self.message)

class InvalidHWID(Exception):
    """Raised when a users HWID is invalid"""
    def __init__(self):
        self.message = "Your HWID is not valid!"
        super().__init__(self.message)

class UserError(Exception):
    """Raised when a user has an error registering"""
    def __init__(self, message):
        if message == "email_used":
            self.message = "That email has been already used!"
        elif message == "invalid_username":
            self.message = "That username is already taken!"
        elif message == "invalid_details":
            self.message = "Your details are incorrect!"
        elif message == "failed":
            self.message = "Failed to complete that task!"
        else:
            pass

        super().__init__(self.message)     

class FailedTask(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
