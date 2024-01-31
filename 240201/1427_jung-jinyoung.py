"""
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""

#카운팅 정렬 사용

numbers = input() #입력된 수
N = len(numbers) # 리스트 항목 개수
K = 11 # 더미 값 +1 생성
counts = [0] * 11  # 빈 count 행렬 생성

for number in numbers:
    counts[int(number)] +=1 # 각 숫자의 개수를 구함

result = []

i = K-1 # 뒤에서 부터 탐색하기 위한 현재 위치 설정
while i >=0:
    if counts[i]: # 개수가 있을 경우
        result.append(i)
        counts[i] -= 1
    else:
        i-=1

print(*result,sep='')



