class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurance = {}
        
        for num in nums:
            if num not in occurance:
                occurance[num] = 1
            else:
                occurance[num] += 1
                
        for key, value in occurance.items():
            if value == 1:
                return key
        