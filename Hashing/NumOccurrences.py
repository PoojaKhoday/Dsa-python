def frequency_query():
    n = int(input("Enter n: "))
    arr = list(map(int, input("Enter array: ").split()))

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    print("Enter numbers to query (0 to stop):")

    while True:
        number = int(input())
        if number == 0:
            break
        print(freq.get(number, 0))


frequency_query()
#sample input & output
#Enter n: 5
#Enter array: 2 1 2 5 6
#Enter numbers to query (0 to stop):
#5
#1