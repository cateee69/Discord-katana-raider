import requests
import time

def get_fingerprint():
    url = "https://discordapp.com/api/v9/experiments"
    header = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36"
        }
    fingerprint = requests.get(url, headers=header).json()["fingerprint"]
    return fingerprint

# time.sleep(0.01)
# f1 = open("tokens unready.txt", "a+")
# f1.close()
# f1 = open("tokens unready.txt", "r")
# lines = f1.readlines()
# f2 = open("tokens ready.txt", "a+")
# f2.write("\n")
# f2.close()
# for token in lines:
#     finger = get_fingerprint()
#     token = token.strip()
#     f2 = open("tokens ready.txt", "a+")
#     f2.write(f"{token}:{finger}\n")
#     f2.close()
#     print(f"\u001b[32;1m[+] token done \u001b[0m")

