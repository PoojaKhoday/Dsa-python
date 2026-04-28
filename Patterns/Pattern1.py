class Solution:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*" , end = "")
            print()
n = int(input())            
obj = Solution()
obj.pattern1(n)                

#sample input & output
#5
#*****
#*****
#*****
#*****
#*****
