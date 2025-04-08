import math, random
import matplotlib.pyplot as plt
import numpy as np

def timeToNextReaction(alpha, r1):
    return -math.log(r1) / alpha

def nextReaction(alpha, r2, k2, k1, alphai, X):
    for i in range(len(alphai)-1):
        if r2 < sum(alphai[:i+1])/alpha:
            return i, True, False, False
    newr2 = r2 - sum(alphai[:-1])/alpha
    for i in range(1, len(alphai)):
        if newr2 < sum(alphai[1:i+1])/alpha:
            return i, False, False, False
    newr3 = newr2 - sum(alphai[1:])/alpha
    for i in range(0,  K// 5):
        if newr3 < k2 * (i+1) * 25 ** 3/1000 ** 3 / alpha:
            return i, False, True, False
    newr4 = newr3 - k2 * K/5 * 25 ** 3/1000 ** 3 / alpha
    for i in range(0, K):
        if newr4 < k1 * X[i] / alpha:
            return i, False, False, True
        else:
            newr4 -= k1 * X[i] / alpha
        
    raise ValueError("Reaction not found")
    # return len(alphai)-1, False

def run(X_0, d, K, k2,k1, endTime):
    X_t = X_0
    numMolecules = sum(X_0)
    currentTime = 0
    time_points = []
    molecule_counts = []
    trackSingleMolecule = []
    for i in range(len(X_0)):
        if X_0[i] == 1:
            trackSingleMolecule.append(i/K)
            break
    time_points.append(currentTime)
    # molecule_counts.append(X_t)
    alphai = [d * X_t_i for X_t_i in X_t]
    alpha = 2 * d *numMolecules - d*X_t[0] - d*X_t[-1] + k2 * K/5 * 25 ** 3/1000 ** 3+ k1 * numMolecules
    while currentTime < endTime:
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        timeToReaction = timeToNextReaction(alpha, r1)
        currentTime = currentTime + timeToReaction
        if(currentTime < endTime):
            reactionNumber, isRight, isBirth, isDeath = nextReaction(alpha, r2, k2, k1, alphai, X_t)
            if isRight:
                X_t[reactionNumber] -= 1
                X_t[reactionNumber+1] += 1
                alphai[reactionNumber+1] = d * X_t[reactionNumber+1]
                trackSingleMolecule.append((reactionNumber+1)/K)
            elif isBirth:
                X_t[reactionNumber] += 1
                numMolecules +=1
            elif isDeath:
                X_t[reactionNumber] -= 1
                numMolecules -= 1
            else:
                X_t[reactionNumber] -= 1
                X_t[reactionNumber-1] += 1
                alphai[reactionNumber-1] = d * X_t[reactionNumber-1]
                trackSingleMolecule.append((reactionNumber-1)/K)
            
            # Update Propensity Functions
            alphai[reactionNumber] = d * X_t[reactionNumber]
            alpha = 2 * d *numMolecules - d*X_t[0] - d*X_t[-1] + k2 * K/5 * 25 ** 3/1000 ** 3 + k1 * numMolecules
            time_points.append(currentTime)
            # molecule_counts.append(X_t)
            
        
    return X_t, time_points, molecule_counts, trackSingleMolecule


def plotRuns(X_0, d, K, k2, k1, endTime, numRuns):
    run_data = []
    end_data = []
    for i in range(numRuns):
        new_X_0 = X_0.copy()            
        X_t, time_points, molecule_counts, trackSingleMolecule = run(X_0 = new_X_0, d=d, K=K, k2=k2, k1=k1, endTime=endTime)
        runi_X = [time_points, trackSingleMolecule]
        run_data.append(runi_X)
        end_data = X_t
    # If multiple runs are being run then comment out makeHistogram and uncomment the following code to plot the runs
    # for i in range(len(run_data)):
    #     plt.plot(run_data[i][1], run_data[i][0])
    # plt.ylabel("Time")
    # plt.xlabel("Position")
    # plt.title(f"Simulation of Atomic Change with {numRuns} Runs. A")
    # plt.figure()
    makeHistogram(end_data)
    plt.show()


def makeHistogram(end_data):
    x = np.arange(K)
    x = x / 40
    plt.bar(x, height=end_data, width=0.025)
    plt.xlabel('x [mm]') 
    plt.ylabel('Frequency')
    plt.title('Histogram of Molecule A Counts')

K = 40
X_0_init = [0 for i in range(K)]
X_0_init[15] = 500
X_0_init[16] = 500
plotRuns(X_0=X_0_init, d=.16, K=40, k2=2e4,k1=1e-3, endTime=240, numRuns=1)