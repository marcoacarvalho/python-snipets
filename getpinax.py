#!/usr/bin/env python

import os
import sys
import urllib
import tarfile

root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

pinax_ver = 'pinax-0.7beta3'
pinax_url = 'http://downloads.pinaxproject.com/%s.tar.gz' % pinax_ver

def progress(count, block_size, total_size):
    percent = int(count*block_size*100/total_size)
    sys.stdout.write('\rDownloading Pinax' + "...%d%%" % percent)
    sys.stdout.flush()

def main():
    try:
        filename, msg = urllib.urlretrieve(pinax_url, reporthook=progress)
        print os.linesep + 'Done!'
    except:
        sys.exit('Unable to download Pinax.')

    tar = tarfile.open(filename)
    tar.extractall(path=root_dir)
    tar.close()

    urllib.urlcleanup()

if __name__ == '__main__':
    main()

