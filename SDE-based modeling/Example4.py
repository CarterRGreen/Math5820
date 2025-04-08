import math, random
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def run(X_0, delT, endTime, k1, k2, k3, k4, k5):
    X_t = X_0
    currentTime = 0
    time_points = []
    position_X = []
    time_points.append(currentTime)
    position_X.append(X_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        r1 = random.normalvariate(0, 1)
        f = -k1 * X_t*X_t*X_t + k2 * X_t*X_t - k3 * X_t + k4
        g = k5
        X_t = X_t + f *delT + r1 * math.sqrt(delT) * g
        time_points.append(currentTime)
        position_X.append(X_t)
    return X_t, time_points, position_X


def plotRuns(X_0, delT, endTime, numRuns, k1, k2, k3, k4, k5):
    run_data_X = []
    end_data_X = []
    for i in range(numRuns):
        X_t, time_points, position_X, = run(X_0 = X_0, delT=delT, endTime=endTime, k1=k1, k2=k2, k3=k3, k4=k4, k5=k5)
        runi_X = [time_points, position_X]
        run_data_X.append(runi_X)
        end_data_X.append(X_t)
    
    
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][0], run_data_X[i][1])
    plotODE(X_0, delT, endTime, k1, k2, k3, k4)
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example 3.2 D")
    # plt.figure()
    # makeHistogram(end_data_X)
    # plt.xlabel('End X Movement') 
    # plt.ylabel('Frequency')
    # plt.title('Histogram of End X Movement')
    plt.show()

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)

def plotODE(x_0, delT, endTime, k1, k2, k3, k4):
    X_t = x_0
    currentTime = 0
    time_points = []
    position_X = []
    time_points.append(currentTime)
    position_X.append(X_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        f = -k1 * X_t*X_t*X_t + k2 * X_t*X_t - k3 * X_t + k4
        X_t = X_t + f * delT
        time_points.append(currentTime)
        position_X.append(X_t)
    plt.plot(time_points, position_X, color='black', linewidth=2, linestyle='dashed')

# plotRuns(X_0=0, delT=.001, endTime=800, numRuns=1, k1=.001, k2=0.75, k3=165, k4=10000, k5=200)
