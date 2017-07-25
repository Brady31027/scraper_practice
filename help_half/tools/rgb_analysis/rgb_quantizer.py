import os
import glob
import re

# read pixel data per image and calculate the average value per channel
class RGBQuantizer():

    def __init__(self, quantization_folders):
        self.quantizationFolders = qualtization_folders

    def quantize(self):
        originalPath = os.getcwd()
        with open('rgb_quantization.txt', 'w') as output:
            for path in self.quantizationFolders:
                os.chdir(path)
                files = glob.glob('*.txt')
                for file in files:
                    print("Quantizing " + file)
                    (redMean, greenMean, blueMean) = self.innerQuantize(file)
                    output.write("{} = {}, {}, {} \n".format(file, redMean, greenMean, blueMean))
                os.chdir(originalPath)

    def innerQuantize(self, filename):
        dataCnt, redSum, greenSum, blueSum = 0, 0, 0, 0
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = re.sub('\s', '', line)
                matchedPattern = re.search('(\d+),(\d+),(\d+)', line)
                redSum += int(matchedPattern.group(1))
                greenSum += int(matchedPattern.group(2))
                blueSum += int(matchedPattern.group(3))
                dataCnt += 1
        return (redSum//dataCnt, greenSum//dataCnt, blueSum//dataCnt)



qualtization_folders = [
 '../../crawlers/urban_crawler/results',
 '../../crawlers/duchateau_crawler/results'
]

quantizer = RGBQuantizer(qualtization_folders)
quantizer.quantize()