class Solution:
        def NnumbersSum(self,i,sum):
            if i<1:
                print(sum)
                return
            self.NnumbersSum(i-1,sum+i)
n = int(input())  
obj = Solution()
obj.NnumbersSum(n,0)
