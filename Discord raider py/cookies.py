import requests
def get_cookies():

    session = requests.Session()
    res = session.get('https://discord.com').cookies
    for cookie in res:
        if cookie.name == "__dcfduid":
            Cookie_Dcfduid = cookie.value
        if cookie.name == "__sdcfduid":
            Cookie_Sdcfduid = cookie.value
    Cookies = "__dcfduid=" + Cookie_Dcfduid + "; " + "__sdcfduid=" + Cookie_Sdcfduid + "; " + "locale=us"
    return Cookies