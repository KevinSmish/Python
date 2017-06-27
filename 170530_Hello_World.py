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
#----------------------------------------------------------------------------------------------- 170530 PyCharmTest.py
from collections import OrderedDict

d = OrderedDict([
    ('one',1),
    ('two',2),
    ('three',3)])

print(d.keys())
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
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------- 

