class Solution(object):
    def countCompleteComponents(self, n, edges):
        counts = [[] for _ in range(n)]
        for edge in edges:
            counts[edge[0]].append(edge[1])
            counts[edge[1]].append(edge[0])
        print(counts)

        count = 0
        used_edges = []
        i = 0

        while i < n:
            if i in used_edges:
                i += 1
                continue
            used_edges.append(i)

            if len(counts[i]) == 0:
                count += 1
                i += 1

            elif len(counts[i]) == 2:
                start_num = i
                ind = i
                num = counts[i][1]
                
                while True:
                    used_edges.append(num)
                    if len(counts[ind]) == 1:
                        num = counts[i][0]
                        ind = start_num
                        while True:
                            used_edges.append(num)
                            if len(counts[ind]) == 1:
                                break
                            else:
                                if ind == counts[num][1]:
                                    ind = num
                                    num = counts[num][0]
                                else:
                                    ind = num
                                    num = counts[num][1]
                        break
                    else:
                        if ind == counts[num][1]:
                            ind = num
                            num = counts[num][0]
                        else:
                            ind = num
                            num = counts[num][1]
                        
                        if num == start_num:
                            count += 1
                            break

            elif len(counts[i]) == 1:
                num = counts[i][0]
                used_edges.append(i)
                used_edges.append(num)
                if len(counts[num]) == 1:
                    count += 1
                    break

                else:
                    ind = i
                    while True:
                        used_edges.append(num)
                        if len(counts[num]) == 1:
                            break
                        else:
                            if ind == counts[num][1]:
                                ind = num
                                num = counts[num][0]
                            else:
                                ind = num
                                num = counts[num][1]

        return count

        
print(Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))