from UtilitiesPersonal import plotTimeVsX
import math, random
import matplotlib.pyplot as plt

def run(X_0, D, S, L, delT, endTime):
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
        r = random.uniform(0, 1)
        if X_t + V_t * delT < 0:
            X_t = - X_t - V_t * delT
            V_t = - V_t
        elif X_t + V_t * delT > L:
            X_t = 2 * L - X_t - V_t * delT
            V_t = - V_t
        else:
            X_t = X_t + V_t * delT
        if r < lamb * delT:
            V_t = - V_t
        currentTime = currentTime + delT
        time_points.append(currentTime)
        position_X.append(X_t)
    return X_t, time_points, position_X


def plotRuns(X_0, D, S, L, delT, endTime, numRuns):
    run_data_X = []
    end_data_X = []
    for i in range(numRuns):
        X_t, time_points, position_X, = run(X_0 = X_0, D=D, S=S, L=L, delT=delT, endTime=endTime)
        for j in range(len(position_X)):
            position_X[j] = position_X[j]
            time_points[j] = time_points[j]

        runi_X = [time_points, position_X]
        run_data_X.append(runi_X)
        end_data_X.append(X_t)
    
    
    plotTimeVsX(run_data_X, numRuns, "4.4c", linewidth=0.4)
    # plt.savefig("Example4.4c.png")
    plt.show()



plotRuns(X_0=0.4, D=1e-4, S=1e-2, L=1, delT=0.1, endTime=840, numRuns=6)