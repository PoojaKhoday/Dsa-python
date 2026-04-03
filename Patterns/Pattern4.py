class Solution:
    def Pattern3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern3(n)