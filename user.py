#!/usr/bin/python

import os
import urllib2
#import pprint

#pprint.pprint(globals())
#pprint.pprint(locals())

mosurl = 'https://docs.google.com/spreadsheets/d/1Qde18KtJX8rrCtkrtfar8JlG9k8iizJmESvhzPgt_-Y/export?gid=0&format=csv'
csvfile = urllib2.urlopen(mosurl)

# Splitting lines by delimiter
while True:
        buf = csvfile.readline()
        if not buf: break
        namePair = buf.split(',')
        print namePair[0]
        #pprint.pprint(namePair);

