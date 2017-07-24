from PIL import Image
import os
import glob
import re

class RGBAnalyzer():
    sourceFolders = []
    def __init__(self, sourceFolders):
        self.sourceFolders = sourceFolders

    def analyzeRGB(self):
        for folder in self.sourceFolders:
            rootPath = os.getcwd()
            print("go to " + folder)
            os.chdir(folder)
            images = glob.glob('*.jpg')
            for img in images:
                filename = re.sub('.jpg', '.txt', img)
                with open(filename, 'w') as file:
                    im = Image.open(img)
                    print("analyzing {}".format(filename))
                    pixels = list(im.getdata())
                    for pix in pixels:
                        file.write(str(pix))
                        file.write("\n")
            os.chdir(rootPath)

analysis_folder = [
 '../../crawlers/urban_crawler/results',
 '../../crawlers/duchateau_crawler/results'
]

analyzer = RGBAnalyzer(analysis_folder)
analyzer.analyzeRGB()