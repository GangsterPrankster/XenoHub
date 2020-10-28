import urllib.request
import os
import pyfiglet
import shutil
ascii_banner = pyfiglet.figlet_format("Scraper")
print(ascii_banner)
url = "https://api.proxyscrape.com/?request=getproxies&proxytype="
output_file = "list.txt"
with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

print("Finished, check list.txt in folder.")

Clear = int(input("Press 1 to Continue or press Ctrl+C to quit: "))

if  Clear == 1:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    exec(open("main.py").read())
else: exit()
