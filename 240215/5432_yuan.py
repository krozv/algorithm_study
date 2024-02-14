T = int(input())
for tc in range(1, T + 1):
    lst = input()
    lst = lst.replace('()', '*', 50000)

    # *이 나올떄 * 이전까지의 괄호 개수 세고 다시 처음부터 시작
    total = 0
    st = []
    for char in lst:
        if char == '(':
            st.append(char)

        elif char == ')': # 닫는 괄호 나오면 팝
            st.pop()
            total +=1 #쇠막대기 한번당 자르는 번수 +1 이라서 +1

        else: # 레이저 나올떄 이전까지 쇠막대기 개수(여는 괄호개수)더하기
            total += len(st)

    print(f'#{tc} {total}')


# T = int(input())
# for tc in range(1, T + 1):
#     lst = input()
#     lst = lst.replace('()', '*', 50000)
#
#     # () 괄호 사이의 *레이저 개수 세기
#     total = 0
#     st = []
#     l_cnt = 0  # 레이저 개수
#     for char in lst:
#
#         if char == ')':
#             while st[-1] != '(':
#                 st.pop()  # 레이저 뺴면서 레이저 개수 세줌
#                 l_cnt += 1
#             total += l_cnt + 1  # 조각은 자른거보다 한개 더 많음
#             st.pop()  # (도 없애줌
#             st.extend(['*'] * l_cnt)  # 다시 레이저 넣어줌
#             l_cnt = 0  # 레이저 개수 초기화
#
#         else:
#             st.append(char)
#
#     print(f'#{tc} {total}')