# 11576. Base Conversion
실버 5

### 코드
```python
A, B = map(int, input().split())
input()
digit_values = list(map(int, input().split()))
digit_values.reverse()#편한 계산을 위해 리스트 뒤집기

converted_decimal = 0
for i,value in enumerate(digit_values):
    #각 자리의 값을 10진수로 변환해서 모두 더하기
    converted_decimal += value* (A**i) 

# print(converted_decimal)

i=0
while True:
    if B**i<= converted_decimal < B**(i+1):
        break
    else:
        i = i + 1

while i>= 0:
    q,r = divmod(converted_decimal, B**i)
    print(q,end=' ')
    converted_decimal = r
    i = i - 1
```