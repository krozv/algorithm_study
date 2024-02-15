'''
쇠막대기와 레이저
의 밀당
'''


T = int(input())
for tc in range(1, T+1):
    stick = input()

    num_list = []
    sum = 0

    for i in range(1, len(stick)):
        if stick[i] == '(' and stick[i-1] == '(':       # (( 연달아 나오는 경우, 앞의 '('이 쇠막대기의 시작임. (쇠막대기 1개)
            num_list.append(1)
        elif stick[i] == ')' and stick[i-1] == '(':     # () 인 경우, 레이저므로 앞에 놓여져 있던 철근을 잘라 2개가 됨
            for j in range(len(num_list)):
                num_list[j] += 1
        elif stick[i] == ')' and stick[i-1] == ')':     # )) 인 경우, 쇠막대기의 끝이므로, 쇠막대기를 하나 없애고 그 개수를 sum 에 더함
            sum += num_list.pop()

    print(f'#{tc} {sum}')