# height = 1.8
# weight = 75

height = float(input("키는 몇인가요?"))
weight = float(input("몸무게는 몇인가요?"))

result = weight / (height * height)

print(result)

#작은 값 부터 if문 처리
if result < 18.5:
    print("저체중")
# elif 18.5 <= result < 23: (X) if
elif result < 23:
    print("정상체중")
elif result < 25:
    print("과체중")
else:
    print("비만")


