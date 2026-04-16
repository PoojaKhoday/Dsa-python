class Solution:
    def reverse(self,l, r):
        if l>=r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        self.reverse(l+1,r-1)
n = int(input())       
arr = list(map(int,input().split()))
obj = Solution()
obj.reverse(0,n-1)   
print(arr) #print(*arr)