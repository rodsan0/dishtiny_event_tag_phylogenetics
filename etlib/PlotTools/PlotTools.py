import matplotlib.pyplot as plt

def enable_pretty_graphing():
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams["figure.figsize"] = (15, 20)
    plt.rcParams["font.size"] = 13
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams['font.family'] = 'Roboto'
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['figure.edgecolor'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'
