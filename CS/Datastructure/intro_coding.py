def twonumbersum(numbers, result):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == result:
        return [i,j]

numbers = [int(numbers) for numbers in input("리스트값을 입력하세요 : ").split(',')]
result = int(input("두 수의 합을 입력하세요 : "))
print("인덱스값 : ", twonumbersum(numbers,result))