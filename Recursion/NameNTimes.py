class Solution:
    def printNumbers(self,i,n,name):
        if i>n:
            return
        print(name)
        self.printNumbers(i+1, n,name)
    
n  = int(input("Enter number of times:"))
name  = input("Enter name:")
obj = Solution()
obj.printNumbers(1,n,name)