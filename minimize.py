import numpy as np

HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]


def Cost(b):
    cost = 0
    for i in range(len(MURDERS)):
        cost += (b[0] + b[1] * HOURLY_WAGE[i] - MURDERS[i]) ** 2
    return cost

def minimum(f, B0, eta, h, precision):
    trace = []
    B = B0
    steps = 0
    while True:
        steps += 1
        if steps % 10 == 0:
            trace.append(B)
        slope = [f([B[0] + h, B[1]]) - f(B), f([B[0], B[1] + h]) - f(B)]
        B0 = B
        B = B0 - eta * np.array(slope)
        if abs(f(B) - f(B0)) < precision:
            if f(B) < f(B0):
                break
    return B, steps, trace

