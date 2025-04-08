from typing import List
import numpy as np

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        summ = summ // 2

        np_nums = np.array(nums)
        sorted_indices = np_nums.argsort()

        def recursive_sum(i, current_sum):
            num = nums[sorted_indices[i]]
            print(num, current_sum)
            if current_sum == num:
                return True
            if current_sum < num:
                return recursive_sum(i + 1, current_sum)
            if i == len(nums) - 1:
                return False

            return recursive_sum(i + 1, current_sum - num) or recursive_sum(i + 1, current_sum)

        return recursive_sum(0, summ)


# print(Solution().canPartition([1,5,11,5]))
# print(Solution().canPartition([1,2,3,5]))
print(Solution().canPartition([1,2,5]))