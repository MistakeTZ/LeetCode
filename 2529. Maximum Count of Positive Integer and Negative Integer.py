class Solution(object):
    def maximumCount(self, nums):
        med = nums[len(nums) // 2]
        if med > 0:
            for i in range(len(nums) // 2, -1, -1):
                if nums[i] <= 0:
                    return len(nums) - i - 1
            return len(nums)
        elif med < 0:
            for i in range(len(nums) // 2, len(nums)):
                if nums[i] >= 0:
                    return i
            return len(nums)
        else:
            return max(len([num for num in nums if num < 0]), len([num for num in nums if num > 0]))
        
print(Solution().maximumCount(nums = [-2,-1,-1,1,2,3]))