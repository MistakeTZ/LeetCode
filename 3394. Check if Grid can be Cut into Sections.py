class Solution(object):
    def checkValidCuts(self, n, rectangles):
        xs = []
        ys = []

        count = len(rectangles)

        for x1, y1, x2, y2 in rectangles:
            xs.append([x1, x2])
            ys.append([y1, y2])
            
        xs.sort(key=lambda x: x[0])
        ys.sort(key=lambda y: y[0])

        can_horizontal = False
        horizontals = []
        started = []
        
        for i in range(count):
            x = xs[i][0]
            j = 0
            while j < len(started):
                if xs[started[j]][1] <= x:
                    started.pop(j)
                else:
                    j += 1
            
            if j == 0:
                if can_horizontal:
                    can_horizontal = False
                    horizontals.append(x)

            started.append(i)
            for j in range(i + 1, count):
                if xs[j][0] == x:
                    started.append(j)
                else:
                    break

            if not can_horizontal:
                can_horizontal = True

        can_vertical = False
        verticals = []
        started = []
        
        for i in range(count):
            y = ys[i][0]
            j = 0
            while j < len(started):
                if ys[started[j]][1] <= y:
                    started.pop(j)
                else:
                    j += 1
            
            if j == 0:
                if can_vertical:
                    can_vertical = False
                    verticals.append(y)

            started.append(i)
            for j in range(i + 1, count):
                if ys[j][0] == y:
                    started.append(j)
                else:
                    break

            if not can_vertical:
                can_vertical = True
        
        if len(horizontals) >= 2 or len(verticals) >= 2:
            return True
        return False


print(Solution().checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(Solution().checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(Solution().checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))