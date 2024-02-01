class Solution:
    def reorderLogFiles(self, logs):
        let_list = []
        dig_list = []

        for log in logs:
            if 'let' not in log:
                dig_list.append(log)
            else:
                let_list.append(log)

        #label 제외한 부분부터 기준 삼아서 sort
        def function(s):
            return s[4:]

        letlist_sort = sorted(let_list, key= function)

        # 기존의 dig리스트를 추가
        letlist_sort.extend(dig_list)


answer = Solution()
answer.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])




# 구버전
# class Solution:
#     def reorderLogFiles(self, logs: list[str]):
#
#         let_list = []
#         dig_list = []
#
#         # let과 dig 분리
#         for i in logs:
#             split = i.split()
#             if 'let' in split[0]:
#                 let_list.append(i)
#             else:
#                 dig_list.append(i)
#
#         print(dig_list)
#
#         # str[0]을 키, str[1:] 을 value
#         str_dict = {}
#         for str in let_list:
#             str_split = str.split()
#
#             str_dict.setdefault(str_split[0], str_split[1:])
#
#         # value리스트를 만들어서 밸류를 sort, 단 나중에 insert로 넣을거기떄문에 reverse
#         value_list = sorted([value for key, value in str_dict.items()], reverse=True)
#         print(value_list)
#
#         # sort한 밸류의 key만 따로 저장
#         ordered_let_list = []
#         for i in value_list:
#             for key, value in str_dict.items():
#                 if i == value:
#                     ordered_let_list.append(key)
#         print(ordered_let_list)
#
#         #저장한 키를 가진 문자열 불러와서 dig_list 에 맨 앞부터 넣음
#         for key in ordered_let_list:
#             for j in let_list:
#                 if key in j:
#                     dig_list.insert(0,j)
#
#         print(dig_list)
#
#
#
# log = Solution
# log.reorderLogFiles(log, logs =["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
