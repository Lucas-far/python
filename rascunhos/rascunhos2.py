

from os import chdir
text = []
text2 = []
text3 = []
text4 = []
text5 = []
chdir('/home/lucas/')
with open('my_log.txt', 'r') as txt:
    for row in txt:
        text.extend([row])
print('\n' * 2)

"---------------------------------------------------------------------------------------------------------------------"
print([1], 'text =', '\n', text)
for obj in text:
    # print(obj.index(':', 17))
    text2.extend([obj[25:]])
print([2], 'text2 =', '\n', text2)
"---------------------------------------------------------------------------------------------------------------------"

"---------------------------------------------------------------------------------------------------------------------"
for obj in text2:
    text3.append(obj.split('\n'))
print([3], 'text3 =', '\n', text3)
"---------------------------------------------------------------------------------------------------------------------"

"---------------------------------------------------------------------------------------------------------------------"
for obj in text3:
    text4.append(obj[0])
print([4], 'text4 =', '\n', text4)
"---------------------------------------------------------------------------------------------------------------------"

"---------------------------------------------------------------------------------------------------------------------"
for obj in text4:
    if len(obj) == 3:
        text5.extend(obj[1])
    else:
        text5.extend([obj])
print([5], 'text5 =', '\n', text5)
"---------------------------------------------------------------------------------------------------------------------"



# for obj in text4:
#     text5.append(obj.split("'"))
# print(text5)
#
# for obj in text5:
#     print(len(obj) == 3)

""
# text5 = []
# contador = 0
# while contador < len(text4):
#     if text4[contador] == 'Key.shift':
#         text5.append(contador)
#     contador += 1
# print('\n', 'Tecla "Key.shift" encontradas nos índices: ', text5, '\n')
#
# for obj in text5:
#     text4[obj] = ''
# print(text4)
#
# text6 = []
# contador2 = 0
# while contador2 < len(text4):
#     if text4[contador2] == 'Key.space':
#         text6.append(contador2)
#     contador2 += 1
# print('\n', 'Tecla "Key.space" encontradas nos índices:', text6, '\n')
#
# for obj in text6:
#     text4[obj] = ' '
# print(text4)
""

# print(len(text))
# for index in text:
#     if len(index) <= 29:
#         text2.extend([index])
# print(text2)
# print(len(text2))

"RASCUNHO"
# print(text2[0])

"RASCUNHO"
# for index in text2:
#     print(index.split()[2].split("'")[1] + ' ', end='')
    # print(index.split()[2])
