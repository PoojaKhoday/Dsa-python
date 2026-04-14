class Solution:
    def printNumbers(self,i, n):
        if i==0:
            return
        print(i)
        self.printNumbers(i-1,n)
        
n = int(input("Enter number of times: "))
obj = Solution()
obj.printNumbers(n,n)      