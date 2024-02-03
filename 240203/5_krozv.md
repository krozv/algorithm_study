# 5
```python
# 5. Longest Palindrome Substring
"""
1 <= s.length <= 1000
s is digit and english letters
"""
class LongestPalindromeSubstring:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        # plan
        # int(str_len/2)+1 개수의 단어를 반대로 뒤집어가면서 일치하는 지 파악
        # 있을 경우 break
        # 없을 경우 개수 1개씩 줄여가면서 슬라이싱
        a = 0
        b = 1
        for i in range(round(str_len/2+0.1), 0, -1):
            # print(round(str_len/2+0.1))
            # print(a, b)
            # print(a==b)
            if a == b:
                # print(a, b)
                break
            for j in range(str_len-i-1):
                # print(str_len-i-1)
                # print(i, s[j:j + i], s[j + i:j + 2 * i] )
                if i == 1 or i % 2 == 0:
                    if s[j:j + i] == s[j + i:j + 2 * i]:
                        a = s[j:j + i]
                        b = s[j + i:j + 2 * i]
                        print(a, b)
                        break
                else:
                    if s[j:j + i] == s[j + i - 1:j + 2 * i - 1]:
                        a = s[j:j + i]
                        b = s[j + i - 1:j + 2 * i - 1]
                        print(a, b)
                        break
                # else: # 짝수
                #     if s[j:j + i] == s[j + i:j + 2 * i]:
                #         a = s[j:j + i]
                #         b = s[j + i:j + 2 * i]
                #         print(a, b)
                #         break
                # print(i, j)
                # # print(str_len-i-1)
                # print(j, j+i, j+i-1, j+2*i-1)
                # # print(s[j:j+i+1],  s[j+i:j+2*i+1])
                # # print(s[j:j+i] == s[j+i-1:j+2*i-1])
                # if s[j:j+i] == s[j+i-1:j+2*i-1]:
                #     a = s[j:j+i]
                #     b = s[j+i-1:j+2*i-1]
                #     print(a, b)
                #     break
        return a



c = LongestPalindromeSubstring()
input1 = "babab"
input2 = "cbb"
print(c.longestPalindrome(input1))
print(c.longestPalindrome(input2))

```