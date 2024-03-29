import getpass
import os
from dotenv import dotenv_values
import configparser

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

input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 4" +" " +"*" * 20)

config = configparser.ConfigParser()
config.read('credentials.ini')
server_config = config['DEFAULT']
for item in server_config.items():
    print (item)
 
input("Press Enter to continue...")

print("*" * 20  + " "+  "Method 5" +" " +"*" * 20)
print ('Use HashiCorp Vault'+' '+ 'https://www.vaultproject.io')
print ('Other soultions are also using the same concept of vault')
print ('such as Ansible and pyATS')
print ('For Ansible Vault'+' '+ 'https://docs.ansible.com/ansible/2.8/user_guide/vault.html')
print ('For pyATS' +' '+ 'https://pubhub.devnetcloud.com/media/pyats/docs/utilities/secret_strings.html')
