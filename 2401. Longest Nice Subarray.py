class Solution(object):
    def longestNiceSubarray(self, nums):
        max_lenght = 1
        for i in range(len(nums) - 1):
            num = nums[i]
            lenght = 1
            for j in range(i + 1, len(nums)):
                if num & nums[j] == 0:
                    num |= nums[j]
                    lenght += 1
                else:
                    break
            if lenght > max_lenght:
                max_lenght = lenght
        return max_lenght

        
print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))