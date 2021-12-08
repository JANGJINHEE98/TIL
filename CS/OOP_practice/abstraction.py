# 추상화 코드 

'''
추상화란 ?
복잡한 내용은 숨기고 주요 기능에만 신경 쓰자! 

변수, 함수(예를 들어 print함수), 객체

추상 클래스란? 
파생 클래스가 구현해야 하는 메소드를 정해줌
파생 클래스의 메소드들이 모두 구현되지 않았을 경우 인스턴스를 만드는 과정에서 오류가 발생 할 것임
추상 클래스는 인스턴스로 만들 수 없다. -> pass를 이용해서 빈 메서드로 만들자. 
추상클래스는 오로지 상속에만 사용함!  
[참고 사이트]
https://dojang.io/mod/page/view.php?id=2389

[note 내용]
기본개념 : 추상화(abstraction)는 복잡한 내용에서 핵심적인 개념 및 기능을 요약하는 것을 말한다.

object의 기능에 따라 추상클래스(상위클래스)를 상속받아 개별적으로 클래스(하위클래스)를 생성한다.

기본적으로 추상메소드를 선언하며 실제 실행되는 기능은 보여지지 않는다.

실제 실행되는 기능은 선언된 추상클래스를 상속받은 다른 클래스의 메소드에서 확인할 수 있다.

추상클래스를 사용하는 이유

대형 프로젝트를 진행하는 경우 또는 프로그램이 복잡해지는 경우 1차적인 설계를 위해 기능을 추상화시켜놓고, 활용여부는 차후 결정하기 위함이다.

'''

from abc import * #abc모듈의 클래스와 메소드를 갖고온다. (abc: abstract base class)

class People(metaclass=ABCMeta):
    
    # 추상 메소드 만들기 
    @abstractclassmethod # 추상 메소드에는 @abstractclassmethod를 선언해 줘야 하는 점 잊지마! ㅇ_<
    def charecter(self):
        pass

# 상속 받는 클래스 
class Student(People):
    def charecter(self, pow, think):
        self.pow = pow
        self.think = think

        print('체력: {0}'.format(self.pow))
        print('생각: {0}'.format(self.think))
    
# 상속받는 클래스
class Driver(People):
    def charecter(self, pow, think):
        self.pow = pow
        self.think = think

        print('체력: {0}'.format(self.pow))
        print('생각: {0}'.format(self.think))

# Student object 생성      
peo1 = Student()
print('Student : ')

# Student object 실행
peo1.charecter(30, 10)

print()

# Driver object 생성
peo2 = Driver()
print('Driver : ')

# Driver object 실행
peo2.charecter(10, 10)