import requests
import json

IP = input("IP: ")

response = requests.get(f'http://ip-api.com/json/{IP}').content

data = json.loads(response)

print(data)

Clear = int(input("Press 1 to Continue or press Ctrl+C to quit: "))

if  Clear == 1:
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')
	exec(open("main.py").read())
else: exit()
