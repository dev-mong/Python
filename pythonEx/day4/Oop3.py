class Menu:

    def __init__(self, n, p):
        self.name = n
        self.price = p

class Kiosk:

    #  키오스크안에 메뉴 데이터 저장
    def __init__(self,mlist):
        self.menu_list = mlist

        self.order_list = []

    def start_service(self):
        print("WELCOME ....")

        num = 1

        print("------------")
        for menu in self.menu_list:
            print(num,menu.name,menu.price)
            num += 1
        print("------------")

        choice = int(input("메뉴를 선택하세요, 0을 누르면 완료\n"))

        if choice == 0 :
            return

        self.order_list.append(self.menu_list[choice - 1])

        self.start_service() #여러가지 음식을 먹기 위해 다음 메뉴 선택

    def print_bill(self):
            total = 0
            print("-------중간 영수증---------")
            for order_menu in self.order_list:
                print(order_menu.name,order_menu.price)
                total += order_menu.price
            print("TOTAL : ", total)
            print("------------------------")
            return total

class MainKiosk:
    
    def __init__(self,dic):
        self.kiosks = dic
        self.result = 0
        self.result_order = []
    def service(self):

        # print(self.kiosks)
        idx = int(input("0 or 1 종료를 원하시면 2  \n"))
        total_result = 0

        if idx == 2:
            print("-----최종 영수증---------")
            print("------------------------")
            for x in self.result_order:
                total_result += x
            print("TOTAL : ", total_result)
                # print(x)

            print("------------------------")
            print("종료되었습니다.")
            return

        kiosk = self.kiosks[idx]  # 선택 된 키오스크 번호
        kiosk.start_service()
        # self.result = kiosk.print_bill()
        # self.result_order.append(self.result)
        # 최종 리스트 출력
        # for x in self.result_order:
        #     self.result_order[]
        #     print(self.result_order[])
        # self.result_order.append(kiosk.print_bill.order_menu.name)
        # print(self.result_order)
        self.service()



kiosk1 = Kiosk([Menu('김밥', 3000), Menu('라면', 4000),
                Menu('떡라면', 4000), Menu('쫄면', 2000)
                 ])
kiosk2 = Kiosk([Menu('봉골레', 13000), Menu('까르보나라', 14000),
                Menu('알리올리오', 14000), Menu('로제', 12000)
                 ])

mainKiosk = MainKiosk([kiosk1, kiosk2])
mainKiosk.service()
