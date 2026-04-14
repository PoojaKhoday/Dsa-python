class Solution:
    def printNumbers(self,i, n):
        if i<1:
            return
        self.printNumbers(i-1,n)
        print(i)
        
n = int(input("Enter number of times: "))
obj = Solution()
obj.printNumbers(n,n)      