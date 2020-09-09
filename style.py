import matplotlib.pyplot as plt


def set_style():
    # Set plot parameters
    fontsize = 24
    linewidth = 2
    tickdirection = 'out'
    tickmajorsize = 10
    tickminorsize = 5

    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams['font.size'] = fontsize
    plt.rcParams['axes.titlesize'] = fontsize
    plt.rcParams['axes.labelsize'] = fontsize
    plt.rcParams['xtick.labelsize'] = fontsize
    plt.rcParams['ytick.labelsize'] = fontsize
    plt.rcParams['legend.fontsize'] = fontsize
    plt.rcParams['figure.titlesize'] = fontsize
    plt.rcParams['lines.linewidth'] = linewidth
    plt.rcParams['axes.linewidth'] = linewidth
    plt.rcParams['xtick.direction'] = tickdirection
    plt.rcParams['ytick.direction'] = tickdirection
    plt.rcParams['xtick.major.top'] = False
    plt.rcParams['xtick.minor.top'] = False
    plt.rcParams['ytick.major.right'] = False
    plt.rcParams['ytick.minor.right'] = False
    plt.rcParams['xtick.major.width'] = linewidth
    plt.rcParams['xtick.minor.width'] = linewidth
    plt.rcParams['ytick.major.width'] = linewidth
    plt.rcParams['ytick.minor.width'] = linewidth
    plt.rcParams['xtick.major.size'] = tickmajorsize
    plt.rcParams['ytick.major.size'] = tickmajorsize
    plt.rcParams['xtick.minor.size'] = tickminorsize
    plt.rcParams['ytick.minor.size'] = tickminorsize
