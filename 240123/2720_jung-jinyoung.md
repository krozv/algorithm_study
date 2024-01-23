## Try
```python
T = int(input()) #테스트 케이스 개수

for _ in range(T):
  case = int(input()) #거스름돈 입력
  C = case/100 #단위가 센트이기 때문에 달러로 계산 
    #C의 타입은 현재 float
    #자리 나눠서 계산
 
  if C >= 1 :
    a = C//1
    b = (C-a) 
    
    Q = int((a) // 0.25)
    D = int(b // 0.1)
    c = round(C-a-(D*0.1),2)
  
    if c < 0.05:a
        N = 0
        P = int(c // 0.01)
    else:
        N = 1
        P = int((c - 0.05) // 0.01)

  elif C >=0.5:
    Q = 2
    R = C-0.5
    D = int(R // 0.1)
    c = round(R - (D*0.1),2)
    if c < 0.05:
      N = 0
      P = int(c // 0.01)
    else:
      N = 1
      P = int((c - 0.05) // 0.01)
  else :
    Q = 1
    R = C-0.25
    D = int(R // 0.1)
    c = round(R-(D*0.1),2)
    if c < 0.05:
      N = 0
      P = int(c // 0.01)
    else:
      N = 1
      P = int((c - 0.05) // 0.01)
  
  print(min(Q,D,N,P))
```
#### 문제점
- 데이터 타입이 모두 float이라는 점 *(입력 조건에서 정수로 설정되었으나, 인지 못함)*
- 부동 소수점 문제 : round로 해결
- `C/1`로 인하여 0.25 쿼터의 개수를 구하는데 문제 발생 
  ```python
    C = 194 
    Q,D,N,P = 4, 9, 0, 4 #원하는 결과 값은 7 1 1 4
  ```


---
---

## Solve

  ```python
  T = int(input("테스트 케이스 개수를 입력하세요: "))

  coins = [25,10,5,1]

  for i in coins :
    c = int(input()) # 정수 거스름돈 (입력 설정)
    rest = [] # 거스름돈 리스트
    for i in coins:
        rest.append(c//i) #값이 큰 동전 순서로 몫 구하기
        c = c % i #나머지 구하기
    print (*rest) # '*'괄호 없이 출력
      
  ```

- int로 해결 : 부동소수점 문제 X
- 몫과 나머지로 해결할 수 있었음
- print 함수 사용시 `*`: 괄호 없이 출력 가능 