'''
private 접근 하는 법 
[인스턴스명]_[클래스명]__[접근하고자 하는 private함수나 변수]
'''

class Point:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.__private_name = "private 접근"

class Point_sub(Point):
  def __init__(self,x, y):
    Point.__init__(self,x,y)
    self.x = x
    self.y = y
    
  def __sub(self):
    self.__x = 10
    self.__y = 20

  def sub(self):
    self.__sub()
    print(self.__x)
    print(self.__y)

my_point = Point(1, 2)

# Answer
print(my_point._Point__private_name)