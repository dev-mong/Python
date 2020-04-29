#
# member = ('user00', 1234, 'cookie')
#
# member = {d:'user00', 'pw':'pw00', 'name:''Hong'}
# # print(member[0])
#
#
#
# for x in member:
#     print(x)

movie_list = [
    ('A',3,2),
    ('M',12,3)
]

# 이중 for문
for data in movie_list:
    for m in data:
        print(m, end=" ")
    print()
