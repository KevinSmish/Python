#----------------------------------------------------------------------------------------------- 001_HelloWorld.py
# -*- coding: cp1251 -*-
import this		# Пасхальное яйцо Python

var = 'Hello, World!'
a,b,c=1,2,3

print()
print(var)
user = input('I am Python. What is your name? ')
print('Hello, ',user)

print('a=',a)
print('b=',b)
print('c=',c)

print(type(var))
print(dir(var))
#----------------------------------------------------------------------------------------------- 002_Types.py
MyDigitalNumberBin = 0b100101
MyDigitalNumberOct = 0o45
MyDigitalNumberHex = 0x25
MyDigitalNumberFromStr = int("37")

MyFloat = float("12.3")

print(MyDigitalNumberBin)
print(MyDigitalNumberOct)
print(MyDigitalNumberHex,'\n',MyDigitalNumberFromStr)

print(MyFloat)
print(10**100)
#----------------------------------------------------------------------------------------------- 003_Strings.py
MyStr1 = "One"
MyStr2 = 'Two'
MyStr3 = '''
Three'''

print(MyStr1+'\n'+MyStr2+MyStr3)

MyStr4 = "Hi "*4
print(MyStr4)

MyStr5 = "Папа у Васи силен в математике!"
LenMyStr5 = len(MyStr5)
print("Строка:",MyStr5)
print("Длина строки:",LenMyStr5)
print("Первый символ:",MyStr5[0])
print("Последний символ:",MyStr5[-1])
print("Первые 3 символа", MyStr5[:3])
print("Последние 3 символа", MyStr5[-3:])
print("Символы с 0 по 12 через 3:", MyStr5[0:12:3])
print("Перевернутая строка:",MyStr5[::-1])
print("Все слова с заглавной буквы:",MyStr5.title())
print("Заменим Васю на Петю:",MyStr5.replace('Васи','Пети'))

lst = MyStr5.split(" ")
print("Список слов строки:",lst)

print("Слово 'Васи' начинается с %d позиции"%MyStr5.find('Васи'))
print("Сочетание букв 'си' встречается %d раз",MyStr5.count('си'))
print("Слово 'победа' с заглавной буквы:","победа".capitalize())
print("Слово 'победа' заглавными буквами:","победа".upper())
print("Слово 'ПОБЕДА' строчными буквами:","ПОБЕДА".lower())
print("Слово ' победа  ' без пробелов:"," победа  ".strip())

# Старый стиль форматирования
print('Отформатированная строка: %2d, %10.4f, %-10s'%(5,7.03,'string'))
# Новый стиль форматирования
print('Отформатированная строка: {0:2d}, {1:10.4f}, {2:>10s}'.format(5,7.03,'string'))
print('Отформатированная строка: {n:2d}, {m:10.4f}, {k:>10s}'.format(m=7.03,k='string',n=5))
#----------------------------------------------------------------------------------------------- 004_List.py
user = ['Top','Left','Bottom','Right']

print(user[0][1])                       # второй символ первого элемента
print(user[-1])                         # последний элемент
user.append('None')
print(user[-1])                         # последний элемент

user.insert(2,'After Left')
print(user)

user1 = ['None','None','None']
user.extend(user1)
print(user)
print('counts of None=',user.count('None'))				# Кол-во вхождений элемента в список
print('Length of User:',len(user))

user.remove('None')
print('Remove first None:',user)

print(user.pop(5))						# Удалить i-тый элемент и вернуть его
print(user)

user.sort()
print('Sort:',user)

user.reverse()
print('Reverse:',user)

del user[4:6]
print('Del 4,5:',user)

lst1 = ['One','Two','Three']
print("Список lst1=",lst1)
print("Элемент 'Three' находится на %d позиции"%lst1.index('Three'))
print("Есть ли элемент 'Three' в списке:",'Three' in lst1)
print("Есть ли элемент 'Four' в списке:",'Four' in lst1)
print("Преобразуем список в строку:", ", ".join(lst1))
#----------------------------------------------------------------------------------------------- 005_Tuple.py
c_tuple = ['Red','White','Black','Blue']
a,b,c,d=c_tuple
print(b)
one_tuple = 1,
#----------------------------------------------------------------------------------------------- 006_Set.py
set1 = {'Red','White','Black','Blue'}
print(len(set1))
print(type(set1))
#
set1.add('Green')
print(len(set1))
#
print('Green' in set1)
#----------------------------------------------------------------------------------------------- 007_if.py
# if - вариант 1
a=2
b=3
c=a if (a<b) else b
print(c)

nm = 7*2
print(nm, ' - число','четное' if (nm %2 == 0) else 'нечетное')

# if - вариант 2
num = int(input('Input a number:'))
if num > 5:
	print('>5')
elif num < 5:
	print('<5')
else:
	print('is 5')
#----------------------------------------------------------------------------------------------- 008_while.py
j = 1
while j<4:
	print(j)
	j+=1
print('End of part one')
# ----------------------
lst = [1,2,3,5,7,9]
pos = 0
while pos < len(lst):
	num = lst[pos]
	pos +=1
	if num==1:
		continue
	elif num == 0:
		break
	print("1/%d=%f"%(num,1/num))
else:
	print("На 0 делить не пытались :)")
#----------------------------------------------------------------------------------------------- 009_for.py
chars = ('A','B','C')
fruit = {'Apple', 'Banana', 'Cherry'}
dict = {'Имя':'Иван','Отчество':'Иванович','Фамилия':'Иванов'}
#print(dict['Имя'])
#---------------------------
for item in zip(chars,fruit):
	print(item)
