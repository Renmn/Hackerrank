    n = int(raw_input())
    list_repr = []
    while n != 0:
        list_repr.append(n%2)
        n = n/2
    binary = list_repr[::-1]

    longest = 0
    current = 0
    for num in binary:
        if num == 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 0

    print max(longest, current)
