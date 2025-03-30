from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = [-1]
        for i, char in enumerate(s):
            last_index = s.rindex(char)
            if i > parts[-1]:
                parts.append(last_index)
            elif last_index > parts[-1]:
                parts[-1] = last_index
        
        parts = [parts[i + 1] - parts[i] for i in range(len(parts) - 1)]
        return parts


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))