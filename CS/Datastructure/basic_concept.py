# len() 함수를 활용하여 배열의 원소길이 구하기
# 기존에 파이썬에서 배웠던 리스트 메소드이다.

x = [15,'x',20,13,['a','b'], 'cde','1']

# 리스트의 전체 길이 출력
print(len(x))
# 리스트의 특정 인덱스의 길이 출력
print(x[1],'의 length: ', len(x[1]))
print(x[4],'의 length: ',len(x[4]))
print(x[5],'의 length: ',len(x[5]))
print(x[6],'의 length: ',len(x[6]))
# print(x[6],'의 length: ',len(x[0]))  # 주석 풀어서 에러파악


# 리스트 인덱싱/슬라이싱 예시

s = [11,22,33,44,55]

print('s[0:3] 결과:', s[0:3])
print('s[:3] 결과:', s[:3])
print('s[1:] 결과:', s[1:])
print('s[::2] 결과:', s[::2])
print('s[0:1:3] 결과:', s[0:1:3])
print('s[-3] 결과:', s[-3])
print('s[-3:-1] 결과:', s[-3:-1])
print('s[1:-1] 결과:', s[1:-1])

# 예시1 - 회문(팰린드롬) 토마토, 기러기
'''
def ispalindrome(s):
    return_numbers = []
    for char in s:
      if char.isalnum(): #문자열이 영어,한글,숫자일 경우 True 아니면 False
        return_numbers.append(char.lower()) # 위의 조건이 True일 경우에만! lower로 바꿔줘서 리스트에 넣어준다
      
    while len(return_numbers) > 1:
      if return_numbers.pop(0) != return_numbers.pop():
        return False

    return True

test_string = input()
print(ispalindrome(test_string))
'''

# 예시2 - 문자열 뒤집기(반복문과 조건문, 대입개념 활용)

def reverse_string(strtest):
  left, right = 0, len(strtest) - 1
  while left < right:
    strtest[left], strtest[right] = strtest[right], strtest[left]
    left += 1
    right -= 1

  return strtest

strtest =['a','b','c','d']
print(reverse_string(strtest))
print(strtest) # 위의 print 결과와 비교해보자.