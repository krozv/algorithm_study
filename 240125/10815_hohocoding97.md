# 10815. 숫자 카드

### 최근방법
시간 : 716ms
```python
import sys
#상근이가 가지고 있는 숫자카드
N = int(sys.stdin.readline())
sangeun_cards_list = list(map(int,sys.stdin.readline().split()))

#상근이가 가지고 있는지 아닌지 확인해야할 숫자 카드
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

sangeun_cards_dict = dict()
for i in sangeun_cards_list:
    sangeun_cards_dict[i] = 0

for i in M_list:
    if sangeun_cards_dict.get(i) == None:
        print('0',end=' ')
    else:
        print('1',end=' ')
```
상근이가 가지고 있는 숫자카드를 딕셔너리(sangeun_cards_dict)로 만들었음

```python
for i in M_list:
    if sangeun_cards_dict.get(i) == None:
        print('0',end=' ')
    else:
        print('1',end=' ')
```
`dict.get(i)`에서 i가 없을 경우 None을 반환하는 것을 이용해 문제를 품


### 이전 방법
시간초과
```python
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for M_element in M_list:
    if M_element in N_list:
        print(1, end=' ')
    else:
        print(0,end=' ')
```