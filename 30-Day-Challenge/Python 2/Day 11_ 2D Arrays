if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    holder = [arr[x][j:j+3] for j in range(0,4) for n in range(0,4) for x in range(n, n+3)]
#This line is slightly obtuse, but what it does is extract each line of each 3x3 square that #contains an hour glass, so there are 48 rows (lists) in the holder list corresponding to each
#of the three lines of each 16 hour glasses yielding 16 * 3
    
    next = [sum(holder[n:n+3], []) for n in range(0,len(holder),3)]
#This concatenates each of the 3 rows of each hour glass into one list
    
    for item in next:
        item.pop(3)
        item.pop(4)
#Removes the values corresponding to the two extra entries in the hour glass
    
    final = [sum(glass) for glass in next]
    print max(final)
