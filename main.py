import pyfiglet
ascii_banner = pyfiglet.figlet_format("XenoHub")
print(ascii_banner)
print("\033[1;32;40m $$$ Gangstar $$$  \n")
print('1 - Ip Tracker')
print('2 - Port Scanner')
print('3 - VPN Checker')
print('4 - Discord Nitro Code Generator')
print('5 - BruteForcer')
print('6 - Proxy Scraper')


Options = int(input("Option: "))
if Options == 1:
 	exec(open("iptracker.py").read())
else:
	if Options == 2:
		exec(open("port.py").read())
	else:
		if Options == 3:
			exec(open("proxy.py").read())
		else:
			if Options == 4:
				exec(open("gen.py").read())
			else:
				if Options == 5:
					exec(open("brute.py").read())
				else:
					if Options == 6:
						exec(open("scrape.py").read())
					else: print("That is not an option!")



