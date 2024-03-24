#!/usr/bin/env python3
import os
import json
import requests

# colors
W  = '\033[0m'  # white (default)
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan

def checker():
    try:
        handle = input(P+' Enter a username to search:\n \n > '+W)
        with open('websites.json', 'r') as f:
            data = json.load(f)
            links = data['sites']

        weblinks = ["{}{}".format(i,handle) for i in links]

        for url in weblinks:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
            if r.status_code == 200:
                print(C+'Unavailable for: '+W+'' + url)
            else:
                print(P+'Available for:   '+W+'' + url)
        main()
    except KeyboardInterrupt:
        exit()

def banner():
    try:
        os.system('cls')
        raise ValueError('Error')
    except Exception:
        os.system('clear')
    print (C+'')
    print (P+' .--.--.-----.-----.----.-----.---.-.--------.-----. ')
    print (P+' |  |  |__ --|  -__|   _|     |  _  |        |  -__| ')
    print (P+' |_____|_____|_____|__| |__|__|___._|__|__|__|_____| ')
    print (P+'      .----|  |--.-----.----|  |--.-----.----.       ')
    print (P+'      |  __|     |  -__|  __|    <|  -__|   _|       ')
    print (P+'      |____|__|__|_____|____|__|__|_____|__|         ')
    print ('                                                       ')
    print (P+'               GitHub: ['+C+'xorsirenz'+P+']')
    print ('')

def main():
    checker()

banner()
main()
