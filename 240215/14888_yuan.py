
def f(i, k):
    #k는 i-1까지의 계산값  
    global mx_v, mn_v, op_lst

    if i == N: # N= 숫자 개수 까지만 진행
        mx_v = max(mx_v, k)
        mn_v = min(mn_v, k)
        return

    else:
        # 각각 연산자가 다 떨어질 때 까지 재귀를 통해 결과를 구하기
        # op_lst = +- * / 
        if op_lst[0] > 0:
            op_lst[0] -= 1
            f(i + 1, k + num_lst[i])
            op_lst[0] += 1

        if op_lst[1] > 0:
            op_lst[1] -= 1
            f(i + 1, k - num_lst[i])
            op_lst[1] += 1

        if op_lst[2] > 0:
            op_lst[2] -= 1
            f(i + 1, k * num_lst[i])
            op_lst[2] += 1

        if op_lst[3] > 0:
            op_lst[3] -= 1
            f(i + 1, int(k / num_lst[i]))  # k//num_lst 로 하면 안됨 음수 떄문임
            op_lst[3] += 1

N = int(input())
num_lst = list(map(int, input().split()))
op_lst = list(map(int, input().split()))
mx_v = -1000000000
mn_v = 1000000000

f(1, num_lst[0]) # 첫번째 숫자
print(mx_v)
print(mn_v)



# def f1(i,k): # s는 i-1까지 선택한 합
#     if i==k:
#         global mx_v
#         global mn_v
#         global lst  # 연산자 리스트
#
#         st = []
#         for x in p:
#             st.append(int(x))
#
#         for char in lst:
#             if char == '+':
#                 x = st.pop()
#                 y = st.pop()
#                 st.append(x + y)
#
#             if char == '-':
#                 x = st.pop()
#                 y = st.pop()
#                 st.append(y - x)
#
#             if char == '*':
#                 x = st.pop()
#                 y = st.pop()
#                 st.append(x * y)
#
#             if char == '/':
#                 x = st.pop()
#                 y = st.pop()
#                 st.append(y // x)
#
#         for x in st:
#             if x > mx_v:
#                 mx_v = x
#             elif x < mn_v:
#                 mn_v = x
#
#     else:
#         for j in range(i,k): # p[i]자리에 올 ㅇ원소p[j] 결정
#             p[i] , p[j] = p[j], p[i]
#             f1(i+1,k)
#             p[i], p[j] = p[j], p[i] # 교환 전으로 복구
#
#
# N = int(input())
# p = list(map(int,input().split()))
# n1, n2, n3, n4 = map(int,input().split())
# lst = ['+']* n1 + ['-'] * n2 + ['*']* n3 + ['/']* n4
#
# mx_v = -1000000000
# mn_v = 1000000000
#
# f1(0,N)
# print(mx_v, mn_v)
#
