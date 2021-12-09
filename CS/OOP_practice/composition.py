# 포함 코드 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print('Person_printPerson')

class Student(Person):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age) # 여기도 self를 넣어줬네? 
        Person.printPerson(self) # 여기에서 self를 넣어주는 이유? class의 메소드가 통째로 포함이라서 그런가? 
        self.id = id

    def test(self, score):
        if score>80:
            print(self.name + " studies hard")
        else :
            print(self.name + " needs supplementary lessons")


# object 생성
# 한 번 생성된 object는 파라미터가 변하지 않는 이상 출력값 또한 변하지 않는다.
s = Student("Dave", 20, 1)

# object 실행
print("s.age:", s.name)   # result : Dave
print("s.age:", s.age)   # result : 20
print("s.id:", s.id)   # result : 1
print('\n')

s2 = Student("Jamie", 25, 2)
print("s2.age:", s2.name)   # result : Jamie
print("s2.age:", s2.age)   # result : 25
print("s2.id:", s2.id)   # result : 2
print('\n')

print('-- test score result --')
s.test(52)
s2.test(88)

# 포함코드2

# 클래스 선언 
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    
    def about(self):
        print(f"This duck has a {self.bill.description} and a {self.tail.length}.")

# object 생성 
duck = Duck(Bill('big bill'), Tail('long tail'))

# object 실행 
duck.about()

'''
먼저 Bill('big bill')이 Duck()의 self.bill로 들어간다. 
self.bill = Bill('big bill')
따라서 self.bill.description은 Bill의 description 메소드를 가리키는것이 됨! 
'''