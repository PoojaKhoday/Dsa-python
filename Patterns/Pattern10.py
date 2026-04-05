class Solution:
    def Pattern10(self,n):
        for i in range(2*n-1):
            stars = i + 1
            if i >= n:
                stars = 2*n - i - 1
            for j in range(stars):
                print("*", end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern10(n)

