from math import sin
from math import pi
from statistics import mean


def f(x):
    return 6.25 * sin(2 * pi / 12 * (x - 4)) + 23.75


if __name__ == "__main__":
    numbers = [float(x.strip()) for x in open("data.txt", "r").read().split("\n") if x.strip() != ""]
    SS_tot = 0
    SS_res = 0
    for i in range(len(numbers)):
        x = i + 1
        SS_tot += (numbers[i] - mean(numbers))**2
        SS_res += (numbers[i] - f(x))**2
    print(1 - SS_res / SS_tot)
