from math import log
from random import random
import matplotlib.pyplot as plt
import numpy as np

l = 2
T = 24

curr = -1/l * log(random())
arrival = [curr]

while curr < T:
    curr = curr -1/l * log(random())
    arrival.append(curr)

arrival = arrival[1:]

t = np.arange(0.0, T, 0.01)

N = len(t)
X = np.zeros(N)

for i in range(N):
    X[i] = np.sum(arrival <= t[i])

plt.plot(t, X)
plt.xlabel('time(hrs)')

plt.show()
