'''
21789. 도키도키 간식드리미

주어지는 수열
간식은 번호 순서대로 받아야 한다.
한 명씩 설 수 있는 여유 공간
수열의 사람들이 한 명씩 여유 공간에 들어갈 수 있지만,
다시 원래 줄에 설 수는 없다.
'''


def can_i_eat_snack(array):
    stack = []      # 여유 공간을 stack 으로 정의
    top = -1
    finish = 1      # 간식을 받은 사람의 순서를 저장해 줄 finish 변수를 정의

    while array != []:      # 먼저 처음 줄을 비운다.
        if array[0] == finish:      # 처음 줄의 첫 번째 사람이 간식을 받을 차례면 바로 간식을 제공
            array.pop(0)
            finish += 1
        elif top != -1 and stack[top] == finish:    # 여유 공간의 제일 앞 사람이 간식을 받을 차례면 간식을 제공
            stack.pop(top)
            top -= 1
            finish += 1
        else:       # 위의 두 경우 모두 아니면 처음 줄의 첫 사람을 여유 공간의 제일 앞 자리로 배치
            stack.append(array[0])
            top += 1
            array.pop(0)

    while stack != [] and stack[top] == finish:     # 처음 줄을 다 비우고 여유 공간의 사람들에게 간식을 나눠줘본다.
        stack.pop(top)
        top -= 1
        finish += 1

    if finish == N + 1:     # 만약 모든 사람에게 간식을 나눠준 경우 'Nice'를 출력
        print('Nice')

    else:       # 실패한 경우 'Sad'를 출력
        print('Sad')


N = int(input())
arr = list(map(int, input().split()))
can_i_eat_snack(arr)