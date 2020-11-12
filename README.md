# AuthGG Wrapper
# How to setup the client
```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")
```
## Logging in example
Allow users logging in and checking if their subscription is valid.
```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

username = input("Username: ")
password = input("Password: ")

status = client.login(username, password)

if status is True:
	# continue
else:
	print(status)
```

## Register a user example
Allows users to register and to begin their subscription.
```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

email = input("Email: ")
license_key = input("License: ")
username = input("Username: ")
password = input("Password: ")

status = client.register(email=email, username=username, password=password, license_key=license_key)

if status is True:
	# continue
else:
	print(status)
```

## Forgot password example

This will send a simple email to the user to reset their password. If the user didn't request this password change, they can just ignore the email.

```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

username = input("Username: ")

status = client.forgotPassword(username)

if status is True:
	# continue
else:
	print(status)
```

## Change password example
This is an easier way for your customers to change their password if needed.

```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

username = input("Username: ")
password = input("Password: ")
newPassword = input("New Password: ")

status = client.changePassword(username=username, password=password, newPassword=newPassword)

if status is True:
	# continue
else:
	print(status)
```


# Admin Client

This admin client makes it easier for "Administators" to manage their team
```py
from AuthGG.admin import AdminClient

client = AdminClient("authorization_key")
```


## Get user count

Returns the value of how many users are registered on your application

```py
from AuthGG.admin import AdminClient

client = AdminClient("authorization_key")

status = client.getUserCount()

if status is True:
	print(status) # Success
else:
	print(status) # Failed
```

## Delete users
Deletes users from the application
```py
from AuthGG.admin import AdminClient

client = AdminClient("authorization_key")

username = input("Username: ")

status = client.deleteUser(username)

if status is True:
	print(status) # Success
else:
	print(status) # Failed
```

# Contribute
## Bitcoin: 1GqmXGqvYfccZTg7dKVtMfD8GE3919segx
## CashApp: $razulol
