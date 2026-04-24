class Solution:
    def SumOfK(self, i, ds, s, arr, target, n):
        if i == n:
            if s == target:
                print(ds)
                return True  
            return False

        ds.append(arr[i])
        s += arr[i]
        if self.SumOfK(i + 1, ds, s, arr, target, n):
            return True

        ds.pop()
        s -= arr[i]
        if self.SumOfK(i + 1, ds, s, arr, target, n):
            return True

        return False

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

obj = Solution()
obj.SumOfK(0, [], 0, arr, target, n)

#sample input/output
#5
#1 2 3 4 5
#2
#[2]