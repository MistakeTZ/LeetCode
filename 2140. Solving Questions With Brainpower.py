from typing import List

class Solution1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        costs = [0] * n
        maxim = [0, 0]

        for i in range(n):
            if maxim[1] <= i:
                costs[i] = questions[i][0] + maxim[0]
            else:
                costs[i] += questions[i][0]
            end_in = questions[i][1] + i + 1

            if costs[i] > maxim[0] and end_in < n:
                maxim[0] = costs[i]
                maxim[1] = end_in

            else:
                for j in range(end_in, min(maxim[1], n)):
                    if costs[j] < costs[i]:
                        costs[j] = costs[i]
        return max(costs)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        costs = [0] * n
        maxim = [0, 0]

        for i in range(n):
            costs[i] += questions[i][0]
            end_in = questions[i][1] + i + 1

            if costs[i] > maxim[0]:
                maxim[0] = costs[i]
                maxim[1] = end_in

                for j in range(end_in, n):
                    costs[j] = costs[i]
            else:
                for j in range(end_in, min(maxim[1], n)):
                    if costs[j] < costs[i]:
                        costs[j] = costs[i]
        return max(costs)


print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
print(Solution().mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))