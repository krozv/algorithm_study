딕셔너리를 정렬할 때는 sorted 함수를 사용함

sorted 함수에 정렬 판단 기준을 입력하고, 정렬을 오름차순으로 할지 내림차순으로 할지 설정할 수 있음

```python
my_dict = {'a': 'hojun', 'c' : 'youtube', 'k' : 'anything'}
print(sorted(my_dict))
#key를 기준으로 key를 정렬
#['a', 'c', 'k']

print(sorted(my_dict, key = my_dict.get))
#value를 기준으로 key를 정렬
#['k','a','c']

print(sorted(my_dict.values()))
#value들을 정렬
#['anything', 'hojun', 'youtube']

print(sorted)
```

#### 성공 코드

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list, letter_list = [], []
        for log in logs:
            split_log = log.split(maxsplit = 1)
            if split_log[1][0].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        letter_list.sort(key = lambda log: (log.split()[1:], log.split()[0]))

        return letter_list + digit_list
```


#### 실패 코드 1
65개 중 63개 통과
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list, letter_list = [], []
        for log in logs:
            split_log = log.split(maxsplit = 1)
            if split_log[1][0].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        letter_list.sort(key = lambda log: log.split()[1:])

        return letter_list + digit_list
        
```


#### 실패 코드
65개 테스트 코드 중 57개만 통과....

이유 : 식별자가 같은 상황이 있어서 딕셔너리 사용시 문제 발생...
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_dict = {}
        let_dict = {}
        dig_key_list = []
        for log in logs:
            k,v = log.split(maxsplit = 1) #첫번째 공백에서만 자르기
            if v[0].isdigit():
                dig_dict[k] = v 
                dig_key_list.append(k)
                dig
            else:
                let_dict[k] = v
        
        #let_dict를 value를 기준으로 정렬
        sorted_let_keys = sorted(let_dict, key=let_dict.get)

        sorted_list = []
        for let_key in sorted_let_keys:
            sorted_list.append(f"{let_key} {let_dict[let_key]}")
        
        #dig_dict는 입력된 순서대로 정렬되야 해
        for dig_key in dig_key_list:
            sorted_list.append(f"{dig_key} {dig_dict[dig_key]}")
        print(sorted_list)
        return sorted_list
```


