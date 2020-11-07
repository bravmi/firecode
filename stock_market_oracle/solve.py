from ..utils import *


def max_profit(prices):
    prices.append(float('-inf'))

    sequences = []
    seq = []
    for x, y in zip(prices, prices[1:]):
        seq.append(x)
        if x > y:
            sequences.append(seq)
            seq = []

    ans = sum(seq[-1] - seq[0] for seq in sequences if len(seq) > 1)
    return ans


if __name__ == '__main__':
    pass
