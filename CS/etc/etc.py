# 카드 만들기 

# class Card():
#     def __init__(self):
#         self.monmey = 0
#         print("카드가 발급되었습니다")
#     def charge(self, howmuch_charge):
#         self.monmey += howmuch_charge
#         print(f"{howmuch_charge}원 충전되었습니다.")
#         print(f"현재 잔액은 {self.monmey}원 입니다.")
#     def consume(self, howmuch_used):
#         if self.monmey >= howmuch_used :
#             self.monmey = self.monmey-howmuch_used
#             print(f"{howmuch_used}원 사용되었습니다. 잔액은 {self.monmey}원 남았습니다.")
#         else :
#             print("잔액이 부족합니다!!!!")

# card1 = Card()
# card1.charge(10000)
# card1.consume(5000)
# card1.consume(5000)
# card1.consume(1000)
# card1.charge(10000)

'''
야심차게 카드를 만들었지만, 할인하나 안해주는 카드를 사람들이 발급할리가 없었다. 
흑흑...
그렇게 카드에 할인기능을 넣게 되는데...!

'''
class Card():
    def __init__(self):
        self.monmey = 0
        print("카드가 발급되었습니다")
    def charge(self, howmuch_charge):
        self.monmey += howmuch_charge
        print(f"{howmuch_charge}원 충전되었습니다.")
        print(f"현재 잔액은 {self.monmey}원 입니다.")
    def consume(self, howmuch_used, place):
        if self.monmey >= howmuch_used :
            if place == '카페':
                howmuch_used = howmuch_used*0.5
                self.monmey = self.monmey-howmuch_used
                print(f"50퍼센트 할인되어 {howmuch_used}원 사용되었습니다. 잔액은 {self.monmey}원 남았습니다.")
            else :
                print(f"{howmuch_used}원 사용되었습니다. 잔액은 {self.monmey}원 남았습니다.")
        else :
            print("잔액이 부족합니다!!!!")


# 오버라이드 
# 상속받는 자식이 부모의 일부분을 대신하는 것?

class Cafe_Card(Card):
    def consume(self, howmuch_used, place):
        if self.monmey >= howmuch_used :
            if place == '카페':
                howmuch_used = int(howmuch_used*0.5)
                self.monmey = self.monmey-howmuch_used
                print(f"50퍼센트 카페 할인되어 {howmuch_used}원 사용되었습니다. 잔액은 {self.monmey}원 남았습니다.")
            else :
                print(f"{howmuch_used}원 사용되었습니다. 잔액은 {self.monmey}원 남았습니다.")
        else :
            print("잔액이 부족합니다!!!!")

card1 = Cafe_Card()
card1.charge(10000)
card1.consume(5000, '넷플릭스')
card1.consume(5000, '카페')
card1.consume(1000, '카페')
card1.charge(10000)