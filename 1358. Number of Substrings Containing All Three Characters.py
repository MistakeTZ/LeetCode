class Solution(object):
    def numberOfSubstrings(self, s: str):
        signs = {}
        reverse = s[::-1]
        for sign in "abc":
            ind = s.find(sign)
            if ind == -1:
                return 0
            signs[sign] = [ind, len(s) - reverse.find(sign) - 1]
        max_first = max([value[0] for value in signs.values()])
        min_last = min([value[1] for value in signs.values()])
        print(signs, max_first, min_last)
        
print(Solution().numberOfSubstrings("abcabc"))
print(Solution().numberOfSubstrings("aaacb"))
print(Solution().numberOfSubstrings("abc"))