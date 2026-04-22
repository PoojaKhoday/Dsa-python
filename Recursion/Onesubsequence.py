class Solution:
    def SumOfK(self, i, ds, s, arr, target, n):
        if i == n:
            if s == target:
                print(ds)
                return True   # stop further recursion
            return False

        # Take the element
        ds.append(arr[i])
        s += arr[i]
        if self.SumOfK(i + 1, ds, s, arr, target, n):
            return True

        # Not take the element
        ds.pop()
        s -= arr[i]
        if self.SumOfK(i + 1, ds, s, arr, target, n):
            return True

        return False


# Input
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

obj = Solution()
obj.SumOfK(0, [], 0, arr, target, n)