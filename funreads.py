#-------------------------------------------------------------------------------
# Name:        funreads.py
# Purpose:     Get Alma Analyic via Alma API and write (clean) funreads xml files
#
# Author:      Linda Ackers
#
# Created:     12/06/2016
# Copyright:   (c) ackersl 2016
#-------------------------------------------------------------------------------
from booklistsFunctions import getPagedListAPI

def main():
    listType = 'FunReads'
    getPagedListAPI(listType)    
   
if __name__ == '__main__':
    main()