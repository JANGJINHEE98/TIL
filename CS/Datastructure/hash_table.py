# case 1 - 딕셔너리로 활용되는 해시테이블을 확인할 수 있다.

test_code = {2.5: 'A' ,'2.0': 'B', '1.0': 'C'}
print(test_code[2.5]) 
print(test_code['1.0'])
print(test_code['2.0'])

print("----------")

# case 2 - 리스트와 튜플을 활용해서 해시테이블을 확인한다.
# 데이터는 튜플로 저장된다.

test_code = [(2.5, 'A'), ('2.0', 'B'), ('1.0', 'C')]
 
def insert(item_list, key, value):
    item_list.append((key, value))
    print(item_list)
 
def search(item_list, key):
    for item in item_list:    # 데이터를 검색하려면 딕셔너리보다 오래 걸린다.(키,값 쌍이 없어서 개별 값으로 반복해서 검색하기 때문이다.)
        if item[0] == key:
            return item[1]      
    print('not matching')       
    
print(search(test_code, '2.0'))
print(search(test_code, 2.5)) 


print("------------")

# 인코딩 예제
bytes_representation = "hello".encode()

for byte in bytes_representation:
    print(byte)


    # 정수값의 합 반환
bytes_representation = "hello".encode()

sum = 0
for byte in bytes_representation:
    sum += byte

print(sum)


# 해시함수를 만들고 활용해보자.
def my_hashing_func(str, list_size):
    bytes_representation = str.encode()    
    sum = 0
    for byte in bytes_representation:
        sum += byte

    print('sum:', sum)
    print('list_size', list_size)
    print('sum%list_size:', sum % list_size)
    return sum % list_size

my_list = [None] * 5

# 위의 my_hashing_func이라는 해시함수를 활용하여 아래처럼 값을 확인할 수 있다.
my_list = [None] * 5

my_list[my_hashing_func("aqua", len(my_list))] = "#00FFFF" # 리스트에 값을 입력

# 여기서 my_list의 4번째(해시값)버킷에 '#00FFFF'가 들어감.

print(my_list[my_hashing_func("aqua", len(my_list))]) # 리스트에 있는 값을 출력

print(my_list)