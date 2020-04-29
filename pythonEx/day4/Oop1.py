class Circle:

    # 생성자
    def __init__(self):
        print("Circle init")
        self.radius = 10 # 현재 메모리 공간에 데이터를 저장

    def show(self):
        print("show", self.radius)

# 인스턴스
c1 = Circle()
c2 = Circle()

print(c1)
print(c1.radius)
print(c2)
print(c2.radius)

c1.radius = 5
c1.show() #메소드 호출

c2.radius = 10
c2.show()

