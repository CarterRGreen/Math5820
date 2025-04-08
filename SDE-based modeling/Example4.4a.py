import math, random
import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

def run(X_0, D, S, delT, endTime):
    X_t = X_0
    r = random.uniform(0, 1)
    if r < 0.5:
        V_t = - S
    else:
        V_t = S
    lamb = S * S / 2 / D
    currentTime = 0
    time_points = []
    position_X = []
    time_points.append(currentTime)
    position_X.append(X_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        r1 = random.uniform(0, 1)
        if currentTime < endTime:
            X_t = X_t + V_t * delT
            time_points.append(currentTime)
            position_X.append(X_t)
        if r1 < lamb * delT:
            V_t = - V_t
    return X_t, time_points, position_X


def plotRuns(X_0, D, S, delT, endTime, numRuns):
    run_data_X = []
    end_data_X = []
    for i in range(numRuns):
        X_t, time_points, position_X, = run(X_0 = X_0, D=D, S=S, delT=delT, endTime=endTime)
        for j in range(len(position_X)):
            position_X[j] = position_X[j] * 1e9
            time_points[j] = time_points[j] * 1e9

        runi_X = [time_points, position_X]
        run_data_X.append(runi_X)
        end_data_X.append(X_t)
    
    
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][0], run_data_X[i][1], linewidth=0.4)
    plt.xlabel("Time [ns]")
    plt.ylabel("x [nm]")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example 4.4 a")
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

plotRuns(X_0=0, D=1e-4, S=1e4, delT=2e-14, endTime=6e-10, numRuns=6)