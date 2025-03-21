class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        groups = [1]
        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                groups.append(1)
            else:
                groups[-1] += 1
        if colors[-1] != colors[0]:
            if len(groups) == 1:
                return len(colors)
            groups[0] += groups.pop()
        count = 0
        for group in groups:
            if group >= k:
                count += group - k + 1
        return count
        
print(Solution().numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6))
