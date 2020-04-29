from random import randrange

value = randrange(0,4)

current = 0

while True:
    input("마음에 준비를 하시고 Eenter")

    print(current, value)

    if current == value:
        print("당첨")
        break
    else:
        print("꽝")

    current = current + 1


