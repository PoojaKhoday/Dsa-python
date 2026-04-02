class Solution:
    def Pattern3(self, n):
        for i in range(n):
            for j in range(1, i+2):
                print(j, end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern3(n)
