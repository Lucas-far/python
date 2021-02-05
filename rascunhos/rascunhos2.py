

from os import chdir
text = []
text2 = []
chdir('/home/lucas/')
with open('my_log.txt', 'r') as txt:
    for row in txt:
        text.extend([row])

# print('===============================================================================================================')
print(text)
print(len(text))
for index in text:
    if len(index) <= 29:
        text2.extend([index])
print(text2)
print(len(text2))
for index in text2:
    print(index.split()[2].split("'")[1] + ' ', end='')
    # print(index.split()[2])
