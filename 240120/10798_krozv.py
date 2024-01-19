# 세로읽기
import sys

data1 = []
for i in range(5):
    data1.append(list(sys.stdin.readline()))

# input에서 문자열'\n'제거 및 가장 긴 단어의 문자 개수 파악
list_len = []
for i in range(len(data1)):
    while data1[i].count('\n') > 0:
        data1[i].remove('\n')
    list_len.append(len(data1[i]))

# 가장 긴 문자 개수를 기준으로 공백 리스트 채워 넣음
for i in range(len(data1)):
    while len(data1[i]) < max(list_len):
        data1[i].append(' ')

# 세로로 읽되, 공백은 읽지 않음
output = []

for i in range(max(list_len)):
    for j in range(len(data1)):
        if data1[j][i] != ' ':
            output.append(data1[j][i])

print(''.join(output))