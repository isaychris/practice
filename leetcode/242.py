class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for letter in s:
            dict[letter] = 1
            
        for letter in s:
            dict[letter] += 1
            
        for letter in reversed(s):
            dict[letter] -= 1
            
        for key, value in dict.items():
            if value != 0:
                return False
            
        return True
            
            