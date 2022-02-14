# 오전 Q&A

'''
# 객체의 생성자  (__init__)
# -> 실행할때 자동적으로 호출됨
'''

class Stats():
    def __init__(self):
        self.var = "안녕하세요"
        print("통계 객체가 생성되었습니다.")
    def __del__(self):
        print("통계 객체가 메모리에서 제거되었습니다.")



'''
클래스 소멸자 이해하기 
객체가 사라질때 자동으로 호출되는 함수를 소멸자 (__del__)이라고 한다.
불안정한 기능이라고 하니, 안쓰는 것을 추천
- 관련링크
[python] **del** 메서드는 무엇이며 어떻게 호출합니까?
[http://daplus.net/python-__del__-메서드는-무엇이며-어떻게-호출합니까/](http://daplus.net/python-__del__-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%B4%EB%A9%B0-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%98%B8%EC%B6%9C%ED%95%A9%EB%8B%88%EA%B9%8C/)
메소드 **del** 공식문서
[https://docs.python.org/3/reference/datamodel.html](https://docs.python.org/3/reference/datamodel.html)

특별 메소드 

[https://wikidocs.net/89](https://wikidocs.net/89)
'''

# 객체 제거 
del Stats

try : 
    print(Stats.var)
except : 
    print("객체가 소멸되었으므로 에러남")

'''
# 총 클래스 설계도를 생성하고 객체화 시키시오! 

# 총이 생성
# 총알이 충전
# 총알이 발사 

# 총 설계도를 만들어볼까? 
class Gun:
    def __init__(self) :
        self.bullet = 0
    def charge(self, num) :
        self.bullet = num
        print(self.bullet, '발 충전되었습니다.')
    def shoot(self,num) :
        for i in range(num):
            if self.bullet > 0:
                print("탕!")
                self.bullet -= 1
            elif self.bullet == 0: # 여기서 self는 각각 인스턴스의 자기 자신을 가리키는 말로 사용됨 (인스턴스는 gun1, gun2가 있었죠?)
                print("총알이 없습니다.")
                break


gun1 = Gun()
gun1.charge(10) # 장전
gun1.shoot(3) # 3발 쏨
print("--------")
gun1.shoot(10) # 10발 밖에 없으므로 총알이 바닥남

#----두번째 총----
gun2 = Gun()
gun2.charge(10)

print("gun1, gun2 총쏘기")
gun1.shoot(5)
print("--------")
gun2.shoot(5)
'''

class Gorilla():
    def __init__(self):
        self.banana = 0
    def eat(self, num):
        self.banana = num
    def shout(self, num):
        for i in range(num):
            if self.banana > 0:
                print("우와~~~")
                self.banana -= 1
            elif self.banana == 0:
                print("배고파요....흑흑")
                break

rilla = Gorilla()
rilla.eat(10)
rilla.shout(1)
rilla.shout(5)



# 오후 Q&A -----------------------------------

'''
추상 클래스와 클래스

예를 들어 자료형 str, list의 추상클래스는 object

⇒ 클래스는 '추상적'을 뜻하는 abstract를 붙어요.

⇒ 이 추상클래스로는 객체를 만들 수가 없어요.

⇒ 개라 불리는 동물, 고양이라 불리는 동물은 있지만, 어떤 생물을 '이건 포유류라는 동물이야' 하지는 않죠.

⇒ 직업이 뭐냐고 물을 때 '전문직'이라고 답하지는 않잖아요. 특정 개체를 이걸로 부르기엔 너무 추상적란거에요.

⇒ 자식 클래스들의 공통분모 역할만을 위한 클래스인거죠.
'''

class Gorilla():
    def __init__(self):
        self.banana = 0
    def eat(self, num):
        self.banana = num
    def shout(self, num):
        for i in range(num):
            if self.banana > 0:
                print("우와~~~")
                self.banana -= 1
            elif self.banana == 0:
                print("배고파요....흑흑")
                break



        