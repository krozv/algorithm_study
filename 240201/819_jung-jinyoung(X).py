"""
input
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

"""
"""
output
"ball"

"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        self.paragraph = paragraph.split()
        str_list = list()
        for char in self.paragraph:
            if char.isalpha :
                str_list.append(char.lower())
        self.banned_word = banned

        for banned_word in self.banned_word:
            for i in range(self.paragraph.count(banned_word)):
                self.paragraph.removed(banned_word)

        return self.paragraph



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

sol = Solution()
sol.mostCommonWord(paragraph,banned)
print(paragraph)