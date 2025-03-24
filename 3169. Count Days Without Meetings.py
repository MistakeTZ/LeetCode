class Solution(object):
    def countDays(self, days, meetings):

        meetings.sort(key = lambda x: x[0])
        
        i = 1
        while i < len(meetings):
            if meetings[i][0] <= meetings[i - 1][1]:
                meetings[i - 1][1] = max(meetings[i - 1][1], meetings[i][1])
                meetings.pop(i)
            else:
                i += 1
        
        count = sum([meeting[1] - meeting[0] + 1 for meeting in meetings])
        return days - count
        
print(Solution().countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(Solution().countDays(days = 5, meetings = [[2,4],[1,3]]))