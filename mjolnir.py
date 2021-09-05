##############----START\LIBS------#######################
import tldextract
from googlesearch import search
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import socket
from socket import error as SocketError
from termcolor import colored
import os
import datetime
###############----proxy-banner----#######################
def proxyBanner():
   print(colored("PROXY SETUP",'green'))
###############----proxy-banner----#######################

###############----proxy-filter----#######################
def proxyfilter():  
 proxies = input(colored(">>> INPUT YOUR PROXY LIST: ", 'yellow')) 
 with open(proxies) as prox:
  while (proxie := prox.readline()):
   for proxie in prox:
      try:
         os.environ['http_proxy'] = 'http://' + proxie
         url = 'http://ipecho.net/plain'
         res = urlopen(url, timeout= 3)
         rtrn = res.read().decode('utf-8')
         print(colored(f"[Trying]",'yellow'),proxie)
         print(colored("[USED-IN-CHAIN>]",'green'), rtrn)
      except URLError as block:
         print(colored(">>DEAD PROXIE!!!",'red'),proxie)
      except SocketError as block:
         print(colored(">>DEAD PROXIE!!!",'red'),proxie)
###############----proxy-filter----#######################
    
##############----time------#######################
start = datetime.datetime.now()
##############----time------#######################

##############----COLORS/ANSI------#######################
os.system('color')
##############----COLORS/ANSI------#######################

##############-----BANNER--------#######################
def banner():
   print(colored("""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣾⠿⢛⡉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⡿⠛⢁⡞⡻⣽⣷⣦⣄⣀⠀⡤⠄⣀⠀⠀⠀⠈⠛⢿⣷⡀⠀⠀⠀
⠀⠀⣰⣿⠟⠀⠀⡮⡸⣱⣿⣿⣿⣿⣿⣿⣾⣵⣂⠍⡢⡀⠀⠀⠀⠻⣿⣆⠀⠀
⠀⣸⣿⠃⠀⠀⣜⡴⣱⣿⣿⣿⣿⣿⣿⡿⢛⣭⢹⣿⣶⣥⣄⡀⠀⠀⠘⣿⣧⠀
⢰⣿⡇⠀⠀⠸⣿⣳⣿⣿⣿⣿⡿⠟⠛⠁⠿⣿⢸⣿⣿⣿⣿⣿⣷⣦⣀⠸⣿⡆
⣼⣿⠀⠀⠀⠀⠀⠛⠿⣿⣿⣏⠲⢿⣿⠸⠗⣀⢻⣿⣿⣿⣿⣿⣿⣳⢻⠆⣿⣧
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⡿⢶⣶⣆⠻⣿⡆⣿⣿⣿⣿⣿⢳⢁⠎⠀⣿⣿
⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠢⠥⣊⣝⠻⢶⣤⣿⣿⣿⣿⢣⣇⠌⠀⠀⣿⡟
⠸⣿⣇⠀⠀⠀⠀⠀⠀⠀⡰⠓⠠⠄⣀⡌⠀⠀⠈⠉⠛⠿⢯⣿⡟⠀⠀⢸⣿⠇
⠀⢹⣿⣄⠀⠀⠀⠀⠀⠠⠓⠢⠤⣀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀
⠀⠀⠹⣿⣦⠀⠀⠀⠠⠑⠒⠤⢄⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠏⠀⠀
⠀⠀⠀⠈⠻⣷⣤⡠⣋⠒⠢⠤⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢿⣷⣭⣖⣒⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⡿⠟⠁MJOLNIR DORKER.⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⠿⣿⣿⣿⣿⠿⠿⠟⠋⠉V:1.0 by:SHEIDHEDA⠀⠀⠀⠀⠀⠀⠀⠀
             """, 'magenta'))
##############-----BANNER--------#######################

###############----dork-banner----#######################
def dorkBanner():
   print(colored("DORK SETUP",'green'))
###############----dork-banner----#######################

##############-----dorker--------#######################
def dorkie():
    CountryTarget = input(colored("INPUT COUNTRY TARGET(name): ",'yellow'))
    TLD = input(colored("INPUT COUNTRY TLD(if supported by google): ",'yellow'))
    LANGX = input(colored("INPUT COUNTRY LANGUAGE CODE (example 'fr'):  ",'yellow'))
    dorklist = input(colored(">>> INPUT YOUR DORKLIST: ", 'yellow')) 
    with open(dorklist) as fillox:
     while (query := fillox.readline().rstrip()):
        for url in search(query, tld=TLD, lang=LANGX, num=100, start=0, stop=None, pause=2.0, country=CountryTarget):
         print(colored(f"[*]", 'green') + url)
         with open("GENERATED-"+start.strftime("%Y-%m-%d %H.%M.%S")+"-.txt","a+") as filo:
          dns = tldextract.extract(url)
          filo.writelines(url+'\n')
          filo.close()
##############-----dorker--------#######################
##############----URL CHECKER AND Exception HANDLER------#######################
        try:    
          check = urlopen(url)
        except SocketError as block:
                   print(colored("[*] Server blocking us!/Could't reach the server!.", 'green'))
        except HTTPError as block:
                   print(colored("[*] HTTP ERROR", 'green'))
        except ValueError as block:
                  print(colored("[*] Value Error!!", 'green'))
        except socket.gaierror as block:
                  print(colored("[*] can't get address info!", 'green'))
##############----URL CHECKER AND Exception HANDLER------#######################
        else:
         url_list = []
         url_list.append(url)
banner() 
proxyBanner()         
proxyfilter()
dorkBanner()
dorkie()
##############----END------#######################
