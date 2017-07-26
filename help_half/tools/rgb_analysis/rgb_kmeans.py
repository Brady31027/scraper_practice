import re
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as plt3d

# Final params
"""
cluster GRAY with center 85,77,72 
cluster BLACK with center 66,50,40
cluster WHITE with center 175,163,151
cluster BROWN with center 133,91,59
cluster GOLD with center 211,178,142
"""

class Point():
	def __init__(self, r, g, b, _class = -1):
		self.r = r
		self.g = g
		self.b = b
		self._class = _class

class KMeans():
	def __init__(self, points, k, iterCnt):
		self.points = points
		self.k = k
		self.iterCnt = iterCnt
		self.centers = []
		self.clusters = [[] for _ in xrange(k)]

		# expert system gives suggested values
		self.centers.append(Point(85,77,72)) # Gray
		self.centers.append(Point(55,40,31)) # Black
		self.centers.append(Point(160,200,136)) # White
		self.centers.append(Point(142,88,54)) # Brown
		self.centers.append(Point(230,180,120)) # Gold
	
	def findNearestCenter(self, p):
		minDis = sys.maxint
		minIndex = -1
		for i in xrange(self.k):
			c = self.centers[i]
			dis = ((c.r - p.r) ** 2) + ((c.g - p.g) ** 2) + ((c.b - p.b) ** 2)
			if dis < minDis:
				minDis = dis
				minIndex = i
		return minIndex

	def resetClusters(self):
		self.clusters = [[] for _ in xrange(self.k)]

	def calculateCenters(self):
		for i in xrange(self.k):
			cluster = self.clusters[i] 
			size = len(cluster)
			if size == 0:
				continue

			rSum, gSum, bSum = 0, 0, 0
			for j in xrange(size):
				rSum += cluster[j].r
				gSum += cluster[j].g
				bSum += cluster[j].b
			self.centers[i].r = rSum // size
			self.centers[i].g = gSum // size
			self.centers[i].b = bSum // size

	def classify(self):
		runCnt = 0
		clusterChanged = True
		while runCnt < self.iterCnt and clusterChanged:
			print "run cnt : {}".format(runCnt)
			clusterChanged = False
			self.resetClusters()
			for p in self.points:
				cluster = self.findNearestCenter(p)
				if cluster != p._class:
					p._class = cluster
					clusterChanged = True
					self.clusters[cluster].append(p)
			self.calculateCenters()
			runCnt += 1

	def getClusters(self):
		return self.clusters

class Io():
	def __init__(self, inputFile):
		self.inputFile = inputFile
		self.dataPoints = []
		self.redChannel = []
		self.greenChannel = []
		self.blueChannel = []

	def readData(self):
		with open(self.inputFile, 'r') as file:
			lines = file.readlines()
		for line in lines:
			line = re.sub(' ', '', line)
			matchedPattern = re.search('(\d+),(\d+),(\d+)', line)
			point = Point(int(matchedPattern.group(1)), 
		          		int(matchedPattern.group(2)), 
		          		int(matchedPattern.group(3)))
			self.dataPoints.append(point)
			self.redChannel.append(  int(matchedPattern.group(1)))
			self.greenChannel.append(int(matchedPattern.group(2)))
			self.blueChannel.append( int(matchedPattern.group(3)))
	
	def getPoints(self):
		return self.dataPoints

	def getRedChannel(self):
		return self.redChannel

	def getGreenChannel(self):
		return self.greenChannel
	
	def getBlueChannel(self):
		return self.blueChannel


io = Io('rgb_quantization.txt')
io.readData()
kmeans = KMeans(io.getPoints(), 5, 1)
kmeans.classify()
results = kmeans.getClusters()


for i in xrange(len(results)):
	print "cluster {} with center {},{},{} has {} elements".format(i, 
		kmeans.centers[i].r, 
		kmeans.centers[i].g, 
		kmeans.centers[i].b, 
		len(results[i]))


# drawing

fig = plt.figure(num=1)
fig3d = plt3d.Axes3D(fig)

R = np.array(io.redChannel)
G = np.array(io.greenChannel)
B = np.array(io.blueChannel)

center_r = []
center_g = []
center_b = []
for i in xrange(kmeans.k):
	center_r.append(kmeans.centers[i].r)
	center_g.append(kmeans.centers[i].g)
	center_b.append(kmeans.centers[i].b)
CR = np.array(center_r)
CG = np.array(center_g)
CB = np.array(center_b)

ax = plt.gca()
ax.hold(True)

# plot center
for i in xrange(kmeans.k):
	color = "red"
	if i == 0:
		color = "red"
	elif i == 1:
		color = "orange"
	elif i == 2:
		color = "yellow"
	elif i == 3:
		color = "green"
	elif i == 4:
		color= "blue"
	else:
		color = "purple"

	ax.scatter(CR[i], CG[i], CB[i], color=color)

# plot data
for i in xrange(0, len(R), 1):
	r = "%02x" % (R[i])
	g = "%02x" % (G[i])
	b = "%02x" % (B[i])
	color = '#'+r+g+b
	ax.scatter(R[i], G[i], B[i], color=color)

plt.show()
