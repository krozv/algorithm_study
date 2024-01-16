t = int(input())

for i in range (t):
    testCase = list(map(int, input().split()))
    output = 0
    for j in range(len(testCase)):
        if testCase[j] % 2 == 1:
            output += testCase[j]
    print(f'#{i+1} {output}')
