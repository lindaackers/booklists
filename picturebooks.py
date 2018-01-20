#-------------------------------------------------------------------------------
# Name:        picturebooks.py
# Purpose:     Get Alma Analyic via Alma API and write (clean) picturebook xml files
#
# Author:      Linda Ackers
#
# Created:     12/6/2016
# Copyright:   (c) ackersl 2016
#-------------------------------------------------------------------------------
from booklistsFunctions import getPagedListAPI

def main():
    listType = 'PictureBooks'
    getPagedListAPI(listType)    
   
if __name__ == '__main__':
    main()