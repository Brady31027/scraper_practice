import requests
import os
import glob
import urllib.request
import re
from bs4 import BeautifulSoup

class UrbanCrawler():
    debugMode = False
    dstFolder = ''
    dataString = ''
    bsObj = None

    # config debug mode
    def __init__(self, debugMode, dstFolder):
        self.debugMode = debugMode
        self.dstFolder = dstFolder

    # create corresponding folder to save images
    # if dst folder doesn't exist, create it
    # if dst folder is not empty, delete all existed images
    def envSetup(self):
        if not os.path.exists(self.dstFolder):
            print("{} is not existed, create new dst folder".format(self.dstFolder))
            os.makedirs(self.dstFolder)
        else:
            if os.listdir(self.dstFolder):
                print("{} folder is not empty".format(self.dstFolder))
                files = glob.glob(self.dstFolder+'/*')
                for f in files:
                    print("... delete {}".format(f))
                    os.remove(f)

    # for debug mode, read mock src and parse the data
    # for release mode, connect to the identified url directly
    def connect(self):
        if self.debugMode:
            print("-> Read mock source")
            with open('mock_src.html', 'r') as myfile:
                self.dataString = myfile.read()
            self.bsObj = BeautifulSoup(self.dataString, "html.parser")
        else:
            # TODO: connect to the url server
            print("-> Connect to server")

    # parsing the html source and get the sample image urls
    def parsing(self):
        sampleDivs = self.bsObj.findAll("div", {"class": "minibanner-box"})
        for sampleDiv in sampleDivs:
            images = sampleDiv.findAll("img")
            for img in images:
                if img.get('alt', ''):
                    self.download(img['src'])

    # download the image according to the given url
    def download(self, url):
        print("Input url: {}".format(url))
        matchedPattern = re.search('T/(.+)\.([A-Za-z]+)$', url)
        fileName = matchedPattern.group(1)
        fileType = matchedPattern.group(2)
        dstName = self.dstFolder + '/' + fileName + '.' + fileType
        urllib.request.urlretrieve(url, dstName)
        print("Downloaded")


urbanCrawler = UrbanCrawler(True, './results')
urbanCrawler.envSetup()
urbanCrawler.connect()
urbanCrawler.parsing()