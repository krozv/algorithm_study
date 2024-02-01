class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 특수문자열 제거
        x = "!?',;."
        for i in x:
            if i in paragraph:
                paragraph = paragraph.replace(i, '')

                # 단어 단위로 스플릿
        word_list = paragraph.split()

        # ban 단어가 아닐떄만 딕셔너리에 넣음
        word_dict = {}
        for word in word_list:
            wordl = word.lower()
            if wordl not in banned:
                if wordl not in word_dict:
                    word_dict[wordl] = 1
                else:
                    word_dict[wordl] += 1

        # max value 값에 대한 키 도출
        max_value = max([value for value in word_dict.values()])
        key = [key for key, value in word_dict.items() if value == max_value]

        for x in key:
            return x


x = Solution
x.mostCommonWord(Self, paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                 banned=["hit"])