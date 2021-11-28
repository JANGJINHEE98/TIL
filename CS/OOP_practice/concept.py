'''
# intro coding 

import random

input_num = int(input())

for i in range(input_num):
  ran_num = random.randint(1,100)
  print(ran_num, end = ' ')

  if ran_num == input_num:
    print("input random number print")
    continue

else:
  print('exit')
'''


# 절차 프로그래밍 (Provedural Programming)
# 조건 또는 기능이 증가할 때마다 함수와 변수 같은 요소가 계속 증가할 수 있으므로 비효율적이다. 

# 케이스 1 : 함수활용
def carAttribute():
  speed = 50
  color = 'black'
  model = 'CarModel'
  return speed,color,model

# return값을 통해 함수 요소값을 확인할 수 있다.
print("Car Attribute: ", carAttribute())

# 케이스 2 : 변수활용
speed = 50
color = 'black'
model = 'CarModel'

# 해당 변수를 각각 명시해주어야 한다.
print("Car Attribute: ", speed,color,model)

# Bus()나 Bus나 똑같음
class Bus:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive_bus(self):
        self.speed = 70

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    def drive_car(self):
        self.speed = 50

myCar = Car(0, "green", "testCar") # 인스턴스 (객체) 생성 / 객체화 
print("--------Car Object Create Complete--------")
print("Car Speed: ", myCar.speed)
print("Car Color: ", myCar.color)
print("Car Model: ", myCar.model)
try : 
    print("Bus color: ", myBus.color) #에러가 남
except :
    pass

myBus = Bus(0, 'black')
print("--------Bus Object Create Complete--------")
print("Bus color: ", myBus.color)

# 운전 중이 아니므로 speed는 0을 출력한다.
print("--------Car/Bus Speed 1--------")
print("Car Speed by drive: ", myCar.speed)
print("Bus Speed by drive: ", myBus.speed)

# Car/Bus object method Call # 이 부분이 조금 이해가 안됨! 
# 메소드 호출 하는 법 
# 객체명.함수()
myCar.drive_car()
myBus.drive_bus()

# 각각의 개체가 각자의 속도로 움직이고 있다.
print("--------Car/Bus Speed 2--------")
print("Car Speed by drive: ", myCar.speed)
print("Bus Speed by drive: ", myBus.speed)


