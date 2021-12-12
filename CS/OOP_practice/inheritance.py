# 상속코드 

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person): # Person 클래스 상속받음(name 변수를 파라미터로 재사용)
    def study(self):
        print(self.name + " studies hard")

class Employee(Person):     # Person 클래스 상속받음(name 변수를 파라미터로 재사용)
    def work(self):
        print (self.name + " works hard")

# object 생성
s = Student("Dave")
e = Employee("David")

# object 실행
print(s.study())
print(e.work())