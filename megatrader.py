import itertools
from typing import Tuple, Iterable, NamedTuple


class Quote(NamedTuple):
    day: int
    name: str
    price: float
    quantity: int
    income: float
    source: str

    def __str__(self):
        return self.source

    def __radd__(self, other):
        return other + self.income


class MaxBuyFilter:
    def __init__(self, money):
        self.money = money

    def predicate(self, items) -> bool:
        total = sum([item.price * item.quantity for item in items])
        return total <= self.money


def parse_input(source: str, days: int) -> Tuple[int, str, float, int]:
    splitted = source.split()
    day = int(splitted[0])
    name = splitted[1]
    price = float(splitted[2]) * 10
    quantity = int(splitted[3])
    income = quantity * (-price + 1000 + 30 + (days - day))
    return Quote(day, name, price, quantity, income, source)


def get_inside_data(days: int) -> list:
    data = []
    source = input()
    while source:
        stock = parse_input(source, days)
        data.append(stock)
        source = input()
    return data


def make_combinations(data: list) -> Iterable:
    """
    original from python itertools recipes, function powerset()
    https://docs.python.org/3/library/itertools.html
    :param data: list
    :return: Iterable
    """
    return itertools.chain.from_iterable(itertools.combinations(data, r) for r in range(1, len(data) + 1))


def calculate_max_profix(filtred: Iterable) -> Tuple[float, Iterable]:
    maximum, result_item = 0, None
    for item in filtred:
        item_income = sum(item)
        maximum = max(item_income, maximum)
        if maximum == item_income:
            result_item = item

    return maximum, result_item


if __name__ == '__main__':
    days, lots, money = map(int, input().split())
    data = get_inside_data(days)
    combinations = make_combinations(data)
    filtred = filter(MaxBuyFilter(money).predicate, combinations)

    max_income, stocks = calculate_max_profix(filtred)
    print(max_income, *stocks, sep='\n')
