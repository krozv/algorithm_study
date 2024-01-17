alphabet = list(input())

# input의 알파벳을 전부 large로 변경
alphabet = [i.upper() for i in alphabet]
alphabet.sort()
used_alphabet = list(set(alphabet))

# 알파벳마다 사용횟수 count_input 리스트에 작성
count_input = []
for i in used_alphabet:
    count_input.append(alphabet.count(i))
Max_alphabet = max(count_input)

# output
if count_input.count(Max_alphabet) > 1:
    print('?')
else:
    print(used_alphabet[count_input.index(Max_alphabet)])
