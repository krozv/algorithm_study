N = int(input())

my_dict = {}
total = 0
cnt = N//2
number_list = []
for j in range(N):
    number = int(input())
    total += number # 합
    number_list.append(number) # 중간 인덱스를 찾기 위한 리스트 추가

    #최빈수를 위한 개수 새는 딕셔너리 조건문
    if number not in my_dict.keys():
        my_dict[number] = 1
    else:
        my_dict[number] +=1

number_list.sort() # 중앙값을 찾기 위한 정렬

print(round(total/N)) # 1. 산술 평균
print(number_list[cnt]) # 2. 중앙값

# 3. 최빈수
sorted_list = sorted(my_dict, key=lambda x :(-my_dict[x], x))
# value 값으로 정렬한 후 key 값으로 정렬 (빈수가 같을 경우 key값으로 정렬)
if N >1: # 개수가 1개 이상일 때
    max_frequency = []
    max_freq = 0
    if sorted_list[0] != sorted_list[-1]: # 입력값이 2개 이상일 때
        for k, v in my_dict.items():
            if v > max_freq:
                max_freq = v
        for k, v in my_dict.items():
            if v == max_freq:
                max_frequency.append(k)
    if max_frequency[0] != max_frequency[-1]:  # key 값이 여러개일 경우
            print(sorted(max_frequency)[1])  # 두번째로 작은 최빈값
    else:  # 오직 하나의 key값이 있을 경우
            print(sorted_list[0])  # 최빈수가 한개일 경우 그 숫자 출력
else: # 개수가 1개일 때
    print(sorted_list[0])

# 4. 범위
max_number = max(number_list)
min_number = min(number_list)
print(max_number - min_number)
