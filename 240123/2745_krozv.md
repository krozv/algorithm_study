# 2745. 진법 변환

## Used method & function

`ord(c)`

유니코드 문자를 나타내는 문자열이 주어지면 해당 문자의 유니코드 코드 포인트를 나타내는 정수를 돌려줌

```python
result = ord('A')
print(result) # 65
```

`chr(i)`

유니코드 코드 포인트가 정수i인 문자를 나타내는 문자열을 돌려줌

`ord(c)`의 반대

```python
result = chr(65)
print(result) # 'A'
```

`enumerate(iterable, start=0)`

index와 value 반환

`isalpha()`

문자열이 모두 알파벳으로 이루어졌을 경우 `True` 반환

## 1st

메모리: 31252 KB

시간: 44 ms

```python
N, B = input().split()
N = list(N)
B = int(B)

str_data = []
i = 0
for i in range(36):
    if i <= 9:
        str_data.append('')
    else:
        str_data.append(chr(i+55))
    i += 1

num = 0
output = 0
for i in range(len(N)):
    if N[i] in str_data:
        num = str_data.index(N[i]) * (B ** (len(N)-i-1))
    else:
        num = int(N[i]) * (B ** (len(N)-i-1))
    output += num

print(output)
```

## 2nd

메모리: 31252 KB

시간: 40 ms

```python

N, B = input().split()
N = list(N)
N.reverse()
B = int(B)

sum = 0
alp_list = [chr(i) for i in range(65, 91)]

for i, elem in enumerate (N):
    if elem.isalpha():
        sum += (ord(elem) - 55) * (B**i)
    else:
        sum += int(elem) * (B**i)
print(sum)
```