class Solution:
    def romanToInt(self, s):
        lookup = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}

        result, prev = 0, 0

        for letter in reversed(s):
            number = lookup[letter]

            if number >= prev:
                result += number
            else:
                result -= number

            prev = number
        return result