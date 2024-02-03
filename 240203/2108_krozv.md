# 2108 통계학

## Condition

산술평균 - 평균

중앙값 - 중앙에 위치한 값

최빈값 - 가장 많이 나타난 값

범위 - 최댓값 - 최솟값

N 수의 개수 1<=N<=500,000, N은 홀수

num_list 입력

정수의 절댓값은 4,000을 넘지 않음 -4001<N<4001

## Solution

### 1st - selection sort

Timeout

```python
# 2108 통계학
N = int(input())
num_list = [int(input()) for _ in range(N)]
count = [0] * N
# 필요한 값 - 총합, 변수개수(=N), max_value, min_value, max_count
# 정렬 후 중앙에 위치한 값?
# 1. 정렬을 함 -> 선택정렬? 시도해봐야지
for i in range(N-1):
    max_idx = i
    for j in range(i+1, N):
        if num_list[max_idx] < num_list[j]:
            max_idx = j
    num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]

# 최댓값, 최솟값, 중앙값
max_num = num_list[0]
min_num = num_list[-1]
cen_num = num_list[N//2]

# 산술평균 구하기 위해서 합이랑, 정수개수 구하기
cnt = [0] * 8001
sum_num = 0
for i in range(N):
    sum_num += num_list[i]
    cnt[num_list[i]+4000] += 1
max_cnt = 0

# 가장 많이 나타난 정수의 개수는?
for i in range(8001):
    if max_cnt < cnt[i]:
        max_cnt = cnt[i]

# 최빈값 구하기
frequency = 0
frequently_num = 0
for i in range(8001):
    if max_cnt == cnt[i]:
        frequently_num = i-4000
        frequency += 1
        if frequency == 2:
            break

# 출력함
print('{:.0f}'.format(sum_num/N))
print(cen_num)
print(frequently_num)
print(max_num - min_num)

```

### 2nd - counting sort

Wrong

```python
# 2108 통계학
import sys
input = sys.stdin.readline
N = int(input())
num_list = [int(input()) for _ in range(N)]
# counting sort
# counting sort를 위해 num_list 내 숫자와 동일한 인덱스의 값을 1씩 증가
count = [0] * 8001
total = 0   # 총합을 구하기 위한 변수
max_cnt = 0 # 최빈수 구하기 위한 변수
for i in range(N):
    count[num_list[i]+4000] += 1
    total += num_list[i]
    if max_cnt < count[num_list[i]+4000]:
        max_cnt = count[num_list[i]+4000]
# counting sort하면서 최빈수 구하기
frq = 0
frq_num = 0
# count의 누적합을 구함
for i in range(1, 8001):
    if count[i] == max_cnt and frq < 2:
        frq_num = i-4000
        frq += 1
    count[i] += count[i-1]

# 누적합을 기준으로 정렬
sorted_num_list = [0] * N
for num in num_list:
    if count[num+4000] != 0:
        sorted_num_list[count[num+4000]-1] = num
        count[num+4000] -= 1

max_num = sorted_num_list[-1]   # 최댓값
min_num = sorted_num_list[0]    # 최솟값

print(round(total/N))           # 산술평균
print(sorted_num_list[N//2])    # 중앙값
print(frq_num)                  # 최빈값
print(max_num - min_num)        # 범위
```

산술평균 시 음수 반올림이 문제인 것으로 사료됨

### python `round()` floating point error

python에서 `rount()`를 사용할 때 고질적인 문제임

일반적으로 우리가 아는 반올림은 '사사오입'을 이용하는 데에 반해,

해당 method는 '오사오입'을 사용함

```python
반올림 예제 적기
```

### Answer