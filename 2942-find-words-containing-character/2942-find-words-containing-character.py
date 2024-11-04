class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indx = []
        for i,word in enumerate(words):
            if x in word:
                indx.append(i)
        return indx
        