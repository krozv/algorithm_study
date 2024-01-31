#해당 개수 만큼 프린트하는 코드 작성 구조 공부
import sys
N = int(sys.stdin.readline())  # 입력될 정수의 총 개수
count = [0] * 10001  # 더미 값 +1

for _ in range(N):
    number = int(sys.stdin.readline())
    count[number] += 1 #각 숫자의 개수 만큼 값 증가

for i in range(10001): #오름차순 조건문 작성
    for j in range(count[i]): # 해당 개수 만큼
        print(i) #해당 정수 프린트