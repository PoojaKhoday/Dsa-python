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

#Sample input & output
#Pooja
#Pooja
#Pooj
#Pooa
#Poo
#Poja
#Poj
#Poa
#Po
#Poja
#Poj
#Poa
#Po
#Pja
#Pj
#Pa
#P
#ooja
#ooj
#ooa
#oo
#oja
#oj
#oa
#o
#oja
#oj
#oa
#o
#ja
#j
#a
