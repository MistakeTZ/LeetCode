class Solution(object):
    def minimumCost(self, n, edges, query):
        vertexes = [[i] for i in range(n)]
        weights = [[] for _ in range(n)]
        for edge in edges:
            vertex1, vertex2, weight = edge
            for i in range(len(vertexes)):
                if vertex1 in vertexes[i]:
                    weights[i].append(weight)
                    if not vertex2 in vertexes[i]:
                        for j in range(len(vertexes)):
                            if vertex2 in vertexes[j]:
                                weights[i].extend(weights[j])
                                vertexes[i].extend(vertexes[j])
                                vertexes.pop(j)
                                weights.pop(j)
                                break
                    break
        
        for i in range(len(weights)):
            if not weights[i]:
                weights[i] = -1
                continue
            result = weights[i][0]
            for num in weights[i][1:]:
                result &= num
            weights[i] = result

        res = []
        for line in query:
            for i in range(len(vertexes)):
                if line[0] in vertexes[i]:
                    if line[1] in vertexes[i]:
                        res.append(weights[i])
                    else:
                        res.append(-1)
                    break
        return res


print(Solution().minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(Solution().minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]))
print(Solution().minimumCost(n = 3, edges = [[1,0,4],[0,2,5],[0,2,3],[0,2,14],[0,2,12],[2,0,14],[0,2,4]], query = [[1,2]]))