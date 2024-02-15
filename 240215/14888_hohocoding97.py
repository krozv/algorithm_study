def dfs(i, r): #r은 i-1번째의 계산결과
    global add, sub, mul, div, max_result, min_result
    if i == N:
        if max_result < r:
            max_result = r
        if min_result > r:
            min_result = r
    else:
        if add > 0:
            add -= 1
            dfs(i+1, r + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, r - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, r * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            if r >= 0:
                dfs(i+1, int(r//nums[i]))
            else:
                dfs(i+1, -int((-r)//nums[i]))
            div += 1
    



N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div  = map(int, input().split())      # +, -, *, / 의 개수
max_result = -1000000000
min_result = 1000000000
dfs(1,nums[0])

print(max_result)
print(min_result)

