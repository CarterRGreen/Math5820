import math, random
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def run(X_0, D, L, delT, endTime):
    X_t = X_0
    currentTime = 0
    time_points = []
    position_X = []
    time_points.append(currentTime)
    position_X.append(X_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        r1 = random.normalvariate(0, 1)
        X_t = X_t  + math.sqrt(2*D*delT) *r1
        if X_t < 0:
            X_t = -X_t
        if X_t > L:
            X_t = 2*L - X_t
        time_points.append(currentTime)
        position_X.append(X_t)
    return X_t, time_points, position_X


def plotRuns(X_0, D, L, delT, endTime, numRuns):
    run_data_X = []
    end_data_X = []
    for i in range(numRuns):
        X_t, time_points, position_X, = run(X_0 = X_0, D=D, L=L, delT=delT, endTime=endTime)
        runi_X = [time_points, position_X]
        run_data_X.append(runi_X)
        end_data_X.append(X_t)
    
    
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][1], run_data_X[i][0], linewidth=0.7)
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example 4.2 a")
    # plt.savefig("Example4.2a.png")
    plt.figure()
    makeHistogram(end_data_X)
    plt.xlabel('End X Movement') 
    plt.ylabel('Frequency')
    plt.title('Histogram of End X Movement')
    # plt.savefig('Example4.2b.png')
    plt.show()

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)

plotRuns(X_0=0, D=.0001, L=1, delT=.000000000000002, endTime=.0000000006, numRuns=1000)