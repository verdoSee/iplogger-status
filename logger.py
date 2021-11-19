import requests
from bs4 import BeautifulSoup
import os

payload = {
    'a': 'stat',
    'go': 'load',
    'id': 'What come after /logger/ in your url',   #Here
    'sort': 'date',
    'ord': 'desc',
}

payloadDrop = {
    'a': 'stat',
    'go': 'drop',
    'link': '6RiCP',
    'id': 'What come after /logger/ in your url',     #Here
    'type': 1
}

headers = {
    'Referer': 'Your URL',      #Here
    'Cookie': 'PHPSESSID=Your PHPSESSID'    #Here
}

toDrop = ''

while toDrop not in ('Y', 'n'):
    toDrop = input('Clear logs and fresh start? [Y/n]: ')
    if toDrop == 'Y':
        reqOld = requests.post('https://iplogger.org/ajax/', data=payloadDrop, headers=headers)
    elif toDrop == 'n':
        reqOld = ''

while True:     
    req = requests.post('https://iplogger.org/ajax/', data=payload, headers=headers)

    if reqOld != req.text:
        logs = []
        os.system('cls' if os.name == 'nt' else 'clear')
        soup = BeautifulSoup(req.text, 'html.parser')
        data = soup.find_all('div', {'class': 'statline'})
        for item in data:
            lo = {'log': item.find('div', title=None).text}
            logs.append(lo)
        for log in logs:
            flag = False
            for letter in log['log']:
                if letter.isalpha() and flag == False:
                    log['log'] = log['log'].replace(letter, ' '+letter)
                    flag = True
                elif letter == '<':
                    ip = log['log'][0 : log['log'].index('<')]

            print(ip)
    reqOld = req.text

        

        
