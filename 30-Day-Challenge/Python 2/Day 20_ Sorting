
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
swaps = 0
Check = True
while Check == True:
    internal_swaps = 0 
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swaps += 1
            internal_swaps += 1
    
    if internal_swaps == 0:
        Check = False

print 'Array is sorted in {} swaps.'.format(swaps)
print 'First Element: {}'.format(a[0])
print 'Last Element: {}'.format(a[-1])
