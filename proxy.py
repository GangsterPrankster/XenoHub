import requests
import json


response = requests.get("https://ip.teoh.io/api/vpn/").content

data = json.loads(response)

print(data)

Clear = int(input("Press 1 to Continue or press Ctrl+C to quit: "))

if  clear == 1:
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')
	exec(open("main.py").read())
else: exit()
