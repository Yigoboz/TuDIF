import time
import requests
import argparse
from colorama import Fore, Style


# Variables
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",required=True,help="Write target")
parser.add_argument("-w","--wordlist",required=True,help="Write Wordlist Path!")
data = parser.parse_args()
nwt = time.asctime()
wordlists = open(F"{data.wordlist}")
counter = 0
slash = "/"
http = "http://"
comb = data.target+slash


print(Fore.RED+"""

 ________          _______   ______  ________ 
/        |        /       \ /      |/        |
$$$$$$$$/__    __ $$$$$$$  |$$$$$$/ $$$$$$$$/ 
   $$ | /  |  /  |$$ |  $$ |  $$ |  $$ |__    
   $$ | $$ |  $$ |$$ |  $$ |  $$ |  $$    |   
   $$ | $$ |  $$ |$$ |  $$ |  $$ |  $$$$$/    
   $$ | $$ \__$$ |$$ |__$$ | _$$ |_ $$ |      
   $$ | $$    $$/ $$    $$/ / $$   |$$ |      
   $$/   $$$$$$/  $$$$$$$/  $$$$$$/ $$/       
                                              
            Turkish Directory Finder | https://github.com/yigoboz

"""+ Style.RESET_ALL)

# Check Online/Offline Status
def check():
    ch = requests.get(http+data.target)
    if ch.status_code == 200:
        print(F"{nwt} {Fore.GREEN} [+] Target Is Online!\n"+ Style.RESET_ALL)
    else:
        print(F"{nwt} {Fore.RED} [!] Target Is Offline!\n"+ Style.RESET_ALL)


print(F"{Fore.GREEN}Starting"+ Style.RESET_ALL + F" {nwt}")

check()

print(F"{Fore.CYAN} [+] Trying... \n"+ Style.RESET_ALL)


for i in wordlists:
    combine = http+comb+i
    r = requests.get(combine)
    if r.status_code == 200:
        print(F"{nwt} {Fore.GREEN} [+] Found ---> {combine}"+ Style.RESET_ALL)
        counter += 1
    elif r.status_code == 403:
        print(F"{nwt} {Fore.CYAN} [!] Permission Denied! ---> {combine}"+ Style.RESET_ALL)
        counter += 1

if counter == 0:
    print(F"{nwt} {Fore.RED} [!!] No Directory Found!"+ Style.RESET_ALL)


