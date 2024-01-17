T = int(input())
for case in range(1, T + 1):
    case_num = int(input())
    score = list(map(int, input().split()))
    sort = sorted(score)
    count = 0
    most = 0
    
    for i in range(0, len(score)-1):
        if sort[i] == sort[i+1]:
            count += 1
        else:
            if most < count:
                most = count
                most_num = []
                most_num.append(sort[i])
            if most == count:
                most_num.append(sort[i])
            count = 0
            
    print(f'#{case_num} {max(most_num)}')
