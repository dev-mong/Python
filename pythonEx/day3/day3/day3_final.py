# list = [1,2,3,4,5]
# size = len(list)
# print(size)


# CRUD
# list = []
# list.append(10)
# list.append(20)
# list.append(30)
# list.append(40)
# print(list)
# list[1] = 1000
# list.remove(10)
# print(list)



# 가위바위보 게임을해서 10번 동안 진행 된 게임에 승패 출력
#
# from random import randrange
#
# count = 0
#
# def game():
#     user = int(input("가위 0 바위 1 보 2"))
#     com = randrange(0, 3)
#
#     if user < com:
#         user = user + 3
#
#     result = user - com
#
#     if result == 2:
#         list = 'w'
#     elif result == 1:
#         list = 'l'
#     else:
#         list = 'd'
#
#     return list
#
#
# result_list = []
#
# while count < 10:
#
#     result = game()
#     print(result)
#     result_list.append(result)
#     count += 1
#     print(count)
#
# print(result_list)


# 로또 문제

# from random import randrange
#
# num_list = []
#
# def check(num_list,num):
#
#     result = False
#
#     for x in num_list:
#         if x == num:
#             result == True
#
#     return result
#
# while len(num_list) < 6:
#     num = randrange(1,46)
#
#     if check(num_list,num) == True:
#         continue
#
#     num_list.append(num)
#
# print(num_list)



# 영화 그래프

import math

movie_list = [
    (0,5,'A'),
    (1,6,'A'),
    (0,8,'A'),
    (4,5,'M'),
    (6,9,'M'),
    (7,4,'M'),
]
def check(x,y):
    caculate = math.sqrt(math.pow(x[0]-y[0],2) +
                     math.pow(x[1] - y[1],2))
    return  caculate

action_input = int(input("액션씬의 횟수"))
kiss_input = int(input("키스씬의 횟수"))

result = (action_input, kiss_input)

movie_list.sort(key=lambda x: check(x,result))

a_cnt = 0
m_cnt = 0

for x in movie_list[0:3]:
    if x[2] == 'M':
        m_cnt += 1
    elif x[2] == 'A':
        a_cnt += 1

print(movie_list[0:3])

if a_cnt > m_cnt:
    print("액션")
elif a_cnt < m_cnt:
    print("멜로")
