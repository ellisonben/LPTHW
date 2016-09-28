def sum_cubed_digits(n):
    s = 0
    while n:
        s += (n % 10) ** 3
        n //= 10
    return s

def armstrong_check(n):
    if n == sum_cubed_digits(n):
        print n

def solve(range):
    for i in range:
        armstrong_check(i)

if __name__ == '__main__':
    solve(range(100,1000))
