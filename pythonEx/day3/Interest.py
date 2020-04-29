
money = 1000
rate = 0.0075

count = 0

# while True:
#   if count == 10:
#   break
# while count <= 10:

for x in range(1,11):
    money = money + (money * rate)
    print(x,money)

    # count = count + 1
    count += 1