#---------------------------
for key, value in dict.items():
	if key=='Отчество':
		continue
	print(key,'=',value)
#---------------------------
lst = [1,2,3,5,7,9]
for num in lst:
	if num==1:
		continue
	elif num == 0:
		break
	print("1/%d=%f"%(num,1/num))
else:
	print("На 0 делить не пытались :)")
#----------------------------------------------------------------------------------------------- 010_Strings.py
var=' привет, люди! '
print(var.title())
print(var.upper())
print(var.lower())
print(var.rstrip())
print(var.lstrip())
print(var.strip())
#----------------------------------------------------------------------------------------------- 011_function.py
# -*- coding: cp1251 -*-

def MyFunc(*args, **kwargs):
	print( args )
	print( kwargs )

Delegate= MyFunc(1, 2, 3, name="Mike", job="programmer")
Delegate # Вызов функции!

# Результат:
# (1, 2, 3)
# {'job': 'programmer', 'name': 'Mike'}
#----------------------------------------------------------------------------------------------- 012_dict.py
dict = {
	'Иван':'инженер',
	'Петр':'старший инженер',
	'Сергей':'главный инженер',
	'Андрей':'начальник'
		}

MyKey1 = "Иван"
print(MyKey1,":",dict[MyKey1])

MyKey2 = "Михаил" # Отсутствует в словаре, следующая строка вызовет исключение KeyError
# print(MyKey2,":",dict[MyKey2]) 
print(MyKey2,":",dict.get(MyKey2)) # None
print(MyKey2,":",dict.setdefault(MyKey2,"студент-практикант")) # None


print("перебор элементов:")
for name, dolg in dict.items():
	print(name,' - ',dolg)

print("\nперебор ключей:")
for name in dict.keys():
	print(name,' - ',dict[name])

print("\nперебор отсортированных ключей:")
for name in sorted(dict.keys()):
	print(name,' - ',dict[name])
#----------------------------------------------------------------------------------------------- 014_random.py
from random import random, sample

var = int(random()*10)
print(var)

var=sample(range(10),3) # 3 числа в диапазоне от 0 до 9
print(var)

var=sample(range(1,10),4) # 4 числа в диапазоне от 1 до 10
print(var)
#----------------------------------------------------------------------------------------------- 015_urllib_test.py
import urllib.request

counts = dict()
fhand = urllib.request.urlopen('http://py4inf.com/code/romeo.txt')
for line in fhand:
	print(line)
	words = line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
for count in counts:
	print(count, counts[count])
#----------------------------------------------------------------------------------------------- 016_urllib_and_regexp_test.py
import urllib.request
import re

fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand:
	print(line)
	match = re.findall('href="(http://\S*)',line.decode())
	if len(match)>0:
		print("!!!")
		print(match)
		print('\n')
#----------------------------------------------------------------------------------------------- 018 sqlite.py
import sqlite3
conn=sqlite3.connect('music.db')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Thunderstruck',20))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('My Way',15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title,plays FROM Tracks')
for row in cur:
	print(row)

cur.execute('DELETE FROM Tracks WHERE plays<20')
conn.commit()

print('Tracks after:')
cur.execute('SELECT title,plays FROM Tracks')
for row in cur:
	print(row)

conn.close()
#----------------------------------------------------------------------------------------------- 019 directory test.py
import os
cwd=os.getcwd() #current working directory
print('Current path:' + cwd)
cwd=os.path.relpath(cwd,"E:\\KVN\\!CODE\\FreeBasic")
print('Rel path:' + cwd)
cwd=os.path.abspath(cwd)
print('Abs path: ' + cwd)

print()
print(os.listdir(cwd))
print()

cwd='E:\\KVN\\!CODE\\PYTHON'
print('File: ' + cwd)
print('DirName: ' + os.path.dirname(cwd))
print('FileName: ' + os.path.basename(cwd))
print(cwd.split(os.path.sep))
print('Size: ' + str(os.path.getsize(cwd)))

print()
print('cover.jpg exists? ' + str(os.path.exists('cover.jpg')))
print('music.db is file? ' + str(os.path.isfile('music.db')))
print('music.db is dir? ' + str(os.path.isdir('music.db')))
print('__pycache__ is dir? ' + str(os.path.isdir('__pycache__')))

print('======================')
for (dirname,dirs,files) in os.walk('.'):
	for filename in files:
		if filename.startswith('00') and filename.endswith('.py'):
			thefile = os.path.join(dirname,filename)
			print(os.path.getsize(thefile), " -> ", thefile)

#os.makedirs('D:\\Python\\!MY_PROG\TEST')
#----------------------------------------------------------------------------------------------- 020 hashlib test.py
import hashlib

fhand=open('music.db','r')
data=fhand.read()
data=bytes(data,"UTF-8")
fhand.close()
checksum=hashlib.md5(data).hexdigest()
print(checksum)
#----------------------------------------------------------------------------------------------- 021 file.py
helloFile = open('E:\\KVN\\!CODE\\PYTHON\\!0.bat')
content=helloFile.read()
helloFile.close()
print(content)

helloFile = open('E:\\KVN\\!CODE\\PYTHON\\!0.bat')
print(helloFile.readlines())
helloFile.close()

