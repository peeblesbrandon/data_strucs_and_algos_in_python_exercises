class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        N = 1 << A
        output = []
        for i in range(N):
            code = i ^ (i >> 1)
            output.append(code)
        return output


mySolution = Solution()
print(mySolution.grayCode(4))
