class Solution(object):
    def maximumCandies(self, candies, k):
        max_candies = sum(candies) // k
        while max_candies > 0:
            count = 0
            for candy in candies:
                count += candy // max_candies
            if count >= k:
                return max_candies
            max_candies -= 1
        return max_candies
        
print(Solution().maximumCandies(candies = [5,8,6], k = 3))
print(Solution().maximumCandies(candies = [2,5], k = 11))