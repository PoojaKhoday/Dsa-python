def character_hashing():
    s = input("Enter string: ")

    freq = {}

    # character hashing
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    print("Enter characters to query (0 to stop):")

    while True:
        ch = input()

        if ch == "0":
            break

        print(freq.get(ch, 0))

character_hashing()

#sample input and output
#Enter string: banana\
#Enter characters to query (0 to stop):
#a
#3
#n
#2
#b
#1
#x
#0