import time
# 총 수입 = 수입 - 지출
price = 5.0
people = 120
before = 0.0

while True:
    # 수입 = 티켓가격 * 관객수
    income = price * people
    # 지출 = 고정비용 (180) + 관객수 * 0.04
    outcome = 180 + (people * 0.04)
    total = income - outcome

    time.sleep(0.2)
    print("Total:", total," before" ,before,"Price",price)

    price = price - 0.1
    people = people + 15

    if before > total:
        break

    # *****
    before = total

print(before)
