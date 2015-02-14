#!/usr/bin/env python

import os, os.path
from argparse import ArgumentParser

class Cache(dict):
    """
    contain informations about the directories in the form {path : size_in_byte}
    """
    def __init__(self):
        dict.__init__(self)

    


class CurrentDir():
    """
    contain information of the current directory, give possibility to have action on it
    """
    def __init__(self,path):
        self.path = path
        self.cache = Cache()

    def move_to_subDir(sef,subPath):
        pass
    
    def scan(self):
        """
        lunch a scan, save information in Cache object
        """
        for root, dirs, files in os.walk (self.path, topdown=False):
            #what's comming below gonna change
            filepaths = [os.path.join(root,file) for file in files]
            local_size = sum([os.path.getsize(filepath) for filepath in filepaths])
            local_size += os.path.getsize(root)
            #local_size just contain the size of the directory + its files, but without its sub directory
            #here we had the size of the sub (which is possible because topdown = False)
            for subDir in dirs : 
                local_size += self.cache[os.path.join(root,subDir)]
            #and we stock it in the cache
            self.cache[root]= local_size
           # print root, total_size
            print root, local_size
            
            

#entry to the program
def main():

    parser = ArgumentParser()
    #below get the different options 
    parser.add_argument("-s", "--scan", dest='runScan', default=False, action='store_true', help="scan the given directory")
    parser.add_argument("dir")

    args = parser.parse_args()
    current_dir = CurrentDir(args.dir)
    if (args.runScan):
        current_dir.scan()

#lunch the main method if this file is lucnh as the main script
if __name__=='__main__':
   exit(main())
