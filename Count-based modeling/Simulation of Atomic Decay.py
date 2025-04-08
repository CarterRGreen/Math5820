import random
import math

def timeToNextDecay(A_t, k):
    rand = random.uniform(0,1)
    return -math.log(rand)/(A_t*k)

def run(A_0, k, t):
    A_t = A_0
    currentTime = 0
    while currentTime < t:
        timeToDecay = timeToNextDecay(A_t, k)
        currentTime = currentTime + timeToDecay
        A_t = A_t - 1
    print(A_t)

run(100,.02,100)