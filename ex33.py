numbers = []

def while_list(end, incr):
    i = 0
    while i < end:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += incr
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def for_list(end, incr):
    
    for i in range(0, end, incr):
        print "At the top i is %d" % i
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
while_list(9, 3)
for_list(9, 3)
    
print "The numbers: "

for num in numbers:
    print num
