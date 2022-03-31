class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_lan = {}
        
        for i, ali in enumerate(order):
            i = str(i+1) # i가 0부터 시작하면 "aa", "a" 비교 안된다
            if len(i) == 1:
                i = '0' + i
            dict_lan[ali] = i

        new_words = []

        for word in words:
            for key, value in dict_lan.items():
                word = word.replace(key, value)
                if value == '26':
                    new_words.append(word)

        n_max = max([len(word) for word in new_words])
        new_words_int = [int(word.ljust(n_max, '0')) for word in new_words]

        new_words_int_ori = new_words_int.copy()
        new_words_int.sort()
        
        return new_words_int_ori ==  new_words_int