import operator
from decimal import *

PRECISION = 3


def round_down(x: float) -> int:
    return int(x * 100)


def round_percentage(props: list):
    diff = 100 - sum(props)
    indexed = list(enumerate(props))
    top_diff = sorted(indexed, key=operator.itemgetter(1))[-diff:]
    for item in top_diff:
        props[item[0]] += 1


if __name__ == '__main__':
    getcontext().prec = PRECISION
    rates = [Decimal(input()) for _ in range(int(input()))]
    total = sum(rates)
    proportions = [round_down(rate / total) for rate in rates]
    if sum(proportions) != 100:
        round_percentage(proportions)

    for rate in proportions:
        print('0.{:02}'.format(rate))
