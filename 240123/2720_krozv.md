# 2720. 세탁소 사장 동혁

## Used method & function

unpacking

`divmod(a, b)`

- same as (a // b, a % b)

## 1st

```python

import sys
T = int(input())
for i in range(T):
    cent = int(sys.stdin.readline())
    quarter = cent // 25
    rest_cent = cent - quarter * 25
    dime = rest_cent // 10
    rest_cent -= dime * 10
    nickel = rest_cent // 5
    rest_cent -= nickel * 5
    penny = rest_cent
    print(quarter, dime, nickel, penny)
```

## 2nd

```python
quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())
for _ in range(T):
    change = int(input())
    change_list = [0] * 4
    if change >= quarter:
        change_list[0] = change // quarter
        change %= quarter    
    if change >= dime:
        change_list[1] = change // dime
        change %= dime
    if change >= nickel:
        change_list[2] = change // nickel
        change %= nickel
    if change >= penny:
        change_list[3] = change // penny
        change %= penny
    
    print(*change_list)
```

## 3rd

```python
quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())
for _ in range(T):
    change = int(input())

    q, change = divmod(change, quarter) 
    d, change = divmod(change, dime)
    n, change = divmod(change, nickel)
    p, change = divmod(change, penny)

    print(q, d, n, p)
```