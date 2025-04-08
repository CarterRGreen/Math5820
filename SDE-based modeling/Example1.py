import math, random
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def run(A_0, delT, endTime):
    A_t = A_0
    currentTime = 0
    time_points = []
    molecule_counts_A = []
    time_points.append(currentTime)
    molecule_counts_A.append(A_t)
    while currentTime < endTime:
        r1 = random.normalvariate(0, 1)
        currentTime = currentTime + delT
        A_t = A_t + r1 * math.sqrt(delT)
        time_points.append(currentTime)
        molecule_counts_A.append(A_t)
        
    return A_t, time_points, molecule_counts_A


def plotRuns(A_0, delT, endTime, numRuns):
    run_data_A = []
    end_data_A = []
    for i in range(numRuns):
        A_t, time_points, molecule_counts_A= run(A_0 = A_0, delT=delT, endTime=endTime)
        runi_A = [time_points, molecule_counts_A]
        run_data_A.append(runi_A)
        end_data_A.append(A_t)

    
    for i in range(len(run_data_A)):
        plt.plot(run_data_A[i][0], run_data_A[i][1])
    average_A = computeAverate(run_data_A,delT, endTime)
    plt.plot([i*delT for i in range(len(average_A))], average_A, color='black', linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of Atomic Change with {numRuns} Runs. A")
    plt.figure()
    makeHistogram(end_data_A)
    plt.show()

def computeAverate(run_data,delT, endTime):
    average = [0] * len(run_data[0][0])
    for i in range(len(run_data)):
        for j in range(len(run_data[i][0])):
            time = int(run_data[i][0][j]/delT)
            average[time] = average[time] + run_data[i][1][j]
    for i in range(len(average)):
        average[i] = average[i]/len(run_data)
    return average

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)
    plt.xlabel('Molecule A Count') 
    plt.ylabel('Frequency')
    plt.title('Histogram of Molecule A Counts')

plotRuns(A_0=0, delT=1, endTime=100, numRuns=500)