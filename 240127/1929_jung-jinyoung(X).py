# 소수 구하기 알고리즘 
# 에라토스테네스의 체

"""
1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)
4. 더 이상 반복할 수 없을 때 까지 2번과 3번의 과정을 반복한다. 
"""


M, N = [int(i) for i in input().split()]

for i in range(M, N+1):
    if i == 2:
            print(2)
    
    elif i ==1 :
        continue

    for num in range(2,int(i**0.5)+1):
        if i % num == 0:
            continue
        else :
            print(i)



