class Solution(object):
    def minZeroArray(self, nums, queries):
        k = 0
        for query in queries:
            if not any(nums):
                return k
            max_in_range = min(max(nums[query[0]:query[1] + 1]), query[2])
            query.extend([max_in_range, []])
            for i in range(query[0], query[1] + 1):
                if nums[i] - max_in_range >= 0:
                    nums[i] -= max_in_range
                    query[-1].append(i)
                elif nums[i] != 0:
                    dif = nums[i]
                    for que in queries[:k]:
                        if que[3] - dif > 0:
                            for num in que[-1]:
                                num 
                        print(que)

            k += 1
        return -1
        
print(Solution().minZeroArray(nums = [2,0,2], queries = [[0,2,1], [0,2,1], [1,1,3]]))
print(Solution().minZeroArray(nums = [4,3,2,1], queries = [[1,3,2], [0,2,1]]))
print(Solution().minZeroArray(nums = [6,2], queries = [[0,0,5],[0,1,4],[1,1,1],[1,1,2],[1,1,4],[0,0,1],[0,0,2],[0,1,1],[1,1,4],[1,1,3],[1,1,5],[1,1,1],[0,1,1],[1,1,4],[0,0,3]]))