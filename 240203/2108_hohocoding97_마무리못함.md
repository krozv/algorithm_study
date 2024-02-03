import sys
input = sys.stdin.readline

counts = [0]*8001 #-4000~4000 카운팅
N = int(input())
sum = 0
num_set = set() #주어진 수들을 하나씩만 담은 세트

for i in range(N):
    counts[int(input())+4000] += 1 #-4000이 counts의 index로는 0 이므로
    sum += i
    num_set.add(i)

average = round(sum/N) #첫째자리에서 반올림한 값

#최빈값 찾기
mode = 0 #최빈값
max_count = 0 #최빈값의 카운트
for num in num_set:


