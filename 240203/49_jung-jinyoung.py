class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_anagrams = {} # 해당되는 문자열의 인덱스 저장 딕셔너리

        for word in strs:
            sorted_word = ''.join(sorted(word.lower())) # 정렬 후 연결
            if sorted_word not in my_anagrams.keys(): #키에 없다면
                my_anagrams[sorted_word] = word # value 값 추가
            else:
                my_anagrams[sorted_word] += f',{word}' # ','로 구분하면서 단어 추가
        my_matrix = [group.split(',') for group in my_anagrams.values()]
        # 구분하기 위해 추가했던 ',' 를 기준으로 split -> list화
        # 2차원 배열 생성 
        return(my_matrix)


