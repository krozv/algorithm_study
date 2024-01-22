# 1193. 분수찾기

## Used method & function

## 1st

```python
X = int(input())

order = True
i = 0
total = 0

while order:
    i = i + 1
    total = total + i
    if total >= X:
        order = False

# 분모 + 분자 = total = i + 1
if i % 2 == 1:
    a = 1
    b = i
    # 분자 감소, 분모 증가
    for j in range(total-X):
        a = a + 1
        b = b - 1
else:
    a = i
    b = 1
    # 분자 증가, 분모 감소
    for j in range(total-X):
        a = a - 1
        b = b + 1
    
print(f"{a}/{b}")
```

## 2nd

```python
X = int(input())

# x가 row번째 줄, X번째에 위치함
for row in range(1, X+1):
    if X <= row:
        break
    X -= row

# row 번째 줄에서 numerator + denominator = row + 1
# 짝수번째 줄은 numerator 커짐
# 홀수번째 줄은 denominator 커짐

# row가 홀수라면
if row % 2 == 1:
    numerator = row + 1 - X
    denominator = X
# row가 짝수라면
else:
    numerator = X
    denominator = row + 1 - X

print(f'{numerator}/{denominator}')
```