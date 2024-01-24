import sys

N = int(sys.stdin.readline()) # 상근쓰 카드 개수
card_list = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline()) #구해야 할 카드 개수
request_1 = list(map(int,sys.stdin.readline().split()))
request_2 = set(request_1) 

com_set = request_2 - card_list # 중복되는 값 구하기
result = [] #최종 값 출력 리스트 
for each in request_1 :
    if each in com_set:
        result.append(0)
    else:
        result.append(1)

print(*result)



#시간 초과 (sys 모듈 사용)
"""
import sys

N = int(sys.stdin.readline()) # 상근쓰 카드 개수
card_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline()) #구해야 할 카드 개수
request = list(map(int,sys.stdin.readline().split()))

arr = []

for each in request:
    if each in card_list:
        arr.append(1)
    else:
        arr.append(0)

print (*arr)
"""


#시간 초과 (리스트, for문, if문)
"""
N = int(input()) # 상근쓰 카드 개수
card_list = list(map(int,input().split()))

M = int(input()) #구해야 할 카드 개수
request = list(map(int,input().split()))

arr = []

for each in request:
    if each in card_list:
        arr.append(1)
    else:
        arr.append(0)

print (*arr)
"""