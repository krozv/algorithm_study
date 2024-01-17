Words = list(input().upper())

dict = {}
for i in Words:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1

max_value = max(dict.values())
max_keys = [key for key, value in dict.items() if value == max_value]

if len(max_keys) >1:
    print("?")
else: 
    print(max_keys[0])