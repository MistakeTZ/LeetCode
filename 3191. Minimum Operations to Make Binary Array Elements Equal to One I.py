class Solution(object):
    def minOperations(self, nums):
        count = 0
        for i in range(len(nums) - 2):
            if not nums[i]:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
        if nums.count(0):
            return -1
        return count

        
print(Solution().minOperations([0,1,1,1,0,0]))
print(Solution().minOperations([0,1,1,1]))
print(Solution().minOperations([1,0,0,1,1,0,1,1,1,0,0,0,1,0,1]))