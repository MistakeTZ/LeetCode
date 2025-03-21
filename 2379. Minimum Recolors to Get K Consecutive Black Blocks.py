class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_count = k
        for i in range(0, len(blocks) - k + 1):
            count = blocks[i:i+k].count("W")
            if count < min_count:
                min_count = count
        return min_count

print(Solution().minimumRecolors("BWWWBB", 6))