helloFile=open('E:\\KVN\\!CODE\\PYTHON\\README.txt','w')
helloFile.write('Некогда читать инструкции!\n')
helloFile.close()

helloFile=open('E:\\KVN\\!CODE\\PYTHON\\README.txt','a')
helloFile.write('Так что не теряйте времени!\n')
helloFile.close()

for arr in range(3):
	KeyFile = open('E:\\KVN\\!CODE\\PYTHON\\test%s.txt' % (arr+1),'w')
	KeyFile.write('test %s' % (arr+1))
	KeyFile.close()
#----------------------------------------------------------------------------------------------- 022 shelve.py
import shelve

shelfFile = shelve.open('mydata')
cats=['Васька','Мурка','Алиса']
shelfFile['cats']=cats
shelfFile.close

cats=1

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(list(shelfFile.keys())) #cats
print(list(shelfFile.values())) #['Васька','Мурка','Алиса']
cats=shelfFile['cats']
shelfFile.close

print(cats)
#----------------------------------------------------------------------------------------------- 023_YandexTranslate-GET.py
import requests

KEY = "trnsl.1.1.2017"
TITLE = "«Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru/"
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def TranslateMe(myText):
    params = {
        'key' : KEY,
        'text' : myText,
        'lang' : 'ru-en'
    }
    response = requests.get(URL,params=params);
    return response.json();

json = TranslateMe('Не было у бабы забот, купила баба порося');
print(json['text'][0]);
print(TITLE);
#----------------------------------------------------------------------------------------------- 023_YandexTranslate-POST.py
import requests
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.2017'
text = 'Я ХОЧУ НАУЧИТЬСЯ ПЕРЕВОДИТЬ ТЕКСТЫ НА АНГЛИЙСКИЙ ЯЗЫК'
lang = 'ru-en'
r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
# Выводим результат
print(r.json()['text'][0])
#----------------------------------------------------------------------------------------------- 025_TestWhile.py
s="Привет, мир!"

while s!="":
    print(s)
    s=s[1:-1]
#----------------------------------------------------------------------------------------------- 026_TestFileOpen.py
f=open("file.txt","r")
while 1:
    l=f.readline()
    if not l:
        break
    if len(l) > 5:
        print(l)
f.close()
#----------------------------------------------------------------------------------------------- 027_TestFor.py
for i in range(1,10):
    for j in range(1,10):
        print("%2i"%(i*j),end=",")
    print()
#----------------------------------------------------------------------------------------------- 028_TestFunction.py
def cena(rub,kop=0):
    return "%i руб. %i коп." %(rub,kop)

print(cena(8,20))
print (cena(2))
print(cena(kop=3,rub=2))

print()
print(2**1000)
print()

u2=u"Еще пример"
print(u2)
#----------------------------------------------------------------------------------------------- 029_TestSwap.py
a=1
b=2
print(a,b)
a,b=b,a
print(a,b)
#----------------------------------------------------------------------------------------------- 030_TestList.py
lst2=[x**2 for x in range(10) if x%2==1] # квадрат нечетных чисел от 0 до 10
lst3=list("abcd")                        # [a,b,c,d]
print(lst2)
print(lst3)
                                         
lst3.pop(2)                              # [a,b,d]
lst3.insert(2,7)                         # [a,b,7,d]
print(lst3)

print()

s=range(10)                              # [0,1,2,3,4,5,6,7,8,9]
t=s[::3]                                 # item[START:STOP:STEP] t=[0,3,6,9]

for i in t:
	print(">>",i)                    # print(*t)

for i in s:
    print(s[i],end=", ")                 # [0,1,2,3,4,5,6,7,8,9]

print()
print(t[3])                              # 9
#----------------------------------------------------------------------------------------------- 031_TestAny.py
lst=['я','не','готов','к','тестированию']
s1=[x for x in lst if x!='не']               # ['я','готов','к','тестированию']
print(*s1)                                   # я готов к тестированию
#----------------------------------------------------------------------------------------------- 032_Lambda.py
def fun(x):                      # Замыкание — это функция python, которая ссылается 
    def zam(z):                  # на свободные переменные в лексическом контексте.
        return x+z               # захват 'x' из внешнего контекста
    return zam

zam = fun(10)
print(zam(5))                    # fun(10):zam(5):10+5=15 

spisok = [1,4,11,2,24,-3,5,15]   # filter() — (функция, последовательность) — возвращает последовательность, 
t = filter(lambda x: x<5, spisok)# состоящую из тех элементов последовательности, для которых функция является истинной.
print(*t)                        # [1, 4, 2, -3]


spisok1 = [2,6,7,0]              # map() — (функция, последовательность) — совершает вызов функция (элемент)
listik1 = [2,5,3,9]              # с каждым элементом последовательности и возвращает список из возвращавшихся функцией значений.
t=map (lambda x,y: x*y, spisok1, listik1) # Перемножим между собой два списка:
print(*t)                        # [4, 30, 21, 0]

from functools import reduce

posled = [2,3,4,5,6,7]           # reduce() — (функция, последовательность) — возвращает единственное значение,
t=reduce(lambda res,x: res*x, posled) #  собранное из результатов вызовов двухаргументной функции с первыми двумя 
                                 # элементами последовательности; затем с полученным результатом и последующим элементом.
print(t)			 # 5040
				 # Последовательность вычислений: (((((1*2)*3)*4)*5)*6)*7
#----------------------------------------------------------------------------------------------- 033 Class.py
# -*- coding: cp1251 -*-

