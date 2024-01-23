N = int(input())

n=0
while N > 3*n*(n+1)+1:           
    n+=1
print(n+1)


# n = 0 
# while True:    
#     if N == 1:
#         print(1)
#         break
#     if  3*3*(n-1)+1 < N < 3*n*(n+1)+1:
#         print(n+1)
#         break
#     n += 1




"""
N = int(input())  # 값 입력

def hex_make(n):
    return 3*n*(n-1)+1

# n번째 방의 범위 (hex_make(n)-6n, hex_make(n)+1)

# A가 범위에 있을 경우 count 출력
# 범위 설정을 위한 조건문 작성

n = 1


while N != 0:
    if N == hex_make(n):
        print(n)
        break
    elif N >=hex_make(n):
        if N < hex_make(n+1):
            print(n+1)
            break
    n += 1
"""

#시간초과 
"""    

N = int(input())  # 값 입력

def hex_make(n):
    return 3*n*(n-1)+1

# n번째 방의 범위 (hex_make(n)-6n, hex_make(n)+1)

# A가 범위에 있을 경우 count 출력
# 범위 설정을 위한 조건문 작성

n = 1
while N != 0:
    if N == hex_make(n):
        print(n)
        n+=1
    elif N >=hex_make(n):
        if N < hex_make(n+1):
            print(n+1)
            break
    n += 1"""

"""
#시간 초과
N = int(input())  # 값 입력

def hex_make(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result = 6 * i + result

    return result

# n번째 방의 범위 (hex_make(n)-6n, hex_make(n)+1)

# A가 범위에 있을 경우 count 출력
# 범위 설정을 위한 조건문 작성

n = 1
while N <= 10e8:
    if N <= hex_make(n):
        if N > hex_make(n - 1):
            print(n+1)
            break
    n += 1


"""



#런타임 에러
"""
N = int(input())  # 값 입력

def hex_make(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1

    return 6 * n + hex_make(n - 1)  # n번째 방 최댓값

# n번째 방의 범위 (hex_make(n)-6n, hex_make(n)+1)

# A가 범위에 있을 경우 count 출력
# 범위 설정을 위한 조건문 작성

n = 1
while N <= 10e8:
    if N <= hex_make(n):
        if N > hex_make(n - 1):
            print(n+1)
            break
    n += 1

# N = int(input()) # 값 입력 
"""