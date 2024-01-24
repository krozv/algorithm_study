"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""
"""
예제 입력 : 
4
1 3 5 7

결과 : 
3

"""

N = int(input())

#(1)원하는 과정 : 입력받은 숫자들 중 소수가 아닌 정수를 제거한다
#(2)제거한다 -> 입력받은 정수 전체 개수에서 소수가 아닌 정수의 개수를 뺀다.

numbers = list(map(int,input().split()))
count = 0 # 소수가 아닌 개수

for num in numbers:
    if num == 1:
        count +=1
        continue #1은 소인수가 아니다

    if num == 2:
        continue #최소 소수 
    
    for n in range(2,num):
        if num % n == 0:
            count +=1
            break 
        

result = N - count # 입력한 숫자들 중 소수가 아닌 것들을 제외
print(result)
