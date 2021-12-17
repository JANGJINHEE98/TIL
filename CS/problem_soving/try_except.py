# try except
# isinstance


## 아래의 test 딕셔너리를 사용해서 아래처럼 출력되도록 만드시오.
test = {'A': 5, '1': 'B', 'C': 9, 'D': 6, '5': 'E', 'F': 'G', '3':'9'} 
result = {'A': 5, 'B': 1, 'C': 9, 'D': 6, 'E': 5}

result = dict()

for a,b in test.items():
    try:
        if int(a):  #만약 int(a)가 되면? 
            a = int(a)
        if int(b):  # '3':'9'때문에 필요
            b = int(b)
    except:
        pass
    if type(a) != type(b):
        if isinstance(b, str):
            result[b] = a
        else:
            result[a] = b

print(result)





