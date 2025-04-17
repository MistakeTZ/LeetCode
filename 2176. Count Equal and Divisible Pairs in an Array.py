from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        i = 0
        arr = sorted(enumerate(nums), key=lambda x:x[1])

        while i < n - 1:
            indexies = [arr[i][0]]

            for j in range(i + 1, n):
                if arr[j][1] == arr[i][1]:
                    indexies.append(arr[j][0])
                else:
                    i = j
                    break
            inds = len(indexies)

            for m in range(inds):
                delimeter = indexies[m] % k
                if delimeter == 0:
                    count += len(indexies) - m - 1
                    continue
                else:
                    for b in range(m + 1, len(indexies)):
                        if (indexies[b] * indexies[m]) % k == 0:
                            count += 1
            if j + 1 == n:
                break
        
        return count


print(Solution().countPairs(nums = [3,1,2,2,2,1,3], k = 2))
print(Solution().countPairs(nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], k = 7))
print(Solution().countPairs(nums = [10,2,3,4,9,6,3,10,3,6,3,9,1], k = 4))
print(Solution().countPairs(nums = [1,2,3,4], k = 1))