from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
        for i in range(half):
            total = nums.count(nums[i])
            if total <= half:
                continue
            maxim = nums[i]
            count = 0
            for j in range(i, n - 1):
                if nums[j] == maxim:
                    count += 1
                    if count * 2 > j + 1:
                        if (total - count) * 2 > n - j - 1:
                            return j
            
            return -1
        return -1
        
print(Solution().minimumIndex([1,2,2,2]))
print(Solution().minimumIndex([2,1,3,1,1,1,7,1,2,1]))
print(Solution().minimumIndex([3,3,3,3,7,2,2]))