# 2164. 카드2
### 코드
240ms
```python
from collections import deque
N = int(input()) #카드 장수 입력
cards = deque(range(1,N+1))

while N>1:
    up_card = cards.popleft() #왼쪽에서 카드 꺼내기. 왼쪽이 위라 생각
    N -= 1
    if N == 1:
        break
    up_card = cards.popleft()
    cards.append(up_card) #왼쪽에서 꺼낸 카드를 오른쪽에 넣기
print(cards[0])
```

### 주연이꺼 보고 다시 푼 코드
228ms
```python
from collections import deque
N = int(input()) #카드 장수 입력
cards = deque(range(1,N+1))

while N>1:
    up_card = cards.popleft() #왼쪽에서 카드 꺼내기. 왼쪽이 위라 생각
    N -= 1
    cards.append(cards.popleft()) #왼쪽에서 꺼낸 카드를 오른쪽에 넣기
print(cards[0])
```