class Person:
	def __init__(self,name):
		# pass
		self.__name = name
	def GetName(self):
		return self.__name
	def Exclaim(self):
		print("I'm a Person")
	def get_prof(self):
		print("Call get_prof")
		return self.prof
	def set_prof(self, prof):
		print("Call set_prof")
		self.prof = prof
	profession = property(get_prof,set_prof)

class Manager(Person):
	def Exclaim(self):
		print("I'm a Manager")
		super().Exclaim()
	#------------------------------------------------
	@classmethod
	def MyClassMethod(cls):
		print("MyClassMethod - Это метод класса")
	#------------------------------------------------
	@staticmethod
	def MyStaticMethod():
		print("MyStaticMethod - Это статический метод. Он не зависит от класса")


hunter = Manager('Elmer Fudd')
print(hunter.GetName())
hunter.Exclaim()
print("-----------------")
print("To Person:")
Person(hunter).Exclaim()
print("-----------------")
hunter.profession = "CEO"
print(hunter.profession)
hunter.MyClassMethod()
hunter.MyStaticMethod()
#----------------------------------------------------------------------------------------------- 034 RegEx.py
# -*- coding: cp1251 -*-

import re

source = 'папа у Васи силен в математике, учится папа за Васю весь год.'
#pattern = 'папа'
#result = re.match(pattern,source)
pattern = re.compile('папа')
result = pattern.match(source)
if result:
	print(result.group())
#----------------------------------------------------------------------------------------------- 035 ConfigParser.ini
[english]
greeting = Hello
[french]
greeting = Bonjour
[files]
home=E:\KVN\!CODE\PYTHON
# Interpolation
verify=%(home)s\VERIFY
#----------------------------------------------------------------------------------------------- 035 ConfigParser.py
# -*- coding: cp1251 -*-

import configparser

cfg = configparser.ConfigParser()
cfg.read("035 ConfigParser.ini");

print(*cfg)
print("[french]=",cfg['french'])
print("[french]=",cfg['french']['greeting'])
print("[files][home]=",cfg['files']['home'])
print("[files][verify]=",cfg['files']['verify'])
#----------------------------------------------------------------------------------------------- 036 Processes.py
import os
import subprocess

print('pid process           : {0:d}'.format(os.getpid()))	#pid process
print('Current work directory: {0}'.format(os.getcwd()))	# current work directory

print('Date:',subprocess.getoutput("date /T"))			# getoutput - процесс возвращает string
print('Date:',subprocess.getstatusoutput("date /T"))		# getstatusoutput - кортеж код статуса и результат
#----------------------------------------------------------------------------------------------- 037 SocketsClient_UDP.py
from datetime import datetime
import socket

server_address=('localhost',6789)
max_size=4096
print('Starting client at',datetime.now())
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP - socket.SOCK_DGRAM
client.sendto(b'Hey!',server_address)
data,server = client.recvfrom(max_size)
print('At',datetime.now(),server,' said ',data)
client.close()
#----------------------------------------------------------------------------------------------- 037 SocketsServer_UDP.py
from datetime import datetime
import socket

