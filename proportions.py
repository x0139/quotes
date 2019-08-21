from decimal import *

if __name__ == '__main__':
    getcontext().prec = 3
    rates = [Decimal(input()) for _ in range(int(input()))]
    total = sum(rates)
    for rate in rates:
        print(round(rate / total, 3)

