class Solution:
    def printNumbers(self, n):
        if n==0:
            return
        self.printNumbers(n-1)
        print(n)
n = int(input("Enter number of times: "))
obj = Solution()
obj.printNumbers(n) 

#input & output
#Enter number of times: 4
#1
#2
#3
#4