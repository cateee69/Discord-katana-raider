import requests
def get_cookies():

    session = requests.Session()
    res = session.get('https://discord.com').cookies
    for cookie in res:
        if cookie.name == "__dcfduid":
            Cookie_Dcfduid = cookie.value
        elif cookie.name == "__sdcfduid":
            Cookie_Sdcfduid = cookie.value
    return (
        f"__dcfduid={Cookie_Dcfduid}; __sdcfduid={Cookie_Sdcfduid}; "
        + "locale=us"
    )