word = input().upper()

word_set = set(word)
word_list = sorted(list(word_set))
my_len = len(word_list)

word_count = {}
for i in range(my_len):
  request = word_list[i]
  word_count[request] = word.count(request)

# result_1 = word_count
# max_value = max(result_1.values())
# result_2 = result_1.keys(max_value)
# print(result_1.keys())
# print(max_value)

result = max(word_count, key=word_count.get)  #빈도수 중 최댓값에 해당하는 key값을 반환

#중복이 있다면 '?'출력
max_value = max(word_count.values())
value_list = list(word_count.values())

if value_list.count(max_value) != 1:
  print("?")
else:
  print(result)