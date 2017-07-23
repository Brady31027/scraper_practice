
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

for k in collectionList:
    mock_file = k + '.html'
    try:
        print("pass at {}".format(k))
        f = open(collectionList[k], 'r')
    except IOError:
        print("error happened at {}".format(k))
        pass