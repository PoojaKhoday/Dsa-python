class Solution:
    def Pattern11(self,n):
        for i in range(1,n+1):
            #num
            for j in range(1, i+1):
                print(j, end = " ")
            #space
            for j in range(4 * (n - i)):
                print(" ", end = "")
                j = -2
            #num
            for j in range(i,0,-1):
                print(j, end = " ")
            print()
n = int(input()) 
obj = Solution()
obj.Pattern11(n)                   

                    