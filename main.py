from math import radians
import os
import random
from sys import prefix
import requests
import threading
import requests
from itertools import cycle
from lxml.html import fromstring
import requests
import time
from token_fingering import get_fingerprint

# with love by Cloud ☆ﾟ.*･｡ﾟ#8294 Also thanks to V4NSH4J#1591 For helping me alot
os.system("title Katana by Cloud ☆ﾟ.*･｡ﾟ#8294")
inviteCode = ""
channelid = ""
message = ""
amount = ""
Join = False  # Dont Change Anything Here
Spam = False
fail = False
tokens_amount = 0
url = ""
proxy = ""


clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

clearConsole()

# main defs
def get_proxies():
    with open("proxies.txt", "r") as temp_file:
        proxies = [line.rstrip("\n") for line in temp_file]
    return proxies


def GetGuildName(inviteCode):
    global fail
    if not fail:
        url = "https://discord.com/api/v9/invites/" + inviteCode
        guild_name = requests.get(url).json()
        try:
            guild_name = guild_name["guild"]["name"]
            message = guild_name
        except:
            print(f"\u001b[31m[-] Failed To Resolve Invite.\u001b[0m")
            message = "Unknown Name"
            fail = True
            return message
        return message
    else:
        return "Unknown name"


def SendMessages(amount, proxy_pool, channelid, guild_name, message, headers):
    global proxy
    for i in range(amount - 1):
        try:
            x = requests.post(
                f"https://discordapp.com/api/v9/channels/{channelid}/messages",
                headers=headers,
                json={"content": message, "tts": "false"},
                proxies={"https://": "http://" + proxy},
            )
        except Exception as e:
            proxy = next(proxy_pool)
            print(f"\u001b[31m[-] Invalid Proxy.\u001b[0m" + str(e))
            continue
        if x.status_code == 200:
            print(
                f"\u001b[32;1m[+] Succes sent message '{message}' to {guild_name}\u001b[0m"
            )
            time.sleep(random.randint(3, 6) / 10)

        elif x.status_code == 429:
            print("\u001b[31m[-] You are being rate limited.\u001b[0m")
            time.sleep(3)
        else:
            print(f"\u001b[31m[-] Invalid Token.\u001b[0m" + str(e))


def JoinGuild(proxy_pool, guild_name, headers, url):
    while True:
        try:
            proxy = next(proxy_pool)
            r = requests.post(
                url, headers=headers, proxies={"https://": "http://" + proxy}
            )
            break
        except Exception as e:
            proxy = next(proxy_pool)
            print(f"\u001b[31m[-] Invalid Token.\u001b[0m" + str(e))
            continue
    if r.status_code == 200:
        print(f"\u001b[32;1m[+] Joined {guild_name}\u001b[0m")


# getting all tokens into list
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
tokens_amount = len(all)


tokens_list = []
for tokens in all:
    tokens = tokens.strip()
    tokens_list.append(tokens)


def main():  # main loop

    global channelid
    global message
    global url
    global tokens_list
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    for tokens in tokens_list:
        proxy = next(proxy_pool)
        tokens_list.remove(tokens)

        try:
            token = tokens

        except:
            print("Skipping empty tokens!")
            continue
        finger = get_fingerprint()
        headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            "x-fingerprint": finger,
        }

        if Join:
            guild_name = GetGuildName(inviteCode=inviteCode)
            JoinGuild(
                proxy_pool=proxy_pool, guild_name=guild_name, headers=headers, url=url
            )

        if Spam:
            guild_name = GetGuildName(inviteCode=inviteCode)
            SendMessages(
                amount=amount,
                proxy_pool=proxy_pool,
                channelid=channelid,
                guild_name=guild_name,
                message=message,
                headers=headers,
            )


def menu():
    global inviteCode, message, amount, channelid, Join, Spam, guild_name, url
    logo = f"""\u001b[95m
        ██╗  ██╗ █████╗ ████████╗ █████╗ ███╗   ██╗ █████╗ 
        ██║ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗
        █████╔╝ ███████║   ██║   ███████║██╔██╗ ██║███████║
        ██╔═██╗ ██╔══██║   ██║   ██╔══██║██║╚██╗██║██╔══██║
        ██║  ██╗██║  ██║   ██║   ██║  ██║██║ ╚████║██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                         Options  
                        \u001b[0m[\u001b[91m1\u001b[0m]\u001b[34m Raid   
                        \u001b[0m[\u001b[91m2\u001b[0m]\u001b[34m Raid + Spam   
                        \u001b[0m[\u001b[91m3\u001b[0m]\u001b[34m Spam        
"""

    while True:
        os.system(f"title Katana Detected {tokens_amount} tokens by Cloud ☆ﾟ.*･｡ﾟ#8294")
        clearConsole()
        print(logo + "\n")
        mainMenu = input("> \u001b[33m")
        if mainMenu == "1":
            Join = True
            Spam = False
            print("\u001b[95mInvite Code\u001b[0m")
            inviteCode = input("> \u001b[95m")
            guild_name = GetGuildName(inviteCode=inviteCode)
            os.system(
                f"title Katana Detected {tokens_amount} tokens Raiding {guild_name} by Cloud ☆ﾟ.*･｡ﾟ#8294"
            )
            url = "https://discord.com/api/v9/invites/" + inviteCode
        elif mainMenu == "2":
            Join = True
            Spam = True
            url = "https://discord.com/api/v9/invites/" + inviteCode
            print("\u001b[95mInvite Code\u001b[0m")
            inviteCode = input("> \u001b[95m")
            guild_name = GetGuildName(inviteCode=inviteCode)
            os.system(
                f"title Katana  Detected {tokens_amount} tokens  Raiding {guild_name}  by Cloud ☆ﾟ.*･｡ﾟ#8294"
            )

            print("\u001b[95mMessage\u001b[0m")
            message = input("> \u001b[95m")
            print("\u001b[95mChannel Id\u001b[0m")
            channelid = input("> \u001b[95m")
            print("\u001b[95mAmmount of messages\u001b[0m")
            while True:
                try:
                    amount = input("> \u001b[95m")
                    amount = int(amount)
                    break
                except:
                    print(f"\u001b[31m[-]Error {amount} is not an intiger\u001b[0m")
        elif mainMenu == "3":
            print("\u001b[41mRemember That: Tokens have to be on server\u001b[0m")
            time.sleep(1)
            Join = False
            Spam = True
            print("\u001b[95mMessage\u001b[0m")
            message = input("> \u001b[95m")
            print("\u001b[95mChannel Id\u001b[0m")
            channelid = input("> \u001b[95m")
            print("\u001b[95mAmmount of messages\u001b[0m")
            while True:
                try:
                    amount = input("> \u001b[95m")
                    amount = int(amount)
                    break
                except:
                    print(f"\u001b[31m[-]Error {amount} is not an intiger\u001b[0m")
        break
    print("\u001b[33mThreaded (y/n)?")
    ThreadMenu = input("> \u001b[33m").lower()
    working = []
    if ThreadMenu == "y":

        for _ in range(len(all) - 1):
            t1 = threading.Thread(target=main)
            time.sleep(random.randint(1, 2))
            t1.start()
            working.append(t1)
        for thread in working:
            thread.join()
    elif ThreadMenu == "n":
        main()


menu()
