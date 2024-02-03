# 49. Group Anagrams

## 1st 

Runtime: 93 ms

Memory:20.4 MB

주어진 strs에서 char를 `ord()`를 사용하여 아스키코드로 변경한 후 아스키코드의 집합을 튜플 형식으로 dictionary 키로 저장

```python
# 49. Group Anagrams
class GroupAnagrams:
    def groupAnagrams(self, strs:[str]) -> [[str]]:
        strs.sort()
        num_list = [0] * len(strs)
        for i in range(len(strs)):
            num_list[i] = tuple(sorted(list(map(lambda x: ord(x), strs[i]))))
        anagram = {}
        for i in range(len(strs)):
            key = num_list[i]
            # anagram dict에 key가 없을 경우
            if not anagram.get(key):
                anagram[key] = [strs[i]]
            # key가 있을 경우
            else:
                anagram[key].append(strs[i])
        anagram_list = []
        for value in anagram.values():
            anagram_list.append(value)
        return anagram_list


c = GroupAnagrams()
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(c.groupAnagrams(word_list))
```

## 2nd

Runtime: 88 ms

Memory:20.5 MB

`append()` 말고 결합 연산자 `+`를 사용해봄

-> 사용결과 runtime이 5ms 감소함

```python
# 49. Group Anagrams
class GroupAnagrams:
    def groupAnagrams(self, strs:[str]) -> [[str]]:
        strs.sort()
        num_list = [0] * len(strs)
        for i in range(len(strs)):
            num_list[i] = tuple(sorted(list(map(lambda x: ord(x), strs[i]))))
        anagram = {}
        for i in range(len(strs)):
            key = num_list[i]
            # anagram dict에 key가 없을 경우
            if not anagram.get(key):
                anagram[key] = [strs[i]]    
            # key가 있을 경우
            else:
                anagram[key] += [strs[i]]   # append method 사용 안하고 결합 연산자 + 사용 변경
        anagram_list = []
        for value in anagram.values():
            anagram_list += [value]
        return anagram_list


c = GroupAnagrams()
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(c.groupAnagrams(word_list))
```