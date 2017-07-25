import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as plt3d

fig = plt.figure(num=1)
fig3d = plt3d.Axes3D(fig)

vectorRed, vectorGreen, vectorBlue = [], [], []
with open('rgb_quantization.txt', 'r') as file:
	lines = file.readlines()
	
for line in lines:
	line = re.sub(' ', '', line)
	matchedPattern = re.search('(\d+),(\d+),(\d+)', line)
	vectorRed.append(int(matchedPattern.group(1)))
	vectorGreen.append(int(matchedPattern.group(2)))
	vectorBlue.append(int(matchedPattern.group(3)))

R = np.array(vectorRed)
G = np.array(vectorGreen)
B = np.array(vectorBlue)

ax = plt.gca()
ax.hold(True)

for i in xrange(0, len(R), 1):
	r = "%02x" % (R[i])
	g = "%02x" % (G[i])
	b = "%02x" % (B[i])
	color = '#'+r+g+b
	ax.scatter(R[i], G[i], B[i], color=color)

plt.show()
