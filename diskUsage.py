#!/usr/bin/env python

import os, os.path


class Cache(dict):
    """
    contain informations about the directories in the form {path : size_in_byte}
    """
    def __init__(self):
        pass

    


class CurrentDir():
    """
    contain information of the current directory, give possibility to have action on it
    """
    def __init__(self,path):
        pass
    
    def move_to_subDir(sef,subPath):
        pass
    
    def scan(self):
        """
        lunch a scan, save information in Cache object
        """
        pass


#entry to the program
def main():
    pass

#lunch the main method if this file is lucnh as the main script
if __name__=='__main__':
   exit(main())
