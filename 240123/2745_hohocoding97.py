b, n = input().split()
b_list = list(b)
alpha_list = [chr(a) for a in range(65,91)]

b_list.reverse()
result = 0
for i, v in enumerate(b_list):
    if v.isalpha(): #만약 알파벳이라면?
        result += (alpha_list.index(v) + 10) * (int(n)**i)
    else: #숫자인 경우
        result += int(v) * (int(n)**i)
print(result)