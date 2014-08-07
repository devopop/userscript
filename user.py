#!/usr/bin/python

import os
import urllib2
from subprocess import call
#import pprint

#pprint.pprint(globals())
#pprint.pprint(locals())

HOMEDIR = "/home/"

def createuser( name ):
    print len(name)
    #call(["useradd", "-m", name])

def addkey( name, key ):
    print len(name), len(key)

#mosurl = 'https://docs.google.com/spreadsheets/d/1Qde18KtJX8rrCtkrtfar8JlG9k8iizJmESvhzPgt_-Y/export?gid=0&format=csv'

#csvfile = urllib2.urlopen(mosurl)

if 'csvfile' in locals():
    file = open("mosurl.txt", "w")
    file.write(csvfile.read())
    file.close()

csvfile = open("mosurl.txt", "r")

# Splitting lines by delimiter
while True:
        buf = csvfile.readline()
        if not buf: break
        namePair = buf.split(',')
        if len(namePair) == 2 and len(namePair[0]) > 0 and len(namePair[1]) > 0:
            #createuser(namePair[0])
            addkey(namePair[0],namePair[1])

        #pprint.pprint(namePair);

#call(["useradd", "-m", namePair[0]])
