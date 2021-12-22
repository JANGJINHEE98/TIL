### rjust(width, [fillchar])

# 002
print("2".rjust(3,"0"))

# 50000
print("50000".rjust(5,"0"))

# "aa123"
print("123".rjust(5,"a"))

### zfill(width) -> 0으로 앞을 채워줌

# 002
print("2".zfill(3))

### split

string_ = "Hello, I am Jack and I am a data scientist"
print(string_)
print(string_[1])

string_list = string_.split(" ")
print(string_list)

# startswith -> 특정 문자열(string_)이 특정 문자(Hello)로 시작하는지 여부를 알려줌 
print(string_.startswith('Hello')) # True
print(string_.startswith('Jack'))

print(string_.endswith('scientist')) # True
print(string_.endswith('tist')) # True

print(string_.replace("Jack", "John")) # Hello, I am John and I am a data scientist
print(string_) # Hello, I am Jack and I am a data scientist -> 원래 문자열 변하지 않음

### 얕은 복사(copy())

fruits = {"apple", "banana", "cherry"}
fruits_copy = fruits.copy()
print(fruits_copy)

print("-----------------")

a = {'a': 5, 'b': 4, 'c': 8}
b = a # 주소 반환?
del b['a']
print(b) # {'b': 4, 'c': 8}
print(a) # {'b': 4, 'c': 8}

print("-----------------")

import copy
a = {'a': 5, 'b': 4, 'c': 8}
b = copy.copy(a)
del b['a']
print(b) # {'b': 4, 'c': 8}
print(a) # {'a': 5, 'b': 4, 'c': 8}

### 깊은 복사(deep copy)
# 깊은 복사는 내부에 객체들까지 새롭게 copy 되는 것이다.
# 완전히 새로운 변수를 만드는 것이라고 볼 수 있다.

import copy
list_var = [[1,2],[3,4]]
list_var_deepcopy = copy.deepcopy(list_var)
list_var_copy = list_var.copy()
list_var_copy2 = copy.copy(list_var)

list_var[1].append(5)

print(list_var)  # 원래 변수

print(list_var_deepcopy)  # deepcopy : append와 같은 메소드를 써도 값이 변경되지 않음

print(list_var_copy)  # copy : 원본이 변경되었으므로 함께 변경됨

print(list_var_copy2)