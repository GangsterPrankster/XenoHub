print("╭━╮╭━╮╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╭╮")
print("╰╮╰╯╭╯╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱┃┃")
print("╱╰╮╭╯╭━━┳━╮╭━━┫╰━╯┣╮╭┫╰━╮")
print("╱╭╯╰╮┃┃━┫╭╮┫╭╮┃╭━╮┃┃┃┃╭╮┃")
print("╭╯╭╮╰┫┃━┫┃┃┃╰╯┃┃╱┃┃╰╯┃╰╯┃")
print("╰━╯╰━┻━━┻╯╰┻━━┻╯╱╰┻━━┻━━╯")
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
		exec(open("portscanner.py").read())
	else:
		if Options == 3:
			exec(open("proxy.py").read())
		else:
			if Options == 4:
				exec(open("gen.py").read())
			else:
				if Options == 5:
					exec(open("brute.py").read())

