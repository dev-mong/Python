# my_list =[i % 10 for i in range(0,31)]
# print(my_list)
#
# my_list = [10,20,30,40,50]
# # 인덱스 길이 구하기
# size = len(my_list)
# print(size)
#
# for num in my_list:
#     print(num)




my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# READ
print(my_list[1])

# UPDATE
my_list[1] = 100
print(my_list[1])

# DELETE
my_list.remove(10)
print(my_list)
