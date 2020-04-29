# from random import randrange
#
# num = randrange(0,4)
# count = 0
#
# while True:
#
#     input("Enter를 누르시오")
#
#     if num == count:
#         print("당첨")
#         break
#     else:
#         print("꽝")
#
#     count = count + 1



# Min = 1
# Max = 100
# Mid = 0
#
# while True:
#
#     Mid = int((Min + Max)/2)
#     print(Mid)
#
#     x = input("높으면 H 낮으면 L 맞으면 C")
#
#     if x == 'H':
#         Min = Mid
#     elif x == 'L':
#         Max = Mid
#     elif x == 'C':
#         break

# from random import randrange
#
# user_count = 0
# com_count = 0
#
# while True:
#
#     com = randrange(0,3)
#     print(com)
#      user = int(input("가위 0, 바위 1, 보 2"))
#
#     if user > com:
#         com = com + 3
#
#     result = com - user
#
#     if result == 2:
#         print("WIN")
#         user_count = user_count + 1
#         com_count = 0
#     elif result == 1:
#         print("LOSE")
#         com_count = com_count + 1
#         user_count = 0
#     elif result == 0:
#         print("DRAW")
#
#     if user_count == 3 or com_count == 3:
#         break



from random import randrange

def game():

    com = randrange(0, 3)
    print("컴 값",com)
    user = int(input("가위 0, 바위 1, 보 2"))


    result_str = ''

    if user > com:
        com = com + 3

    result = com - user

    if result == 2:
        result_str = 'user_win'

    elif result == 1:
        result_str = 'com_win'

    elif result == 0:
        result_str = 'd'

    print(result_str)

    return result_str

count = 0
before = ''

while True:

    result = game()

    if result == before:
        count = count + 1
    elif result == 'd':
        continue
    else:
        count = 1
        before = result

    if count == 3:
        break





