# coding:utf-8
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dict = set(wordList)
        
        distance = 0
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                
                for next_word in self.get_nextwords(word):
                    if next_word in visited or next_word not in dict:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
            
        return 0
    def get_nextwords(self,word):
        words = []
        for i in range(len(word)):
            left, right = word[:i],word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                words.append(left+char+right)
        return words
        