server_address=('localhost',6789)
max_size=4096
print('Starting server at',datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP - socket.SOCK_DGRAM
server.bind(server_address)
data,client = server.recvfrom(max_size)
print('At',datetime.now(),client,' said ',data)
server.sendto(b'Are you talking to me?',client)
server.close()
#----------------------------------------------------------------------------------------------- 038 SocketsClient_FTP.py
from datetime import datetime
import socket

server_address=('localhost',6789)
max_size=1000
print('Starting client at',datetime.now())
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # For FTP - socket.SOCK_STREAM
client.connect(server_address)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At',datetime.now(), 'someone replied ',data)
client.close()
#----------------------------------------------------------------------------------------------- 038 SocketsServer_FTP.py
from datetime import datetime
import socket

server_address=('localhost',6789)
max_size=1000
print('Starting server at',datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # For FTP - socket.SOCK_STREAM
server.bind(server_address)
server.listen(5)
client,addr = server.accept()
data = client.recv(max_size)
print('At',datetime.now(),client,' said ',data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()
#----------------------------------------------------------------------------------------------- 039_TestRPC_Client.py
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
num = 7
result = proxy.double(num)
print("Double %s is %s"%(num,result))
#----------------------------------------------------------------------------------------------- 039_TestRPC_Server.py
from xmlrpc.server import SimpleXMLRPCServer

def double(num):
	return num*2

server=SimpleXMLRPCServer(("localhost",6789))
server.register_function(double,"double")
server.serve_forever()
#----------------------------------------------------------------------------------------------- 039 TestPylint.py
# -*- coding: cp1251 -*-
''' Тестирование функции reduce '''

from functools import reduce

sm = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(sm)			# Сумма
# pylint.exe 040_TestPylint.py >0
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- Замыкание
def fun(x):                      # Замыкание — это функция python, которая ссылается 
    def zam(z):                  # на свободные переменные в лексическом контексте.
        return x+z               # захват 'x' из внешнего контекста
    return zam

zam = fun(10)
print(zam(5))                    # fun(10):zam(5):10+5=15 
#----------------------------------------------------------------------------------------------- filter()
spisok = [1,4,11,2,24,-3,5,15]   # filter() — (функция, последовательность) — возвращает последовательность, 
t = filter(lambda x: x<5, spisok)# состоящую из тех элементов последовательности, для которых функция является истинной.
print(*t)                        # [1, 4, 2, -3]
#----------------------------------------------------------------------------------------------- map()
spisok1 = [2,6,7,0]              # map() — (функция, последовательность) — совершает вызов функция (элемент)
listik1 = [2,5,3,9]              # с каждым элементом последовательности и возвращает список из возвращавшихся функцией значений.
t=map (lambda x,y: x*y, spisok1, listik1) # Перемножим между собой два списка:
print(*t)                        # [4, 30, 21, 0]
#----------------------------------------------------------------------------------------------- resuce()
posled = [2,3,4,5,6,7]           # reduce() — (функция, последовательность) — возвращает единственное значение,
t=reduce(lambda res,x: res*x, posled) #  собранное из результатов вызовов двухаргументной функции с первыми двумя 
                                 # элементами последовательности; затем с полученным результатом и последующим элементом.
print(t)			 # 5040
				 # Последовательность вычислений: (((((1*2)*3)*4)*5)*6)*7
#----------------------------------------------------------------------------------------------- 170528 TranslateYandex.py
import requests

KEY = "trnsl.............................."
TITLE = "«Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru/"
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def TranslateMe(myText):
    params = {
        'key' : KEY,
        'text' : myText,
        'lang' : 'ru-en'
    }
    response = requests.get(URL,params=params);
    return response.json();

json = TranslateMe('Не было у бабы забот, купила баба порося');
print(json['text'][0]);
print(TITLE);
#----------------------------------------------------------------------------------------------- 170530 PyCharmTest.py
from collections import OrderedDict

d = OrderedDict([
    ('one',1),
    ('two',2),
    ('three',3)])

print(d.keys())
#----------------------------------------------------------------------------------------------- 170610 FunctionalProg.py
name_lengths = map(len, ['Маша', 'Петя', 'Оля']) 	# Простой map, принимающий список имён и возвращающий список длин:
print(*name_lengths)					# => [4, 4, 3]

# --------------------------------------------------------------------------------------
squares = map(lambda x: x * x, [0, 1, 2, 3, 4]) 	# Этот map возводит в квадрат каждый элемент:
print(*squares)						# => [0, 1, 4, 9, 16]

# --------------------------------------------------------------------------------------
import random

names = ['Маша', 'Петя', 'Вася']
secret_names = map(lambda x: random.choice(['Шпунтик', 'Винтик', 'Фунтик']), names)
print(*secret_names)					
# Алгоритм может присвоить одинаковые прозвища разным секретным агентам. 
# Будем надеяться, что это не послужит источником проблем во время секретной миссии.
# --------------------------------------------------------------------------------------
import random

names = ['Маша', 'Петя', 'Вася']
secret_names = map(hash, names)
print(*secret_names)
# --------------------------------------------------------------------------------------
from functools import reduce

#Reduce принимает функцию и набор пунктов. Возвращает значение, получаемое комбинированием всех пунктов.
sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4]) 	# Пример простого reduce. Возвращает сумму всех пунктов в наборе:
print(sum)						# => 10					
# --------------------------------------------------------------------------------------
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = reduce(lambda a, x: a + x.count('капитан'),
                   sentences,
                   0)
print(" Cлово капитан встречается " + str(cap_count) + " раза")
# --------------------------------------------------------------------------------------
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
zolushka = list(filter(lambda x: x == 'мак', mixed))

print (zolushka)					# ['мак', 'мак', 'мак', 'мак', 'мак']
# --------------------------------------------------------------------------------------
# Вычисление наибольшего элемента в списке при помощи reduce:
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a,b: a if (a > b) else b, items)
 
print (all_max)						# 32
# --------------------------------------------------------------------------------------
people = [{'имя': 'Маша', 'рост': 160},
    {'рост': 'Саша', 'рост': 80},
    {'name': 'Паша'}]

heights = list(map(lambda x: x['рост'],
              filter(lambda x: 'рост' in x, people)))

if len(heights) > 0:
    from operator import add
    average_height = reduce(add, heights) / len(heights)
print("Средний рост:"+str(average_height))
ok=input("Ok?")
# --------------------------------------------------------------------------------------
from random import random

def move_cars(car_positions):
    return list(map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions))

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print(state['time'])
    print('\n'.join(list(map(output_car, state['car_positions']))))

def race(state):
	draw(state)
	if state['time']>0:
        	race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})
#----------------------------------------------------------------------------------------------- 170610 generator expressions.py
f = (x for x in range(10)) 		# выражение - генератор
c = [x for x in range(10)] 		# генератор списков

print(*c)
print(list(f))
# --------------------------------------------------------------------------------------
def prime(lst):
    for i in lst:
        if i % 2 == 0:
            yield i

f = prime([1,2,3,4,5,6,7])
print(list(f)) 				# [2, 4, 6]
# --------------------------------------------------------------------------------------
def generator_range(first, last):
    yield from range(first, last)

print(list(generator_range(2, 4)))
#----------------------------------------------------------------------------------------------- 170610 generators.py
def Fib(N):
	a, b = 0, 1
	for i in range(N):
		yield a
		a, b = b, a + b

for i in Fib(100):
	print(i,' ',end='')
#----------------------------------------------------------------------------------------------- 170610 iterators.py
it1 = iter([1, 2, 3, 4, 5])


def forit(mystate=[]):
	if len(mystate) < 3:
		mystate.append('.')
		return "."
	else:
		return None


