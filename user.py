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

useradd -m vii
mkdir -p /home/vii/.ssh
wget -O /home/vii/.ssh/authorized_keys http://pxe-eu.webzilla.com/configs/freebsd/pubkeys/vii.pubkey
chown -R vii:vii /home/vii
chmod 700 /home/vii/.ssh
chmod 644 /home/vii/.ssh/authorized_keys
