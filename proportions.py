def calculate_rates(rate: float, total: float, precision: int = 3):
    return round(rate / total, precision)


if __name__ == '__main__':
    rates = [float(input()) for _ in range(int(input()))]
    total = sum(rates)
    for rate in rates:
        print(calculate_rates(rate, total))
