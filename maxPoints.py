import math
import json

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        if len(A) != len(B):
            return 0
        points = {}
        max_points = 0
        for i in range(len(A)):
            print(points)
            p2 = (A[i], B[i])
            if p2 in points:
                for slope in points[p2]:
                    points[p2][slope] += 1

                    # update max
                    max_points = max(points[p2][slope], max_points)
                    print(points)
            else:
                for p1 in points:
                    slope_num = p2[1] - p1[1]
                    slope_den = p1[0] - p1[0]

                    # calculate slope
                    if slope_den == 0:
                        slope = "vert"
                    else:
                        GCD = math.gcd(slope_num, slope_den)
                        slope = str(slope_num / GCD) + "/" + \
                            str(slope_den / GCD)

                    # increment slope counter for that point
                    if slope in points[p1]:
                        points[p1][slope] += 1
                    else:
                        points[p1][slope] = 1

                    # update max
                    max_points = max(points[p1][slope], max_points)
                    print(points)
                points[p2] = {}
        return max_points + 1


mySolution = Solution()
X = [1, 2, -1, 4, 4, 3, 0, 0]
Y = [1, 2, -1, 1, 4, 2, 1, 1]
print(mySolution.maxPoints(X, Y))

