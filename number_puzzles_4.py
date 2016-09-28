for a in range(1, 42):
    for b in range(1, 42):
        for c in range(1, 42):
            for d in range(1, 42):
                if a+b+c+d == 45 and (a+2 == b-2 == c*2 == d/2) and d%2 == 0:
                    print a
                    print b
                    print c
                    print d
                    print ""
