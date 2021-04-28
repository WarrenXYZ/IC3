import matplotlib.pyplot as plt

"""
import numpy as np

trainx = np.linspace(-1, 1, 100)
trainy = 2 * trainx + np.random.randn(*trainx.shape) * 0.3

plt.plot(trainx, trainy, 'ro', label = 'Original data')
plt.legend()
plt.show()
print("画图结束")
"""

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "0.8")

arrowEdge = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction', xytext = centerPt, textcoords = 'axes fraction', va = "center", ha = "center", bbox = nodeType, arrowprops = arrowEdge)

def createPlot():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()

    createPlot().ax1 = plt.subplot(111, frameon = False)

    plotNode('决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)

    plt.show()
