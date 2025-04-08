import math, random
import matplotlib.pyplot as plt


def plotTimeVsX(run_data_X, numRuns, exampleNumber, linewidth=0.4,):
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][0], run_data_X[i][1], linewidth=linewidth)
    plt.xlabel("Time")
    plt.ylabel("x")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example {exampleNumber}")
    plt.show()

def plotXvsTime(run_data_X, numRuns, exampleNumber, linewidth=0.4,):
    for i in range(len(run_data_X)):
        plt.plot(run_data_X[i][1], run_data_X[i][0], linewidth=linewidth)
    plt.ylabel("Time")
    plt.xlabel("x")
    plt.title(f"Simulation of movement with {numRuns} Runs. Example {exampleNumber}")
    plt.show()

def makeHistogram(end_data_A, bins=40, range=(0, 1)):
    plt.hist(end_data_A, bins=bins, range=range)
    plt.xlabel('End X Movement') 
    plt.ylabel('Frequency')
    plt.title('Histogram of End X Movement')


def run(D, k1, k2, h, L, delT, endTime):
    currentTime = 0
    X_t = []
    while True:
        currentTime = currentTime + delT
        if currentTime > endTime:
            break
        newX_t = []
        for moleculePosition in X_t:
            r1 = random.normalvariate(0, 1)
            moleculePosition += math.sqrt(2 * D * delT) * r1
            if moleculePosition < 0:
                moleculePosition = - moleculePosition
            elif moleculePosition > L:
                moleculePosition = 2 * L - moleculePosition
            r2 = random.uniform(0, 1)
            if r2 >= k1 * delT:
                newX_t.append(moleculePosition)
        X_t = newX_t
        r3 = random.uniform(0, 1)
        if r3 < k2 * h * h  * L / 5 * delT:
            r4 = random.uniform(0, 1)
            X_t.append(r4 * L / 5)
    return X_t


def plotRuns(D, k1, k2, h, L, delT, endTime, numRuns):
    end_data_X = []
    for i in range(numRuns):
        X_t = run(D=D, k1=k1, k2=k2, h=h, L=L, delT=delT, endTime=endTime)
        end_data_X.append(X_t)
    
    
    makeHistogram(end_data_X, bins=40, range=(0, L))
    plt.show()


#k2 = 2e-5 um^{-3} s^{-1} = 2e4 * mm^{-3} s^{-1}
plotRuns(D=1e-4, k1=1e-3, k2=2e4, h=1/40, L=1, delT=0.01, endTime=1800, numRuns=1)