#!/usr/bin/python

import os
import urllib2
from subprocess import call

import pwd
import grp

#import pprint

#pprint.pprint(globals())
#pprint.pprint(locals())

HOMEDIR = "/home/"

def createuser( name ):
    call(["useradd", "-m", name])
    upath = HOMEDIR + name + "/.ssh"
    os.mkdirs(upath)
    os.chmod(upath, 0700)
    uid = pwd.getpwnam(name).pw_uid
    gid = grp.getgrnam(name).gr_gid
    os.chown(upath,uid,gid)
    call(["usermod", name, "-a -G", "libvirtd"])
    call(["usermod", name, " -s /bin/bash"])
    #os.chown(upath,os.getuid(name),os.getgid(name))
    #call(["useradd", "-m", name])

def addkey( name, key ):
    #print len(name), len(key)
    upath = HOMEDIR + name + "/.ssh/authorized_keys"
    file = open(upath, "w")
    file.write(key)
    file.close()
    os.chmod(upath, 0644)

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

csvfile.close()
        #pprint.pprint(namePair);

#call(["useradd", "-m", namePair[0]])
