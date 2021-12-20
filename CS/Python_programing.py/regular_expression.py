# 정규식
import re

wordlist = ["color", "colour", "work", "working", "fox", "worker", "working"]

for word in wordlist:
    if re.match('col..r', word):
        print(word)

regular_expressions = '<html><head><title>Title</title>'
print(len(regular_expressions))

print(re.match('<.*>', regular_expressions).span()) # 0,32

print(re.match('<.*>', regular_expressions).group())  # <html><head><title>Title</title>

print(re.search('<head>.*>', regular_expressions).group()) # match로 할 경우에는 에러가 뜸


# case 1_1
# re.compile 쓰기! 
# re.search 나 re.match 처럼 쓸때마다 re를 import 할 필요 없으니 가벼워진다. 

phone = re.compile(r"""
010-    # 핸드폰 앞자리 
\d{4}-  # 중간자리
\d{4}  # 뒷자리
""", re.VERBOSE) #verbose 옵션을 사용하면 compile할때 whitespace는 제외! -> 보기 쉽게 만들 수 있다. 

# case 1_2
phone = re.compile(r"010-\d{4}-\d{4}")

# case 1_3
info = ['홍길동 010-1234-1234', '고길동 010-5678-5679']

for text in info:
    match_object = phone.search(text)
    print(match_object.group())