#----------------------------------------------------------------------------------------------- 001_HelloWorld.py
var = 'Hello, World!'
a,b,c=1,2,3

print(var)
print('a=',a)
print('b=',b)
print('c=',c)

print(type(var))
print(dir(var))
#----------------------------------------------------------------------------------------------- 002_Input.py
user = input('I am Python. What is your name? ')
print('Hello, ',user)
#----------------------------------------------------------------------------------------------- 003_If.py
a=2
b=3
c=a if (a<b) else b
print(c)

nm = 7*2
print(nm, ' - число','четное' if (nm %2 == 0) else 'нечетное')
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
#----------------------------------------------------------------------------------------------- 005_Tuple.py
c_tuple = ['Red','White','Black','Blue']
a,b,c,d=c_tuple
print(b)
#----------------------------------------------------------------------------------------------- 006_Set.py
set1 = {'Red','White','Black','Blue'}
print(len(set1))
print(type(set1))
#
set1.add('Green')
print(len(set1))
#
print('Green' in set1)
#----------------------------------------------------------------------------------------------- 007_iif.py
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
print('End')
#----------------------------------------------------------------------------------------------- 009_for.py
chars = ('A','B','C')
fruit = {'Apple', 'Banana', 'Cherry'}
dict = {'Имя':'Иван','Отчество':'Иванович','Фамилия':'Иванов'}
#print(dict['Имя'])
#
for item in zip(chars,fruit):
	print(item)
#
for key, value in dict.items():
	if key=='Отчество':
		continue
	print(key,'=',value)
#----------------------------------------------------------------------------------------------- 010_Strings.py
var=' привет, люди! '
print(var.title())
print(var.upper())
print(var.lower())
print(var.rstrip())
print(var.lstrip())
print(var.strip())
#----------------------------------------------------------------------------------------------- 011_for_and_if.py
list = [1,2,3,4,5]

for elem in list:
	if elem==2:
		print("sorry, we are out of element 2 right now")
	else:
		print(elem)
print("\nFinished making your pizza")
#----------------------------------------------------------------------------------------------- 012_dict.py
dict = {
	'Иван':'инженер',
	'Петр':'старший инженер',
	'Сергей':'главный инженер',
	'Андрей':'начальник'
		}

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
#----------------------------------------------------------------------------------------------- 
