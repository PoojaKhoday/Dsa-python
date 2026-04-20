def subsequences(arr, index, path):
    if index == len(arr):
        print(path)
        return
    
    # Take element
    path.append(arr[index])
    subsequences(arr, index + 1, path)
    
    # Remove element (backtrack)
    path.pop()
    
    # Not take element
    subsequences(arr, index + 1, path)


# Input
arr = list(map(int, input().split()))

subsequences(arr, 0, [])