import math, random
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def run(X_0, Y_0, D, delT, endTime):
    X_t = X_0
    Y_t = Y_0
    currentTime = 0
    time_points = []
    position_X = []
    position_Y = []
    time_points.append(currentTime)
    position_X.append(X_t)
    position_Y.append(Y_t)
    while currentTime < endTime:
        currentTime = currentTime + delT
        r1 = random.normalvariate(0, 1)
        r2 = random.normalvariate(0, 1)
        X_t = X_t + r1 * math.sqrt(2*D*delT)
        Y_t = Y_t + r2 * math.sqrt(2*D*delT)
        time_points.append(currentTime)
        position_X.append(X_t)
        position_Y.append(Y_t)        
    return X_t, Y_t, time_points, position_X, position_Y


def plotRuns(X_0, Y_0, D, delT, endTime, numRuns):
    run_data_X = []
    run_data_Y = []
    end_data_X = []
    end_data_Y = []
    for i in range(numRuns):
        X_t, Y_t, time_points, position_X, position_Y = run(X_0 = X_0, Y_0 = Y_0, D = D, delT=delT, endTime=endTime)
        runi_X = [time_points, position_X]
        runi_Y = [time_points, position_Y]
        run_data_X.append(runi_X)
        run_data_Y.append(runi_Y)
        end_data_X.append(X_t)
        end_data_Y.append(Y_t)
    
    # twoDPlot(run_data_X, run_data_Y)
    # average_X, average_Y = computeAverate(run_data_X,run_data_Y,delT, endTime)
    # plt.plot(average_X, average_Y, color='black', linewidth=2)
    # plt.xlabel("Time")
    # plt.ylabel("Number of Molecules")
    # plt.title(f"Simulation of movement with {numRuns} Runs. A")
    # plt.figure()
    make2dHistogram(end_data_X, end_data_Y)
    plt.xlabel('End Movement')
    plt.savefig('Example4.1.png')
    plt.show()

def twoDPlot(run_data_X, run_data_Y):
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][1], run_data_Y[i][1])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Simulation of Movement with {len(run_data_X)} Runs")

def computeAverate(run_data_X, run_data_Y,delT, endTime):
    average_X = [0] * len(run_data_X[0][0])
    average_Y = [0] * len(run_data_Y[0][0])
    for i in range(len(run_data_X)):
        for j in range(len(run_data_X[i][0])):
            time = int(run_data_X[i][0][j]/delT)
            average_X[time] = average_X[time] + run_data_X[i][1][j]
            average_Y[time] = average_Y[time] + run_data_Y[i][1][j]
    for i in range(len(average_X)):
        average_X[i] = average_X[i]/len(run_data_X)
        average_Y[i] = average_Y[i]/len(run_data_Y)
    return average_X, average_Y

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)

def make2dHistogram(end_data_A, end_data_B):
    plt.hist2d(end_data_A, end_data_B, bins=60)

plotRuns(X_0=0,Y_0=0,D=.0001, delT=.1, endTime=10, numRuns=1000000)