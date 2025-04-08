import random
# Move forward one unit in time
def incrementTime(A_t, k, dt):
    rand = random.uniform(0,1)
    if rand < A_t * k * dt:
        return -1
    return 0

def run(A_0, k, dt, t):
    A_t = A_0
    currentTime = 0
    while currentTime < t:
        currentTime = currentTime + dt
        A_t = A_t + incrementTime(A_t, k, dt)
    print(A_t)

run(100,.02,.00001,100)