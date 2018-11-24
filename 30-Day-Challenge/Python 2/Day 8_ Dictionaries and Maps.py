phoneBook = {}
for i in range(int(raw_input())):
    kv_pair = raw_input().split()
    phoneBook[kv_pair[0]] = kv_pair[1]

while True: 
    query = raw_input()
    if query in phoneBook:
        print '{query}={number}'.format(query=query, number = phoneBook[query])
    else:
        print 'Not found'
