class Solution:
    def reverse(self,arr,i,n):
        def helper(i):
            if i>=n//2:
                return
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
            helper(i+1)
        helper(i)    
n = int(input())       
arr = list(map(int,input().split()))
obj = Solution()
obj.reverse(arr,0,n)   
print(arr) #print(*arr)