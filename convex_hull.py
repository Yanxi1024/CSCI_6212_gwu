import random

class Solution:
    def operation(self, convex_hull, start: int, end: int):
        if end - start < 3:
            return convex_hull[start:end + 1]
        mid = int((start + end) / 2)
        left_part = self.operation(convex_hull, start, mid)
        right_part = self.operation(convex_hull, mid + 1, end)
        return self.combine(left_part, right_part)
    
    def combine(self, left_part, right_part):
        convex_hull = left_part + right_part
        convex_hull.sort()
        
        def crossPro(p, o, q):
            x1, y1 = p
            x2, y2 = o
            x3, y3 = q
            return (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1)
        
        upper_boundery, lower_boundery  = [], []
        
        for point in convex_hull:
            while len(upper_boundery) >= 2 and crossPro(upper_boundery[-2], upper_boundery[-1], point) > 0:
                upper_boundery.pop()
            while len(lower_boundery) >= 2 and crossPro(lower_boundery[-2], lower_boundery[-1], point) < 0:
                lower_boundery.pop()
            
            lower_boundery.append(tuple(point))
            upper_boundery.append(tuple(point))   
        
        res = map(list, list(set(lower_boundery + upper_boundery)))
        return list(res)
            
    def convexSolution(self, convex_hull):
        print("-----------------------------------------------------------------------------------------------------------------------")

        res = self.operation(convex_hull, 0, len(convex_hull) - 1)
        print(res)

def generatePoints(num: int):
    # This func generate a point list, num is the length of the point list. 
    # This func is used for testing the excutive time
    res = list()
    for i in range(int(num / 2)):
        res.append([i, random.randint(0, 5)])
        res.append([i, random.randint(6, 10)])
    return res

def main():
    solution = Solution()
    
    # points = [[3,5],[0,0],[0,2],[6,2]]
    # solution.convexSolution(points)
    points = [[3,5],[0,0],[0,2],[6,2],[1,2],[2,2],[3,2],[3,1],[3,0]]
    solution.convexSolution(points)
    # points = [[3,5],[0,0],[0,2],[6,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[4,3],[3,3],[4,2],[5,7]]
    # solution.convexSolution(points)
    # points = [[3,5],[0,0],[0,2],[6,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[4,3],[3,3],[4,2],[5,7],[7,5],[7,1],[8,2],[8,3]]
    # solution.convexSolution(points)
    # points = [[3,5],[0,0],[0,2],[6,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[4,3],[3,3],[4,2],[5,7],[7,5],[7,1],[8,2],[8,3],[9,3],[9,4],[10,7],[11,2]]
    # solution.convexSolution(points)


if __name__ == '__main__':
    main()
    

        