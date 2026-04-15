class Solution:
    #def NnumbersSum(self, N):
        #your code goes here
        def NnumbersSum(self,N):
            if N==0:
                return 0
            return N + self.NnumbersSum(N-1)
N = int(input())  
obj = Solution()
print(obj.NnumbersSum(N))
