def subsequences(s, index, path):
    if index == len(s):
        print(path)
        return
    
    # Take character
    subsequences(s, index + 1, path + s[index])
    
    # Not take character
    subsequences(s, index + 1, path)


# Input
s = input().strip()

subsequences(s, 0, "")