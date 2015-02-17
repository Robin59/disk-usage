#!/usr/bin/env python

import os, os.path
from argparse import ArgumentParser

class byte(int):
    """
    class for a better reprensetation of the bytes
    """
    #conversion list for bytes
    conv = [(2**(10*4),'TiB'),(2**(10*3),'GiB'),(2**(20),'MiB'),(2**(10),'KiB'),(1,'B')]
    #def __init__(self):
    
    def __repr__(self):
        for (value,unit)in self.conv :
            if self>=value :
                if self%value ==0 :
                    return "{:3d} {}".format(self/value,unit)
                else:
                    return "{:3.2f} {}".format(float(self)/value,unit)
        return "" #for the 0 case
    
    __str__ = __repr__

class Cache(dict):
    """
    contain informations about the directories in the form {path : size_in_byte}
    """
    def __init__(self):
        dict.__init__(self)

    def __getitem__(self, directory):
        try:
            return dict.__getitem__(self,directory)
        except KeyError as e :
            print "no data for ", directory
            return 0


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
            #add of the files
            self.cache.update([(filepath,os.path.getsize(filepath)) for filepath in filepaths])
            local_size = sum([os.path.getsize(filepath) for filepath in filepaths])
            local_size += os.path.getsize(root)
            #here we had the size of the sub (which is possible because topdown = False)
            for subDir in dirs : 
                local_size += self.cache[os.path.join(root,subDir)]
            #and we stock it in the cache
            self.cache[root]= local_size
           
    def interact(self):
        """
        this method is for the interaction with the user
        """
        print "" #entre message
        currentPath=self.path
        while True :
            print "Current directory total size :", byte(self.cache[currentPath])
            for subDir in os.listdir(currentPath) :
                print subDir, byte(self.cache[os.path.join(currentPath,subDir)])
            anwser = raw_input("use q to quit")
            currentPath = self.action(currentPath, anwser)

    def action (self, currentPath, rawImput):
       """
       do the appropreate action related to the rawImput
       q for quit, s for a new scan
       """
       if rawImput is 'q' :
           exit(0)
       elif rawImput is 's' :
           self.cache =Cache()
           self.scan()
       return currentPath
            

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
    current_dir.interact()
#lunch the main method if this file is lucnh as the main script
if __name__=='__main__':
   exit(main())
