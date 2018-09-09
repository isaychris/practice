class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}

        for letter in s:
            if letter not in map:
                map[letter] = 1
            else:
                map[letter] += 1

        for i, letter in enumerate(s):
            if map[letter] == 1:
                return i

        return -1
        
        
        