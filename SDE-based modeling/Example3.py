import math, random
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def run(X_0, delT, endTime):
    X_t = X_0
    currentTime = 0
    time_points = []
    position_X = []
    time_points.append(currentTime)
    position_X.append(X_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        r1 = random.normalvariate(0, 1)
        X_t = X_t + delT + r1 * math.sqrt(delT)
        time_points.append(currentTime)
        position_X.append(X_t)
    return X_t, time_points, position_X


def plotRuns(X_0, delT, endTime, numRuns):
    run_data_X = []
    end_data_X = []
    for i in range(numRuns):
        X_t, time_points, position_X, = run(X_0 = X_0, delT=delT, endTime=endTime)
        runi_X = [time_points, position_X]
        run_data_X.append(runi_X)
        end_data_X.append(X_t)
    
    
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][0], run_data_X[i][1])
    plt.plot([0,endTime], [0,endTime], color='black', linewidth=2, linestyle='dashed')
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example 3.2 c")
    plt.figure()
    makeHistogram(end_data_X)
    plt.xlabel('End X Movement') 
    plt.ylabel('Frequency')
    plt.title('Histogram of End X Movement')
    plt.show()

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)

plotRuns(X_0=0, delT=.001, endTime=100, numRuns=500)