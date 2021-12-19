# 컬렉션 자료형의 내장메소드 
# append(), extend(), insert()

# append()
my_list=[]
for i in range(1000, 2200):
    if (i%7==0) and (i%5!=0):
        my_list.append(str(i))

print(','.join(my_list))

# insert()
my_list=[]
for i in range(1000, 2200):
    if (i%7==0) and (i%5!=0):
        my_list.insert(len(my_list), str(i))

print(','.join(my_list))

print("==================")

li = [1,2,3,4]
li.insert(0, '숫자를 세볼게!')
print(li)

print("==================")

# extend 
list_1 = ['bread', 'meat']
list_2 = ['Lettuce',2 ,5]
list_1.extend(list_2) # extend는 요소 하나씩 넣어줌 만약 append였으면 이 리스트를 통째로 넣었을 것!
print('list1: {}, list2: {}'.format(list_1, list_2))


print("===============================================")

# del, remove, pop

# remove
list1 = [11, 12, 43, 4, 6]
for i in list1.copy():
    if not i % 2: # 여기서 not은 true일경우, false 처럼 반대의 boolean을 반환해준다. 2로 나눠질 경우 나머지는 0이고, 0 == false이므로, not 2%i 곧 2로 나눠 지는 것들만 true가 반환되어 리스트에 들어가게 된다.
        list1.remove(i)
print(list1)

# del
my_list = [1, 2, 3, 4, 5]
my_list[0] = 99
print(my_list)

del my_list[0] # 리스트의 0번째 요소를 지워준다
print(my_list)

# pop
my_list = [1, 2, 3, 4, 5]
my_list[0] = 99
print(my_list)

my_list.pop()
print(my_list)

# count()와 index()
my_list = ['xyz', 'XYZ' 'abc', 'ABC']
print("Index for xyz : ",  my_list.index( 'xyz' )) # 몇번째 인덱스에 있는지
print("Index for ABC : ",  my_list.index( 'ABC' ))

my_list = ['xyz', 'XYZ' 'abc', 'ABC']
print("Count for xyz : ",  my_list.count( 'xyz' )) # 몇개 있는지?
print("Count for ABC : ",  my_list.count( 'ABC' ))

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top+bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,102))

def list_update(data):
    new_li=[]
    new_set = set()
    for item in data:
        if item not in new_set:
            new_set.add(item) # set은 add를 이용해서 1개의 값을 추가 할 수 있다.
            new_li.append(item)

    return new_li

list_test=[120,120,10,20,30,20]
print(list_update(list_test))

# sort, sorted 
from operator import itemgetter
'''
l = []
while True:
    s = input()
    if not s: # s 에 어느 문자라도 들어가면(!= 0) False / 아무것도 들어가지 않으면(== 0) not 으로 False -> True 된다. 입력을 멈추고 싶으면 enter를 치라는 뜻!
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))

# 입력 테스트 시, ('dave', 'B', 10) 처럼 아이템인덱스 채워주기
'''

# get()
# dic = {}
# s=input()
# for s in s:
#     dic[s] = dic.get(s,0)+1
# print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('hi', '33'))