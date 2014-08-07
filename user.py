#!/usr/bin/python

import os
#import csv
import urllib2
import StringIO

#os.stat('./.pip')

mosurl = 'https://docs.google.com/spreadsheets/d/1Qde18KtJX8rrCtkrtfar8JlG9k8iizJmESvhzPgt_-Y/export?gid=0&format=csv'
csvfile = urllib2.urlopen(mosurl)

#print csvfile.splitlines();

while True:
        buf = csvfile.readline();
        if not buf: break
        #reader = csv.reader(buf,delimiter=',',quoting=csv.QUOTE_NONE)
        print buf.split(',')

