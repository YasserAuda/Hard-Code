import getpass
import os
from dotenv import dotenv_values

print("*" * 20  + " "+  "Method 1" +" " +"*" * 20)
username=str(input('Type Your Username:\n'))
password=getpass.getpass()

print("User Credential is" + " " + "Username is" + " " + username + " " +"Password is" +" " + password)

'''
another way

username=input('Type Your Username:\n')
password=getpass.getpass()

print(f "User Credential is : Username is {username} , Password is {password}")
'''

input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 2" +" " +"*" * 20)
username2 = str(os.environ.get('USER'))
password2 = str(os.environ.get('Password'))

print("User Credential is" + " " + "Username is" + " " + username2 + " " +"Password is" +" " + password2)

input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 3" +" " +"*" * 20)
user_Credential_from_envfile = dotenv_values(".env")
print(user_Credential_from_envfile)
