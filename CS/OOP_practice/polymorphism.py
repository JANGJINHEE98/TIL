# 다형성 

'''
다형성은 구현되는 하위 클래스에 따라 클래스를 다르게 처리하는 기능 
상속과 다른점 : 
상속은 상위 클래스의 기능(함수, 변수)을 재사용
다형성은 상위 클래스의 기능을 변경하여 사용 (그대로 재사용 X)
'''

class Person :
    def run(self):
        print("I'm a human: ", end='')
        print('run')

    def play(self):
        print("I'm a human: ", end='')
        print('run')

class Student(Person):
  def run(self):
    print("I'm a student: ", end='')
    print('fast run')
  
  def play(self):
    print("I'm a student: ", end='')
    print('play')

class teacher(Person):
  def teach(self):
    print("I'm a teacher: ", end='')
    print('teach')

  def play(self):
    print("I'm a teacher: ", end='')
    print('teach play')

# 리스트를 생성한다.
number = list()

# 생성한 리스트에 다형성 개념을 위해 다른 클래스(Student, teacher)가 상위 클래스(Person)를 참조할 수 있도록 한다.
number.append(Student())  # 리스트 끝에 서브 클래스 Student()를 넣습니다. 
number.append(teacher())  # 다시 리스트 끝에 서브 클래스 teacher()를 넣습니다.

print("=========")
for Runner in number:
    Runner.run()     # 상위클래스인 Person의 run은 상속하여 사용하지만 내용은 다르다.

print("=========")
for Player in number: 
    Player.play()    # 상위클래스인 Person의 play는 상속하여 사용하지만 내용은 다르다.

'''
결과 
=========
I'm a student: fast run -> run메소드의 결과가 바뀜
I'm a human: run -> run메소드가 하위 클래스에 따로 없으므로? 그냥 기본 run이 나오는 듯?
=========
I'm a student: play
I'm a teacher: teach play
'''