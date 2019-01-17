# coding:utf-8
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        
        distant = 0
        visited = set([start])
        
        while queue:
            distant += 1 
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distant
                
                for next_word in self.get_next_words(word):
                    if next_word in visited or next_word not in dict:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
                    
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
