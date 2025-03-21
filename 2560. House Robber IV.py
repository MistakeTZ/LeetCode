class Solution(object):
    def minCapability(self, nums, k):
        indices = [i for i, _ in sorted(enumerate(nums), key=lambda x: x[1])]
        length = k

        while True:
            subarr = indices[:length]
            sub_sort = list(subarr)
            sub_sort.sort()
            count = 1

            i = 1
            while i < length:
                if sub_sort[i] - 2 >= sub_sort[i - 1]:
                    count += 1
                    i += 1
                elif i + 1 < length:
                    count += 1
                    i += 2
                else:
                    break

            if count >= k:
                return nums[subarr[-1]]
            length += k - count


print(Solution().minCapability(nums = [4,22,11,14,25], k = 3))
print(Solution().minCapability(nums = [9,6,20,21,8], k = 3))