it2 = iter(forit, None)
print([x for x in it1])
print([x for x in it2])

# --------------------------------------------------------------------------------------
print ([x for x in enumerate("abcd")])			# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# --------------------------------------------------------------------------------------
from itertools import chain
it1 = iter([1,2,3])
it2 = iter([8,9,0])
for i in chain(it1, it2):
	print(i)					# 1 2 3 8 9 0
#----------------------------------------------------------------------------------------------- 170613 CoRoutines.py
def print_matches(matchtext):
	print("Поиск подстроки", matchtext)
	while True:
		line = (yield) # Получение текстовой строки
		if matchtext in line:
			print(line)


matcher = print_matches("python")
#matcher.next()
matcher.send(None)
matcher.send("Hello World")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close() # Завершение работы с объектом matcher
#----------------------------------------------------------------------------------------------- 170618 BeautifulSoup.py
# pip3 install beautifulsoup4
# pip3.exe install lxml

import requests, bs4
#from lxml import html

#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#print(type(noStarchSoup))

#exampleFile = open("example.html")
#exampleSoup = bs4.BeautifulSoup(exampleFile)
#elems = exampleSoup.select('#author')
#print(type(elems))

url = 'http://www.ebook3000.com/'

# r = requests.get(url)
# Открываем полученный файл и видим, что все не так просто: сайт распознал в нас робота и не спешит показывать данные.
# Однако, у браузера отлично получается получать информацию с сайта. Посмотрим, как именно он отправляет запрос. 
# Для этого воспользуемся панелью "Сеть" в "Инструментах разработчика" в браузере (я использую для этого Firebug), 
# обычно нужный нам запрос — самый продолжительный.

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
      }
r = requests.get(url, headers = headers)
#with open('test.html', 'w') as output_file:
#  output_file.write(str(r.text.encode('cp1251')))
soup = bs4.BeautifulSoup(r.text,"html.parser")
books_list = soup.find('div',{'class':'index_box'})  #<div class="mains_left_box">
items = soup.find_all('div',{'class':'index_box_lit'})  #<div class="mains_left_box">
for item in items:
    print(item.find('a').get('href'))
#----------------------------------------------------------------------------------------------- 170618 Logging.py
import logging

# =================================================
# Отключение логиирования
#logging.disable(logging.CRITICAL)
# =================================================

