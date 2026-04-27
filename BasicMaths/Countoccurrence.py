class Solution:
    def countoccurrence(self,number, arr):
        cnt = 0
        for i in range (len(arr)):
            if arr[i] == number:
                cnt=cnt+1
        return cnt
n = int(input())
number = int(input())
arr = list(map(int,input().split()))
obj = Solution()
result = obj.countoccurrence(number,arr)
print(result)

#Sample input & output
