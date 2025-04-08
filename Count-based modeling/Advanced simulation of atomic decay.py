import math, random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def timeToNextReaction(alpha, r1):
    return -math.log(r1) / alpha

def nextReaction(alpha, r2, alpha1, alpha2, alpha3):
    if r2 < alpha1 / alpha:
        return 1
    elif r2 < (alpha2 + alpha1) / alpha:
        return 2
    elif r2 < (alpha3 + alpha2 + alpha1) / alpha:
        return 3
    else:
        return 4

def run(A_0, B_0, k_1, k_2, k_3, k_4, v, endTime):
    A_t = A_0
    B_t = B_0
    currentTime = 0
    time_points = []
    molecule_counts_A = []
    molecule_counts_B = []
    time_points.append(currentTime)
    molecule_counts_A.append(A_t)
    molecule_counts_B.append(B_t)
    alpha1 =  A_t *(A_t - 1) * k_1 / v
    alpha2 =  A_t * B_t * k_2 / v
    alpha3 = k_3 * v
    alpha4 = k_4 * v
    alpha = alpha1 + alpha2 + alpha3 + alpha4
    while currentTime < endTime:
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        timeToReaction = timeToNextReaction(alpha, r1)
        currentTime = currentTime + timeToReaction
        if(currentTime < endTime):
            reactionNumber = nextReaction(alpha, r2, alpha1=alpha1, alpha2=alpha2, alpha3=alpha3)
            if reactionNumber == 1:
                A_t = A_t - 2
                alpha1 =  A_t *(A_t - 1) * k_1 / v
                alpha2 = A_t * B_t * k_2 / v
                alpha = alpha1 + alpha2 + alpha3 + alpha4
            elif reactionNumber == 2:
                A_t = A_t - 1
                B_t = B_t - 1
                alpha1 =  A_t *(A_t - 1) * k_1 / v
                alpha2 = A_t * B_t * k_2 / v
                alpha = alpha1 + alpha2 + alpha3 + alpha4
            elif reactionNumber == 3:
                A_t = A_t + 1
                alpha1 =  A_t *(A_t - 1) * k_1 / v
                alpha2 = A_t * B_t * k_2 / v
                alpha = alpha1 + alpha2 + alpha3 + alpha4
            elif reactionNumber == 4:
                B_t = B_t + 1
                alpha2 = A_t * B_t * k_2 / v
                alpha = alpha1 + alpha2 + alpha3 + alpha4
            time_points.append(currentTime)
            molecule_counts_A.append(A_t)
            molecule_counts_B.append(B_t)
        
    return A_t, time_points, molecule_counts_A, B_t, molecule_counts_B


def plotRuns(A_0, B_0, k_1, k_2, k_3, k_4, v, endTime, numRuns):
    run_data_A = []
    run_data_B = []
    end_data_A = []
    end_data_b = []
    for i in range(numRuns):
        A_t, time_points, molecule_counts_A, B_t, molecule_counts_B = run(A_0 = A_0, B_0=B_0, k_1= k_1, k_2=k_2, k_3=k_3, k_4=k_4, v=v, endTime=endTime)
        runi_A = [time_points, molecule_counts_A]
        runi_B = [time_points, molecule_counts_B]
        run_data_A.append(runi_A)
        run_data_B.append(runi_B)

        end_data_A.append(A_t)
        end_data_b.append(B_t)

    
    for i in range(len(run_data_A)):
        plt.plot(run_data_A[i][0], run_data_A[i][1])
    avg = computeAverage(run_data_A, endTime)
    plt.plot(range(len(avg)), avg, color='black', label='Average')
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of Atomic Change with {numRuns} Runs. A")
    plt.figure()

    for i in range(len(run_data_B)):
        plt.plot(run_data_B[i][0], run_data_B[i][1])
    avg = computeAverage(run_data_B, endTime)
    plt.plot(range(len(avg)), avg, color='black', label='Average')
    plt.xlabel("Time")
    plt.ylabel("Number of Molecules")
    plt.title(f"Simulation of Atomic Change with {numRuns} Runs. B")

    heatMap(end_data_A, end_data_b)
    plt.figure()
    makeHistogram(end_data_A)

def computeAverage(run_data, endTime):
    average = [0 for i in range(endTime)]
    for time_i in range(endTime):
        for i in range(len(run_data)):
            for j in range(len(run_data[i][0])):
                if run_data[i][0][j] >= time_i:
                    average[time_i] = average[time_i] + run_data[i][1][j]
                    break
    for i in range(len(average)):
        average[i] = average[i] / len(run_data)
    return average

def heatMap(end_data_A, end_data_B):
    binsA = np.arange(0, 30, 1)  # Bins for moleculeA (range and step)
    binsB = np.arange(0, 30, 1)  # Bins for moleculeB (range and step)

    # Create a 2D histogram
    hist, xedges, yedges = np.histogram2d(end_data_A, end_data_B, bins=[binsA, binsB])

    # Normalize the histogram (optional, for percentage-based heatmaps)
    hist = hist / np.sum(hist)

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(hist.T,  # Transpose to match (x, y) order
                xticklabels=binsA[:-1],  # Bin edges as labels
                yticklabels=binsB[:-1],
                cmap="viridis",  # Colormap
                cbar_kws={'label': 'Frequency'},  # Add color bar label
    )
    plt.xlabel('Molecule A Count')
    plt.ylabel('Molecule B Count')
    plt.title('Heatmap of Molecule A vs. Molecule B Frequency')

def makeHistogram(end_data_A):
    plt.hist(end_data_A, bins=60)
    plt.xlabel('Molecule A Count') 
    plt.ylabel('Frequency')
    plt.title('Histogram of Molecule A Counts')
    plt.show()

plotRuns(A_0=0, B_0=0, k_1=.001, k_2=0.01, k_3=1.2, k_4=1, v=1, endTime=100, numRuns=5000)