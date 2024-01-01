# while True:
#     try:
#         name = input('Enter the name of the file:')
#         fhead = open(name)
#         break
#     except:
#         print('The file', name, 'does not exist')
#         continue
    
# counts = dict()
# for line in fhead:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val  in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# lst = sorted([(v,k) for k,v in counts.items()])

# for val, key in lst[:10]:
#     print(key, val)

# import re

# hand = open('./myfiles/xfile.txt')
# for line in hand:
#     line = line.rstrip()
#     if(re.search('^[^\W]', line)):
#         print(line)

# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(re.search('^\S', x))
# print(y)


# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)

# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('@([^\s]*)', lin)
# print(y)

# import re

# hand = open('./myfiles/xfile.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum: ', max(numlist))

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# mysock.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode())

# while True:
#     data = mysock.recv(512)
#     if(len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# mysock.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode())

# console = {'log': print}

# while True:
#     data = mysock.recv(512)
#     if(len(data) < 1):
#         break
#     # console["log"](data.decode())
# mysock.close()

# print(dir([]))


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# count = dict()
# for line in fhand:
#     mystr = line.decode().strip()
#     for text in mystr:
#         count[text] = count.get(text, 0) + 1
# print(count)

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# while True:
#     url = input('Enter your url: ')

#     try:
#         html = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         break
#     except:
#         print("Cannot scrape ",url)
#         continue


# # Retrieve all of the anchor tags
# htmElem = input('Enter the html element:')
# tags = soup(htmElem)
# for tag in tags:
#     print(tag.get('href', None))


# import json
# data = '''{
#     "name": "Chuck",
#     "phone": {
#         "type": "intl",
#         "number": "+1 734 303 4456"
#     },
#     "email": {
#         "hide": "yes"
#     }
# }'''

# info = json.loads(data)
# print('Name: ', info["name"])
# print('Hide: ', info["email"]["hide"])
# myObj = {"hello": "come over here"}


# import urllib.request, urllib.parse, urllib.error
# import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# while True:
#     address = input('Enter location: ')
#     if (len(address) < 1): break
    
#     url = serviceurl + urllib.parse.urlencode({'address': address})
    
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
    
#     try:
#         js = json.loads(data)
#     except:
#         js = None
        
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure to Retrieve ====')
#         print(data)
#         continue
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)



# import urllib.request, urllib.parse, urllib.error
# import twurl
# import json

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# while True:
#     print('')
#     acct = input('Enter Twitter Account: ')
#     url = twurl.augment(TWITTER_URL, {'screen_name':acct,'count': '5' })
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())
#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     print(json.dumps(js, indent=4))
    
#     for u in js['users']:
#         print(u['screen_name'])
#         s = u['status']['text']
#         print(' ', s[:50])


# class PartyAnimal:
#     x = 0
    
#     def party(self):
#         self.x = self.x + 1
#         return self
    
#     def done(self):
#         print("Sof far", self.x)
    
# an = PartyAnimal()
# an.party().party().party().party().done()


# class Student:
    name:str
    age:int
    isStudent:bool
    
    def __init__(self:object, name:str, age:int, isStudent:bool) -> None:
        self.name = name
        self.age = age
        self.isStudent = isStudent
    
    def agefunc(self:object) -> object:
        self.age = self.age + 1
        return self
    
    def done(self) -> None:
        print('So far', self.age)
    
    def __del__(self:object) -> None:
        # print('Returned self in deconstructor', self.age)

# an = Student("Obed", 12, True)
# an.agefunc().agefunc().agefunc().agefunc()
# print('an contains', an)


class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam) -> None:
        self.name = nam
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)