for N in range(int(raw_input())):
    Splittee = raw_input()
    print '{Even} {Odd}'.format(Even=Splittee[::2], Odd=Splittee[1::2])

