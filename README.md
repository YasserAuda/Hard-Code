Hard coding your secrets in python or any programming language is something you should avoid.

What is your secrets ?
User credentials , API Keys , API Tocken or Cookies etc

You should always Soft coding it and there are many ways to do that , let me show you a few of them in the following script I created.

In this script you will see three options for soft coding your secrets.

Option 1 With help of using "Input" built-in function and  "getpass" python library we can allow the user to interactively type his credential.
"getpass" python library reads the input from the user as Password and not showing while not showing what charachters he is typing.

Code:
import getpass
username=str(input('Type Your Username:\n'))
password=getpass.getpass()

print("User Credential is" + " " + "Username is" + " " + username + " " +"Password is" +" " + password)

Option 2 you can save your username and password as Environment variables in windows then we call it using "os" python library.
 
Code:
import os
input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 2" +" " +"*" * 20)
username2 = str(os.environ.get('USER'))
password2 = str(os.environ.get('Password'))

print("User Credential is" + " " + "Username is" + " " + username2 + " " +"Password is" +" " + password2)

Option 3 you can save your username and password in a file then  call the  credential  using " Python-dotenv " python third party library.
Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.
https://pypi.org/project/python-dotenv/
You will need to install first using pip install Python-dotenv command
Code :
from dotenv import dotenv_values
input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 3" +" " +"*" * 20)
user_Credential_from_envfile = dotenv_values(".env")
print(user_Credential_from_envfile)

Script code aviable here in my github account:


