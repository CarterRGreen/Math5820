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

def makeHistogram(end_data_A, bins=40):
    plt.hist(end_data_A, bins=bins)
    plt.xlabel('End X Movement') 
    plt.ylabel('Frequency')
    plt.title('Histogram of End X Movement')
