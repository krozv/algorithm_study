#### 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

```python
T = int(input().strip())
for test_case in range(1,T+1):
    t = int(input().strip())
    student_score = list(map(int, input().split()))
    score_list = list(set(student_score))
    score_list.sort()
    student_score_count = []
    for i in score_list:
        student_score_count.append(student_score.count(i))
    student_score_count = student_score_count[::-1]
    num = len(student_score_count)-1-student_score_count.index(max(student_score_count))
    print(f'#{t} {score_list[num]}')
```



#### 2072. 홀수만 구하기

```python
T = int(input())
for test_case in range(1,T+1):
    sum_odd_num = 0
    num_list = list(map(int, input().split()))
    for i in num_list:
        if i %2 == 1:
            sum_odd_num += i
    print(f'#{test_case} {sum_odd_num}')
```

#### 2063. 중간값 찾기

```python
N = int(input())
N_array = list(map(int, input().split()))
N_array.sort()
print(N_array[N//2])
```
