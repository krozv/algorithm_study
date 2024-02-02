

### 첫 성공 방법
90ms
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for s in strs:
            if word_dict.get(''.join(sorted(s))) == None:
                word_dict[''.join(sorted(s))] = list()
                word_dict[''.join(sorted(s))].append(s)
            else:
                word_dict[''.join(sorted(s))].append(s)
        #print([*word_dict.values()])
        return [*word_dict.values()]
```
문자열을 sorted() 사용해 정렬하면 리스트로 출력값 나옴..
```python
s= 'eat'
print(sorted(s))
#['a', 'e', 't']
```
그래서 `''.join(sorted(s))` 사용


### 답지..

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
```