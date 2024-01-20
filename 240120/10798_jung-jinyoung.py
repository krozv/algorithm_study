
# 입력받은 다섯 개의 문자열을 저장한 리스트를 생성
words_list=[]
for a in range(5):
    word = input()
    words_list.append(word) # 입력받은 각 단어들을 리스트에 추가

result="" # 세로로 읽을 값을 저장할 변수 설정

#문자열 중 가장 긴 길이를 구함
#구하지 않고 바로 for문을 써서 error 발생했음

max_len = max(len(word) for word in words_list)
for i in range(max_len):
    #다섯 개의 문자열을 세로로 읽어서 result에 추가
    for j in range(5):
        # 현재 단어의 길이가 i보다 큰 경우에만 추가
        if i < len(words_list[j]):
            result += words_list[j][i]

print(result)

