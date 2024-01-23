N ,b = input().split()
b = int(b)

result = 0
power = 0

# N의 자리가 0과 9사이일때는 바로 int 형변환 해서 사용
# 그렇지않으면 ord 로 바꿈

for char in reversed(N):
    digit = int(char) if '0' <= char <= '9' else ord(char) - ord('A') + 10
    result += digit * power  # 자리 수에 따라 power 에 b(진법)을 계속 곱해줌 
    power *= b 

print(result)




# A의 순서 사용
# def char_to_digit(char):
#     if '0' <= char <= '9':
#         return int(char)
#     else:
#         return ord(char) - ord('A') + 10

# N = input()
# b = int(input())

# result = 0
# power = 0

# for i in reversed(N):
#     result += char_to_digit(i) * (b ** power)
#     power += 1

# print(result)



# 딕셔너리와 인덱스 모두 사용

# N ,b = input().split()
# b = int(b)

# number_dict = {char : idx for idx, char in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

# result = 0
# power = 0

# for char in reversed(N):
#     result += number_dict[char] * (b**power)
#     power += 1 

# print(result)


# 인덱스 사용

# N ,b = input().split()
# b = int(b)

# number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# result = 0
# power = 0

# for i in reversed(N):
#     sum = number.index(i) * (b ** power)
#     power += 1
#     result += sum

# print(result)



# 딕셔너리 사용

# N ,b = input().split()
# b = int(b)
#
# new_list = N[::-1]  # 한 글자씩 거꾸로 list
#
# dict_alpha = {}
# for i in range(26):
#     key = chr(ord('A') + i)     # 알파벳 A부터 Z까지 순서대로 키 생성
#     value = 10 + i              # 10부터 35까지의 값을 값으로 사용
#     dict_alpha[key] = value
#
# sum = 0
#
# for idx, char in enumerate(new_list):
#     if char.isalpha():
#         numb = (b ** idx) * dict_alpha[char]  # new_list 가 알파벳이면 키 값 불러와서 계산
#         sum += numb
#
#     else:
#         numb = (b ** idx) * char   # new_list 가 숫자면 바로 계산
#         sum += numb
#
# print(sum)



