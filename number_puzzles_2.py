def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def reverse(n):
    r = 0
    while n:
        r = 10 * r + n % 10
        n //= 10
    return r

def solve_one():
    for i in range(10, 57):
        if sum_digits(i) > 10:
            print i

def solve_two():
    for i in range(10, 100):
        if i - reverse(i) == sum_digits(i):
            print i

def check(answer):
    while answer != '1' and answer != '2':
        if answer == '3':
            exit(0)
        print "I am sorry, I don't understand. [1/2/3]"
        answer = raw_input('> ')

def choose(choice):
    check(choice)
    if choice == '1':
        print ""
        solve_one()
    if choice == '2':
        print ""
        solve_two()

def menu():
    while True: 
        print "1) Find two digit numbers <= 56 with sums of digits > 10"
        print "2) Find two digit number minus number reversed which equals sum of digits"
        print "3) Quit\n"
        choose(raw_input('> '))
        print ""
    
if __name__ == '__main__':
    menu()
