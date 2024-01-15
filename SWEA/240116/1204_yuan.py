#1204. 

def number(scores):
    dic = {}
    for i in scores:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_value = max(dic.values())
    max_keys = [key for key, value in dic.items() if value == max_value]
    return max(max_keys)

Test_case = int(input())
trial = 1
while trial <= Test_case:
    Test_case_number = int(input())
    scores = input().split()
    print('#'+str(trial)+" "+number(scores))
    trial += 1 