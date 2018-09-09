class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for num in nums:
            if seen.get(num) == True:
                return True
            else:
                seen[num] = 1
                
        return False