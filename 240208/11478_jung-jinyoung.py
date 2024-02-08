str_input = input()
N = len(str_input)
count = 0 # 부분 문자열 개수
sub_str = {}

# 길이가 1인 부분 문자열 추가
for i in range(1, N+1):
    sub_str[i]= set() # value 값을 빈 set로 설정
    for j in range(0,N-i+1):
        sub_str[i].add(str_input[j:j+i])
    count += len(sub_str[i]) # set의 길이 추가

print(count)