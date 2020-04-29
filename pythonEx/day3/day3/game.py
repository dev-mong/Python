from random import randrange

result_list = []

for x in range(10):
    user_num = int(input("가위 0 바위 1 보 2"))

    com_num = randrange(0,3)

    if com_num < user_num:
        com_num += 3

    gap = com_num - user_num

    result = ''

    if gap ==2:
        result = 'u'
    elif gap == 1:
        result = 'c'
    elif gap == 0:
        result = 'd'

    result_list.append(result)

print(result_list)