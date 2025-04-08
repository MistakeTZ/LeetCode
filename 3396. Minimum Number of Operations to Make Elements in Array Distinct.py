from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] in nums[i + 1:]:
                return i // 3 + 1
        return 0


print(Solution().minimumOperations([1,2,3,4,2,3,3,5,7]))
print(Solution().minimumOperations([4,5,6,4,4]))
print(Solution().minimumOperations([6,7,8,9]))