# Логгирование на экран
#logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
# Логгирование в журнал
logging.basicConfig(filename = '170618 Logging.log', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')

def factorial(n):
    logging.debug('Начало factorial(%s%%)'%(n))
    total = 1
    for i in range(1,n+1):
        total*=i
        logging.debug('i=' + str(i)+', total='+str(total))
        logging.debug('Конец factorial (%s%%)' %(n))
    return total

print(factorial(5))
logging.debug('Конец программы')
#----------------------------------------------------------------------------------------------- 170618 MouseAndKeyboard.py
import pyautogui, time

w,h = pyautogui.size()
print(w,h)

print('Mouse cursor position:',pyautogui.position())

time.sleep(3)
# найдем изображение на экране
x0,y0,x1,y1 = pyautogui.locateOnScreen('submit.png')
print(x0,y0,x1,y1)
pyautogui.moveTo(x0,y0,duration=0.15)

time.sleep(3)


for i in range(2):
	pyautogui.moveTo(100,100,duration=0.15)
	pyautogui.moveTo(200,100,duration=0.15)
	pyautogui.moveTo(200,200,duration=0.15)
	pyautogui.moveTo(100,200,duration=0.15)

time.sleep(3)
pyautogui.scroll(200)

pyautogui.click(100,150,button='middle')
#pyautogui.click(100,150,button='right')

# получим изображение экрана
im = pyautogui.screenshot()
#----------------------------------------------------------------------------------------------- 170618 MouseAndKeyboard-1.py
import pyautogui, time

pyautogui.moveTo(300,800,duration=0.25)
pyautogui.click(300,300,button='left')

time.sleep(1)
pyautogui.typewrite('Hello!',0.25)
pyautogui.typewrite(['left','?','shiftright','del'],0.25)

pyautogui.keyDown('shift')
pyautogui.press('left')
pyautogui.keyUp('shift')

pyautogui.hotkey('shift','left')
#----------------------------------------------------------------------------------------------- 170618 RaiseException.py
def func():
    raise Exception('Это сообщение об ошибке')

# ------------------------------
print('Hello!')
try:
    func()
except Exception as err:
    print('Возникло исключение: ' + str(err))
print('Good bye!')
#----------------------------------------------------------------------------------------------- 170618 RequestAuthentication.py
import os, requests

USERNAME = 'kvn_2001@mail.ru' # put correct usename here
PASSWORD = input('password: ') # put correct password here

os.system('cls')

LOGINURL = 'http://pokazuha.ru/main.cfm?filename=system/login.cfm'
DATAURL = 'http://pokazuha.ru/?nc=21622'

session = requests.session()

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

formdata = {
    'e_mail': USERNAME,
    'rpath': PASSWORD,
    'login_btn' : 'Login'
}

# Authenticate
r = session.post(LOGINURL, data=formdata, headers=req_headers, allow_redirects=False)
print(r.headers)
print(r.status_code)
#print(r.text)

# Read data
r2 = session.get(DATAURL)
print("___________DATA____________")
print(r2.headers)
print(r2.status_code)
print(r2.text)
#----------------------------------------------------------------------------------------------- 170618 WorkWithPDF.py
import os, PyPDF2

# Block One
# ===========================================================================
pdfFileObj = open('E:\\!!BOOKS\\!ЖУРНАЛЫ\\160307 Frommers_Croatia_.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(0 , 5): # pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    print(page)

# Block Two
# ===========================================================================
pdfFileObj = open('E:\\!!BOOKS\\026_Brett_King__Bank_3-0.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print('numPages=',pdfReader.numPages)
print('isEncrypted:',pdfReader.isEncrypted)

pageObj = pdfReader.getPage(6)
print(pageObj)
p10 = pageObj.extractText()
print("Text",p10)

out = PyPDF2.PdfFileWriter()
out.addPage(pdfReader.getPage(6))
out.addPage(pdfReader.getPage(7).rotateClockwise(90))

page8 = pdfReader.getPage(8)
page8.mediaBox.upperRight = (
    page8.mediaBox.getUpperRight_x() / 2,
    page8.mediaBox.getUpperRight_y() / 2
)
out.addPage(page8)

outputStream = open("Результат.pdf", "wb")
out.write(outputStream)
outputStream.close()
#----------------------------------------------------------------------------------------------- 170618 ZipFile.py
import zipfile, os, shutil

os.chdir('E:\\KVN\\!CODE\\PYTHON\\')
newZip = zipfile.ZipFile('new.zip','w')
newZip.write('file.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

exampleZip = zipfile.ZipFile('new.zip')
print(exampleZip.namelist())
zipInfo = exampleZip.getinfo('file.txt')
print(zipInfo.file_size)
print(zipInfo.compress_size)
exampleZip.close()

shutil.move('new.zip','.idea\\new.zip')
os.chdir('E:\\KVN\\!CODE\\PYTHON\\.idea\\')

exampleZip = zipfile.ZipFile('new.zip')
exampleZip.extractall()
exampleZip.extract('file.txt','E:\\KVN\\!CODE\\PYTHON\\VERIFY\\')
exampleZip.close()
#----------------------------------------------------------------------------------------------- 170619 DateTime.py
import datetime

now_date = datetime.date.today() # Текущая дата (без времени)
now_time = datetime.datetime.now() # Текущая дата со временем
 
cur_year = now_date.year # Год текущий
cur_month = now_date.month # Месяц текущий
cur_day = now_date.day # День текущий
cur_hour = now_time.hour # Час текущий
cur_minute = now_time.minute # Минута текущая
cur_second = now_time.second # Секунда текущие
num_week = now_date.isoweekday() # узнаем номер недели (от 1 до 7)
 
now_date = now_date.replace(2011,6,30) # меняем полностью дату на 30.06.2011
now_date = now_date.replace(day=cur_day) # меняем только день
now_date = now_date.replace(month=cur_month) # меняем только месяц
now_date = now_date.replace(year=cur_year) # меняем только год
 
ny_2011 = datetime.date(2011,2,1) # создали дату: 1 февраля 2011 года
delta = ny_2011 - now_date # разница (дельта) в между 2-мя датами
 
delta = datetime.timedelta(days=2) # дельта в 2 дня
now_date = now_date + delta # Узнаем какое число будет через 2 дня
now_date = now_date - delta # или какое число было 2 дня назад

# форматируем дату 
print(now_time.strftime("%d.%m.%Y %I:%M %p")) 	#09.07.2017 01:33 PM
print(now_time.isoformat()) 			# 2017-07-09T13:33:44.544831

#Наиболее интересные директивы используемые для форматирования времени.
#Расположены не в алфавитном порядке, а в логическом)

# %S — секунды. От 0 до 61
# %M — минуты. От 00 до 59
# %H — час. От 00 до 23
# %I — час. От 1 до 12
# %p -После перед полуднем или после (AM или PM)
# %d — день. От 1 до 31
# %j — день как номер года. От 001 до 366
# %A - день недели (Понедельник)
# %a - сокращенно день недели (Пн)
# %m — месяц. От 01 до 12
# %B - название месяца (Январь)
# %b - сокращенное название месяца (Янв)
# %y — год в виде 2-х последних чисел. От 00 до 99
# %Y — год в виде полного числа
#----------------------------------------------------------------------------------------------- 170627 TestFile.py
# -*- coding: cp1251 -*-
import os

SomeText = "Небольшой блок текста."

f = open('test1.txt','wt')
f.write(SomeText)
print(SomeText,file=f)
print(SomeText,file=f,sep='',end='')
f.close()

with open('music.db','rb') as f:
	f.seek(12)		# Перешли к 12-му символу
	print(f.tell())		# Текущее смещение в байтах

	f.seek(1,os.SEEK_CUR)	# Сдвинемся на 1 байт от текущей позиции
	print(f.tell())		# Текущее смещение в байтах

	f.seek(1,os.SEEK_END)	# Сдвинемся на 1 байт c конца файла
	print(f.tell())		# Текущее смещение в байтах

	f.seek(8170)		
	r = f.read()
	print(len(r))
	print(r)
#----------------------------------------------------------------------------------------------- 170627 TestJSON.py
# -*- coding: cp1251 -*-

import json
import codecs

with codecs.open("menu.json","rt") as f:
	js = json.load(f)

print(js)
menu2 = json.dumps(js)
print(menu2)
#{'breakfast': {'items': {'breakfast burritos': '$6.00', 'pancakes':
#'$4.00'}, 'hours': '7-11'}, 'lunch': {'items': {'hamburger': '$5.00'},
#'hours': '11-3'}, 'dinner': {'items': {'spaghetti': '$8.00'}, 'hours': '3-10'}}
#----------------------------------------------------------------------------------------------- 170627 TestXML.py
# -*- coding: cp1251 -*-

# menu.xml
# ....................................
# <?xml version="1.0"?>
# <menu>
# <breakfast hours="7-11">
# <item price="$6.00">breakfast burritos</item>
# <item price="$4.00">pancakes</item>
# </breakfast>
# <lunch hours="11-3">
# <item price="$5.00">hamburger</item>
# </lunch>
# <dinner hours="3-10">
# <item price="8.00">spaghetti</item>
# </dinner>
# </menu>
# ....................................

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)				# 'menu'
for child in root:
	print('tag:', child.tag, 'attributes:', child.attrib)
for grandchild in child:
	print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
#...
#tag: breakfast attributes: {'hours': '7-11'}
#tag: item attributes: {'price': '$6.00'}
#tag: item attributes: {'price': '$4.00'}
#tag: lunch attributes: {'hours': '11-3'}
#tag: item attributes: {'price': '$5.00'}
#tag: dinner attributes: {'hours': '3-10'}
#tag: item attributes: {'price': '8.00'}
print(len(root))			# количество разделов menu
#3
print(len(root[0])) 			# количество элементов breakfast
#2
#----------------------------------------------------------------------------------------------- 170702 TestPandas.py
# -*- coding: cp1251 -*-

import pandas as pd
#import numpy as np

def count_to_len(row):
	row.Count = len(row.Name)
	return row

names = pd.read_csv(r'E:\KVN\!CODE\PYTHON\170702 TestPandas_yob2016.txt') #, names=['Name','Gender','Count’])
# print(names.columns)

print("Sort by Name")
print(names.sort_values(by='Name', ascending=True).head(5))

print("Print only boys")
print(names[names.Gender=='M'].tail(5))

print("Print very popular names")
print(names[names.Count>15000])

print("Print very popular names for boys")
print(names.query("Gender=='M' & Count>15000"))


print("{} boys and {} girls".format(
	names[names.Gender=='M'].Count.sum(), # max(), min(), mean()-среднее, median()-медиана
	names[names.Gender=='F'].Count.sum()
))

print("Print with our function")
nm = names.apply(count_to_len,axis=1)
print(nm[nm.Count>=14])

print('Объединение')
cols = ['Name','Gender','Count']
names_2015 = pd.read_csv(r'E:\KVN\!CODE\PYTHON\170702 TestPandas_yob2015.txt',names=cols)
names_2016 = pd.read_csv(r'E:\KVN\!CODE\PYTHON\170702 TestPandas_yob2016.txt',names=cols)
names_2015_2016 = pd.merge(names_2015,names_2016,
	on=['Name','Gender'],
	suffixes=('_2015','_2016')
)
print(names_2015_2016.head(5))
print("Sum:")
print(names_2015_2016.groupby('Gender').sum())
print("Max:")
print(names_2015_2016.groupby('Gender').max())
#----------------------------------------------------------------------------------------------- 170702 TestPandas-1.py
# -*- coding: cp1251 -*-

import pandas as pd
#import numpy as np

def count_to_len(row):
	row.Count = len(row.Name)
	return row

names = pd.read_csv(r'E:\KVN\!CODE\PYTHON\170702 TestPandas_yob2016.txt') #, names=['Name','Gender','Count’])
# print(names.columns)

print("Print only boys")
print(names[names.Name=='Alex'])
#----------------------------------------------------------------------------------------------- 170703 TestMatPlotLib.py
# -*- coding: cp1251 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand

#plt.plot([1,4,9,16,25,36,49,64])

num = input('Введите номер от 1 до 6')
if num=='1':
	X = [50,10,200,100]
	L = ['A','B','C','D']
	plt.pie(X)
	plt.legend(L)
	plt.show()
elif num == '2':
	X = np.linspace(0,1)
	Y = X**3 - X**2 - 2
        
	plt.plot(X, Y)
	plt.show()
elif num == '3':
	cols = ['Name','Gender','Count']
	data_state_names = pd.read_csv(r'E:\KVN\!CODE\PYTHON\170702 TestPandas_yob2015.txt',names=cols) 
	query = "Name=='Alex'"
	data = data_state_names.query(query).groupby('Gender').sum()
	print(data)

	plt.title(query)
	plt.pie( [data.loc['M'].sum(), data.loc['F'].sum()], colors=['Blue','Red'] )
	plt.legend(['M','F'])
	plt.show()
elif num == '4':
	X = [50,10,200,100]
	Y = np.arange(len(X))

	L = ('A','B','C','D')

	plt.bar(Y,X, align='center')
	plt.xticks(Y, L)
	plt.show()
elif num == '5':
	for color in ['red', 'green', 'blue']:
		n = 10
		x, y = rand(2, n)
		scale = 200.0 * rand(n)
		plt.scatter(x, y, c=color, s=scale, label=color,
                	alpha=0.3, edgecolors='none')

	plt.legend()
	plt.grid()

	plt.show()
elif num == '6':
	data = [np.random.normal(0, std, 100) for std in range(6, 10)]

	plt.boxplot(data)
	plt.xticks(np.arange(len(data)) + 1, ('A','B','C','D'))
	plt.show()
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 

