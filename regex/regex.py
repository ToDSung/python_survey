import re

# re.match() 從字串首字開始比對

eg1 = re.match('www', 'www.runoob.com')
eg2 = re.match('com', 'www.runoob.com')

print(eg1)
# <_sre.SRE_Match object; span=(0, 3), match='www'>
print(eg2)
# None

# . 表示所有可能的字元 
# * 其前的字元或字元集合可出現任何次數或不出現 eg: sky*blue 比對 skblue skyblue skyyyblue
# ? 前一個字串出現或不出現 eg: facebo?k 比對 facebk or facebok
# + 前一個字串出現一次或以上 eg: sky+blue 比對 skyblue or skyyyblue
# *?, +?, ?? 會找到第一個符合的字段
eg3 = re.match(r'(.*) are (.*?) .*', 'Cats are smarter than dogs')

print(eg3.group())
# Cats are smarter than dogs
print(eg3.group(1))
# Cats
print(eg3.group(2))
# smarter
print(eg3.groups())
# ('Cats', 'smarter')

eg4 = re.match(r'dogs', 'Cats are smarter than dogs')
# re.M 多行 re.I 忽略大小寫
eg5 = re.search(r'dogs', 'Cats are smarter than dogs', re.M|re.I)

if eg4:
    print(eg4.group())
else:
    print('No mathch')
print(eg5.group())

# #.*$ 用來比對python 註解 eg: 2004-959-559 # 這是一個國外電話號碼

eg6 = re.search(r'#.*$', '2004-959-559 # 這是一個國外電話號碼', re.M|re.I)
print(eg6.group())
# # 這是一個國外電話號碼
eg7 = re.sub(r'#.*$', "", '2004-959-559 # 這是一個國外電話號碼')
print(eg7)
# 2004-959-559
# \D = [^0-9] 比對任何非數字字符出來 替換成 ""
eg8 = re.sub(r'\D', "", '2004-959-559 # 這是一個國外電話號碼')
print(eg8)
# 2004959559

pattern = re.compile(r'\d+')

eg9 = pattern.findall('www.123.com.tw.546')
eg10 = pattern.findall('91huioph401h07123')

print(eg9)
# ['123', '546']
print(eg10)
# ['91', '401', '07123']

# '(?P...)'
s = '1102231990xxxxxxxx'
res = re.search(r'(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
# {'province': '110', 'city': '223', 'born_year': '1990'}