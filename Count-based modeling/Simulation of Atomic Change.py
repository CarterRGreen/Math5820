import math, random
import matplotlib.pyplot as plt

def timeToNextReaction(alpha, r1):
    return -math.log(r1) / alpha

def nextReaction(alpha, A_t, k, r2):
    if r2 < A_t * k / alpha:
        return -1
    else:
        return 1

def run(A_0, k_1, k_2,v, endTime):
    A_t = A_0
    currentTime = 0
    time_points = []
    molecule_counts = []
    time_points.append(currentTime)
    molecule_counts.append(A_t)
    while currentTime < endTime:
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        alpha = A_t * k_1 + k_2 * v
        timeToReaction = timeToNextReaction(alpha, r1)
        currentTime = currentTime + timeToReaction
        if(currentTime < endTime):
            A_t = A_t + nextReaction(alpha, A_t, k_1, r2)
            time_points.append(currentTime)
            molecule_counts.append(A_t)
        
    return A_t, time_points, molecule_counts

def calcAverage(A_0, k_1, k_2, v, endTime, numRuns):
    total = 0
    for i in range(numRuns):
        A_t = run(A_0, k_1, k_2, v, endTime)
        total = total + A_t
    return total / numRuns

def calcVariance(A_0, k_1, k_2, v, endTime, numRuns):
    total = 0
    for i in range(numRuns):
        A_t = run(A_0, k_1, k_2, v, endTime)
        total = total + A_t 
    return total  * total / numRuns / numRuns - (calcAverage(A_0, k_1, k_2, v, endTime, numRuns)) ** 2

def plotRuns(A_0, k_1, k_2, v, endTime, numRuns):
    for i in range(numRuns):
        A_t, time_points, molecule_counts = run(A_0, k_1, k_2, v, endTime)
        plt.plot(time_points, molecule_counts)
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of Atomic Change with {numRuns} Runs")
    plt.show()

plotRuns(10, 0.05, 0.01, 10, 500, 50)

# a_0 = 100
# k_1 = 0.02
# k_2 = 0.05
# v = 100
# endTime = 100
# numRuns = 10000
# print(f"Actual Average: {calcAverage(a_0, k_1, k_2, v, endTime, numRuns)}")
# print(f"Expected Average {k_2 / k_1 * v + (a_0 - k_2 / k_1 * v) * math.exp(-k_1 * endTime)}")

# print(f"Actual Variance: {calcVariance(a_0, k_1, k_2, v, endTime, numRuns)}")
# #print(f"Expected Variance: {k_2 / k_1 * v + (a_0 - k_2 / k_1 * v) * math.exp(-k_1 * endTime)}")