from decimal import *

PRECISION = 3

if __name__ == '__main__':
    getcontext().prec = PRECISION
    rates = [Decimal(input()) for _ in range(int(input()))]
    total = sum(rates)
    for rate in rates:
        print(round(rate / total, PRECISION)

