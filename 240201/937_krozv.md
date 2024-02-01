```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # dictionary로 만들어서 숫자 세야징
        word = ''
        data = []
        # 문자가 영어로 구성되어있을 경우, lower case로 변환 후 저장
        for char in paragraph:
            if char.isalpha():
                char = char.lower()
                word += char
            else:
                if word != '':
                    data.append(word)
                word = ''
        data.append(word)
        # 단어의 출현 개수를 dictionary를 이용하여 count
        word_dict = {}
        for word in data:
            if word in banned:
                pass
            elif word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        # most common word 탐색
        max_value = 0
        most_common_word = ''
        for key, value in word_dict.items():
            if max_value < value:
                max_value = value
                most_common_word = key
        return most_common_word
```