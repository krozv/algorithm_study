T = int(input())
for _ in range(T):
  case = int(input())
  input_list = list(map(int, input().split()))
  list_zero = [0 for i in range(101)]
  
  for i in input_list:
      if list_zero[i] != 0:
          list_zero[i] += 1
      else:
          list_zero[i] = 1
  # print(list_zero)
  list_zero.reverse()
  print(f'#{case} {100 - list_zero.index(max(list_zero))}')
