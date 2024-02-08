def push(item):
    stack.append(item)
    return stack
def pop():
    stack.pop()
    return stack

while True:
    str_input = input()
    # 입력 받은 문자가 없을 경우
    if str_input == '.':
        break
    check = '([])'
    end_point = '.'

    N = len(str_input)
    stack = []
    idx_list1 = [] # '[' 인덱스 저장
    idx_list2 = [] # '(' 인덱스 저장
    for i in range(N):
        char = str_input[i]
        if char in check[:2]:
            push(char)
            if char == '(':
                idx_list2.append(i)
            else:
                idx_list1.append(i)

        elif char in check[2:]:
            # empty stack
            if len(stack) == 0 :
                print('no')
                break

            if char == check[2]: # ']'
                # not a pair
                if stack[-1] == '(':
                    print('no')
                    break
                check1 = idx_list1[-1]  # '[~]'사이 확인하기 위한 인덱스 확인
                len1 = len(str_input[check1:i+1]) # '[~]'사이 개수 확인
                # pair but not a balance
                if len1 == 0:
                    print('no')
                    break
                else:
                    pop()
            else:
                # not a pair
                if stack[-1] == '[':
                    print('no')
                    break
                check2 = idx_list2[-1] # '(~)'사이 확인하기 위한 인덱스 확인
                len2 = len(str_input[check2:i+1]) # '(~)'사이에 개수 확인
                # pair but not a balance
                if len2 == 0:
                    print('no')
                    break
                else:
                    pop()


    #마지막 인덱스에서 결과 확인
    else:
        if len(stack)==0 and str_input[-1] == '.':
            print('yes')
        #overflow
        else :
            print('no')

