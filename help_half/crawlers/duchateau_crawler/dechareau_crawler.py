import os
import glob
import re
import urllib.request
import time
from bs4 import BeautifulSoup

class DechareauCrawler():

    debugMode = True
    dstFolder = ''
    collectionList = {
        'chateau' : 'chateau.html',
        'vernal' : 'vernal.html',
        'heritage_timber' : 'heritage_timber.html',
        'riverstone' : 'riverstone.html',
        'strata' : 'strata.html',
        'terra' : 'terra.html',
        'vintage_remains' : 'vintage_remains.html',
        'new_classics' : 'new_classics.html',
        'palais' : 'palais.html',
        'luxury_vinyl_1' : 'luxury_vinyl_1.html',
        'luxury_vinyl_2' : 'luxury_vinyl_2.html',
        'vinyl_deLuxe_classic' : 'vinyl_deLuxe_classic.html',
        'porcelain':'porcelain.html',
        'atelier_series_luxury_performance_vinyl':'atelier_series_luxury_performance_vinyl.html',
        'vinyl_deluxe_grand':'vinyl_deluxe_grand.html'
    }

    baseUrl = 'http://duchateau.com'

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
                files = glob.glob(self.dstFolder + '/*')
                for f in files:
                    print("... delete {}".format(f))
                    os.remove(f)


    # for debug mode, read mock src and parse the data
    # for release mode, connect to the identified url directly
    def connect(self, filename):
        if self.debugMode:
            print("-> Read mock source {}".format(filename))
            with open(filename, 'r') as myfile:
                rawdataString = myfile.read()
            return rawdataString
        else:
            # TODO: connect to the url server
            print("-> Connect to server")

    def parse(self):
        for key in self.collectionList:
            filename = self.collectionList[key]
            rawdata = self.connect(filename)
            bsObj = BeautifulSoup(rawdata, "html.parser")
            self.parseOneCollection(bsObj, key)

    def parseOneCollection(self, bsObj, key):
        imageDivs = bsObj.findAll("div", {"class": "background"})
        for imgDiv in imageDivs:
            matchedPattern = re.search('url\((.+)\);', str(imgDiv))
            url = matchedPattern.group(1)
            url = self.baseUrl + url
            self.download(url, key)
            time.sleep(1)

    def download(self, url, key):
        matchedPattern = re.search('/[0-9]{2}/(.+)\.([A-Za-z]+)$', url)
        filename = matchedPattern.group(1)
        filetype = matchedPattern.group(2)
        dstName = self.dstFolder + '/' + key.upper() + '_' + filename + '.' + filetype
        urllib.request.urlretrieve(url, dstName)
        print("Downloaded")


dechareauCrawler = DechareauCrawler(True, './result')
dechareauCrawler.envSetup()
dechareauCrawler.parse()
