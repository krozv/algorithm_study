# A진법과 B진법 A, B
# A진법 자리수 a 자리수
# A진법 m개 숫자 digit_list

#10진법 나타내기:


A, B = list(map(int,input().split()))
a = int(input())
digit_list = list(map(int,input().split()))

digit_list.reverse()

power = 0
sum= 0

for i in digit_list:       
    sum += i * (A ** power)    
    power += 1

result_list = []

if sum < B:
    print(sum)
else:
    while sum >= B:
        k,v = divmod(sum, B)
        result_list.append(v)
        sum = k

result_list.reverse()
print(k, *result_list)

