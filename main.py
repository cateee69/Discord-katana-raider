import os
import random
from sys import prefix
import requests
import threading
import requests
import cookies

from itertools import cycle
from lxml.html import fromstring
import requests

import time
from token_fingering import get_fingerprint

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()
def get_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
def get_cookies():
    cookies.get_cookies()
while True:
    try:
        f = open("tokens ready.txt", "r")
        break
    except:
        print("\u001b[31m[-]Error no tokens folder\u001b[0m")
        f = open("tokens ready.txt", "a+")
        f.close()
        print("[+]Created Token Folder")
        time.sleep(1)
        clearConsole()
    
all = f.readlines()

inviteCode = input("Invite code ONLY CODE >")
message = input("message to spam if u dont want leave blank > ")
send = False
if message != "":
    channelid = input("chanel id > ")
    send = True

url = "https://discord.com/api/v9/invites/" + inviteCode
guild_name = requests.get(url).json()
guild_name = guild_name["guild"]["name"]
tokens_list = []
for tokens in all:
    tokens = tokens.strip()
    tokens_list.append(tokens)
def main(): #main loop
    global channelid
    global message
    global url
    global tokens_list

    for tokens in tokens_list:

        try:
            token = tokens
            cookies = get_cookies()
        except:
            print("Skipping empty tokens!")
            continue
        finger  = get_fingerprint()
        header = {
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-GB",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
            "authorization": token,
            "cookie": cookies,
            "x-fingerprint": finger
        }
        r = requests.post(url, headers=header)
        if r.status_code == 200:
            print(f"\u001b[32;1m[+] Joined {guild_name}\u001b[0m")
            headers = {           
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-GB",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "authorization": token,
                "cookie": cookies,
                "x-fingerprint": finger
            }
            if send:
                for i in range(10):
                    x = requests.post(f"https://discordapp.com/api/v9/channels/{channelid}/messages", headers=headers, json={'content': message})
                    if x.status_code == 200:
                        print(f"\u001b[32;1m[+] Succes sent message '{message}' to {guild_name}\u001b[0m")

        elif "rate limited." in r.text:
            print("[-] You are being rate limited.")
        else:
            print(f"\u001b[31m[-] Invalid Token.\u001b[0m")
            print(r.reason)
            print(r.text.replace("{", "").replace('"', '').replace(":", "").replace("}", ""))
        time.sleep(random.randint(1, 3))
main()
# working = []
# for _ in range(len(all)):
#     t1 = threading.Thread(target=main)
#     t1.start()
#     working.append(t1)
# for thread in working:
#     thread.join()
