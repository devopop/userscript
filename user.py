#!/usr/bin/python

import os
<<<<<<< HEAD
=======
import os.path
>>>>>>> 00c1d061ed64c3dfddbd3745a10b0a36816be516
import urllib2
import re
import pwd
import grp

<<<<<<< HEAD
#import pprint

from subprocess import call

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
    regexp = re.compile('^\s+?ssh-rsa\s+')
    if regexp.search(key) is not None:
        print 'matched'
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
=======
from subprocess import call

HOMEDIR = "/home/"
FILE2SAVE = "mos.csv"


# User creation
def createuser( name ):
    upath = HOMEDIR + name + "/.ssh"

    try:
        pwd.getpwnam( name )
    except KeyError:
        call( ["useradd", "-m", name] )
#    else:
#        print "User already exists!"

    if not os.path.isdir( upath ) or not os.access( upath, os.R_OK ):
        os.makedirs( upath )
        os.chmod( upath, 0700 )
        chuf( upath,name )
        call( ["usermod", name, "-a", "-G", "libvirtd", "-s", "/bin/bash"] )

# Key processing
def addkey( name, key ):
    regexp = re.compile( '^(\s+)?(ssh-rsa|ssh-dss)\s+[A-Za-z0-9+/=]+(?:\s+)?' )
    if regexp.match( key ) is not None:
        fpath = HOMEDIR + name + "/.ssh/authorized_keys"
        file = open( fpath, "a" )
        file.write( key )
        file.close()
        chuf( fpath,name )
        os.chmod( fpath, 0644 )

# Key accuracy and existance check
def checkkey( name, key ):
    fpath = HOMEDIR + name + "/.ssh/authorized_keys"
    regexp = re.compile( '^(\s+)?(ssh-rsa|ssh-dss)\s+[A-Za-z0-9+/=]+(?:\s+)?' )
    if regexp.match( key ) is not None:
        newPair = key.split(' ')
        if os.path.isfile( fpath ) and os.access( fpath, os.R_OK ):
            file = open( fpath, "r" )
            if file is not None:
                while True:
                    buf = file.readline()
                    if not buf:
                        file.close()
                        break
                    oldPair = buf.split(' ')
                    
                    if oldPair[0] == newPair[0] and oldPair[1] == newPair[1]:
                        print "Duplicate found!"
                        return None;
                return 1
            
            return None;
    else:
        return None;

# File owner change
def chuf( path, name ):
    uid = pwd.getpwnam( name ).pw_uid
    gid = grp.getgrnam( name ).gr_gid
    os.chown( path, uid, gid )



mosurl = 'https://docs.google.com/spreadsheets/d/1Qde18KtJX8rrCtkrtfar8JlG9k8iizJmESvhzPgt_-Y/export?gid=0&format=csv'
#mosurl2 = 'https://docs.google.com/spreadsheets/d/1rTkGAuvqeIV7g1FteVoRs9CRiNR8wmmbaQs_ktIGH4w/export?gid=0&format=csv'
csvfile = urllib2.urlopen(mosurl)
#csvfile = urllib2.urlopen(mosurl2)

if 'csvfile' in locals():
    file = open( FILE2SAVE, "w" )
    file.write( csvfile.read() )
    file.close()

#csvfile = open( FILE2SAVE, "r" )

# User/key pair process
if csvfile is not None:
    while True:
            buf = csvfile.readline()
            if not buf: break
            namePair = buf.split(',')
            print namePair
            if len( namePair ) == 2 and len( namePair[0] ) > 0 and len( namePair[1] ) > 0:
                createuser( namePair[0] )
                if ( checkkey( namePair[0],namePair[1] ) ):
                    addkey( namePair[0], namePair[1] )

    csvfile.close()
>>>>>>> 00c1d061ed64c3dfddbd3745a10b0a36816be516
