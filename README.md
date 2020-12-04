# AuthGG Wrapper
# How to setup the client

## Official [Pypi Website](https://pypi.org/project/AuthGG/)

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

try:
	client.login(username, password)
	
	# clear console and redirect
except Exception as e:
	print(e)
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

try:
	client.register(email=email, username=username, password=password, license_key=license_key)

	# successfully registerd
except Exception as e:
	print(e)

```

## Forgot password example

This will send a simple email to the user to reset their password. If the user didn't request this password change, they can just ignore the email.

```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

username = input("Username: ")

try:
	client.forgotPassword(username)

	# successfully sent
except Exception as e:
	print(e)
```

## Change password example
This is an easier way for your customers to change their password if needed.

```py
from AuthGG.client import Client

client = Client(api_key="api_key", aid="aid", application_secret="secret")

username = input("Username: ")
password = input("Password: ")
newPassword = input("New Password: ")

try:
	client.changePassword(username=username, password=password, newPassword=newPassword)

	# successfully changed password
except Exception as e:
	print(e)

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

try:
	status = client.getUserCount()
	print(status)
except Exception as e:
	print(e)

```

## Delete users
Deletes users from the application
```py
from AuthGG.admin import AdminClient

client = AdminClient("authorization_key")

username = input("Username: ")

try:
	status = client.deleteUser(username)
	print(status)
except Exception as e:
	print(e)
```

# Contribute
## Bitcoin: 1GqmXGqvYfccZTg7dKVtMfD8GE3919segx
## CashApp: $razulol
