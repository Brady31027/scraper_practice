import re
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as plt3d

class Point():
	def __init__(self, r, g, b, _class = -1):
		self.r = r
		self.g = g
		self.b = b
		self._class = _class

class KMeans():
	def __init__(self, k, iterCnt):
		self.k = k
		self.iterCnt = iterCnt
		self.centers = []
		for i in xrange(k):
			point = Point(random.randint(0, 255), 
						random.randint(0, 255), 
						random.randint(0, 255))
			self.centers.append(point)
	def classify(self):
		pass

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

io = Io('rgb_quantization.txt')
io.readData()
kmeans = KMeans(6, 100)

for i in xrange(len(kmeans.centers)):
	p = kmeans.centers[i]
	print "{} {} {} {}".format(p.r, p.g, p.b, p._class)
	

# drawing
"""
fig = plt.figure(num=1)
fig3d = plt3d.Axes3D(fig)

R = np.array(io.redChannel)
G = np.array(io.greenChannel)
B = np.array(io.blueChannel)

ax = plt.gca()
ax.hold(True)


for i in xrange(0, len(R), 1):
	r = "%02x" % (R[i])
	g = "%02x" % (G[i])
	b = "%02x" % (B[i])
	color = '#'+r+g+b
	ax.scatter(R[i], G[i], B[i], color=color)

plt.show()
"""
