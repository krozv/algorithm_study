# 49. Group Anagrams

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