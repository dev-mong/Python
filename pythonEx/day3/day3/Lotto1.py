# 로또문제
from random import randrange

nums = []

def checkfunction(nums,num):
    for x in nums:

        break
    return False

# 루프를 nums가 6개가 되는 동안
while len(nums) < 6:

    num = randrange(1, 46)
    nums.append(num)

    if checkfunction(nums,num) == True:
        continue

print(nums)

# 1~45 사이의 숫자를 뽑는다

# 뽑은 값이 있다면 다시 뽑는다.






