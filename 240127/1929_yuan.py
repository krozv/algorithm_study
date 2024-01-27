N,M = list(map(int,input().split()))


for numb in range(N,M+1):
    if numb == 1:
        continue

    for divisor in range(2,int(numb**0.5) + 1):
        if numb % divisor == 0:
            break

    else:
        print(numb)






# N,M = list(map(int,input().split()))


# for numb in range(N,M+1):
#     divisible = False 

#     for divisor in range(2,M):
#         if numb // divisor !=1 and numb % divisor == 0:
#             divisible = True
#             break

#     if divisible == False:
#         print(numb)

