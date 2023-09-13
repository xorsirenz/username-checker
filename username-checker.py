#!/usr/bin/env python3
import os
import yaml
import requests

# colors
W  = '\033[0m'  # white (default)
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
    

def checker():
    handle = input(C+' Type ['+P+'exit'+C+'] to close the program\n \n Enter a username to search:\n \n > '+W)
    if handle == 'exit':
        exit()
    else:
        with open('websites.yml') as f:
            data = yaml.safe_load(f)
            links = data['sites']

        weblinks = ["{}{}".format(i,handle) for i in links]

        for url in weblinks:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
            if r.status_code == 200:
                print(C+'Unavailable for: '+W+'' + url)
            else:
                print(P+'Available for:   '+W+'' + url)
        main()



def banner():
    try:
        os.system('cls')
        raise ValueError('Error')
    except Exception:
        os.system('clear')
    print (C+'')
    print (' .--.--.-----.-----.----.-----.---.-.--------.-----. ')
    print (' |  |  |__ --|  -__|   _|     |  _  |        |  -__| ')
    print (' |_____|_____|_____|__| |__|__|___._|__|__|__|_____| ')
    print ('                                                     ')                                                
    print ('            __               __                      ')
    print ('      .----|  |--.-----.----|  |--.-----.----.       ')    
    print ('      |  __|     |  -__|  __|    <|  -__|   _|       ')   
    print ('      |____|__|__|_____|____|__|__|_____|__|         ')     
    print ('                                                     ')
    print (C+'              '+C+' Created by: Madison')
    print (P+'               GitHub: ['+C+'x3-madison'+P+']')
    print ('')

def main():
    checker()

banner()
main()
