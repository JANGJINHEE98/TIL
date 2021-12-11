# 캡슐화 코드

class Encap:
    def __init__(self, value):
        self.value = value
        print('init:', self.value)

    def _set(self): # 언더바 앞에 하나 붙은 경우  : 이 모듈내에서만 변수/함수를 사용하겠다는 의미 
        print('set:', self.value)

    def printTest(self):
        print('printTest :', self.value)


e = Encap(10)

# case 1
print(e.__init__(20))
print(e._set())
print(e.printTest())

print("---------")

# case 2
print(e.__init__(30))
print(e._set())
print(e.printTest())

# 먼저 init : 10이 자동으로 실행됨(생성자니깐!)
# 그리고 _set은 접근이 가능했음(?) -> 아직 잘 이해하지 못함
