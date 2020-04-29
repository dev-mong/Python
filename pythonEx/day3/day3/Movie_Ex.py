import math

movie_sample = [
    ('M',0,4),
    ('M',3,10),
    ('M',6,7),
    ('M',4,1),
    ('A',0,10),
    ('A',7,5),
    ('A',7,5),
    ('A',6,2)
]

def cakcDistance(point1,point2):
    result = math.sqrt( math.pow(point1[0] - point2[0],2) +
                        math.pow(point1[1] - point2[1],2) )
    return result



count_kiss = int(input("키스씬의 숫자를 입력하세요"))
count_action = int(input("액션씬의 숫자를 입력하세요"))



