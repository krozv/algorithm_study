
N = int(input())

def func(k):
    return int(k * (k + 1) / 2) # k번째 줄 가장 끝 수의 순번 함수 

n = 1
while N > func(n):
    n += 1

if n % 2 == 1:
    num_1 = func(n) - N + 1
    num_2 = n - num_1 + 1 # num_1 + num_2 = n+1
else:
    num_2 = func(n) - N + 1
    num_1 = n - num_2 + 1

print(f'{num_1}/{num_2}')



# N = int(input())

# def func(k):
#     return int(k*(k+1)/2)


# n=1

# if N ==1 :
#     print("1/1")
# else:
#     while N > func(n):
#         n+=1
#         if n % 2 == 0:
#             num_1 = 1+func(n)-N
#             num_2 = n+1-num_1
            
#         else :
#             num_1 = n+1-num_2
#             num_2 = 1+func(n)-N
#     print(f'{num_1}/{num_2}')



            

    

# N = int(input())

# def Num(num):
#     return int(num * (num+1) / 2)

# k = 1
# num1=0
# num2=0

# while N > Num(k):
#     s = Num(k)-N
#     num1 = k-s # 감소
#     num2 = s # 증가
#     if k % 2 == 1:
#         print(f'{num1}/{num2}')
#         break        
#     else :
#         print(f'{num2}/{num1}')        
#     k += 1

        
        


# while True:    
#     d = Num(k)-N 
#     num1 = k-d # 분모
#     num2 = 1+d # 분자
#     if N < Num(k):
#         if k % 2 == 1:
#             print(f'{num2}/{num1}')
#             break
#         else :
#             print(f'{num1}/{num2}')
#             break
#     k+=1