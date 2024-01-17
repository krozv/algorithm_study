word = input().upper()
alphabet = list(set(word))

alpa_list = []
for i in alphabet:
    number = word.count(i)
    alpa_list.append(number)
    
if alpa_list.count(max(alpa_list)) > 1:
    print('?')
else:
    max_index = alpa_list.index(max(alpa_list))
    print(alphabet[max_index])