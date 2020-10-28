import socket
import _thread
import time
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network_speed="LAN"
    menu2=False
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            print ("Invalid URL or IP")
            exit(0)
        Core.ipurl=self.ipurl
        ascii_banner = pyfiglet.figlet_format("PortScanner")
        print(ascii_banner)
        while Core.menu1 is not True:
            choice = input("\n1 - simple \n2 - extended\n")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                print("You can only pick 1 and 2")
        while Core.menu2 is not True:
            choice = input("\n1 - LAN \n2 - Global Network\n")
            if choice == "1":
                Core.network_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.network_speed=0.3
                menu2 = True
                break
            else:
                print("You can only pick 1 and 2")

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res == 0:
                    tmp="Port",x,"is open", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(bcolors.OKGREEN,tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("Input Target IP or website\n"))
    print(bcolors.WARNING,"Range:",Core.mode,"\n Target:",Core.ipurl,"\n Scanning speed:",Core.network_speed,bcolors.ENDC)
    print(bcolors.BOLD,"Scanning...",bcolors.ENDC)
    for count in range(0,Core.mode):
        #print (Core.mode)
        time.sleep(Core.network_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)

    Clear = int(input("Press 1 to Continue or press Ctrl+C to quit: "))

if  Clear == 1:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    exec(open("main.py").read())
else: exit()
