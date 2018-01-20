#-------------------------------------------------------------------------------
# Name:        OnDiplay_esl_newbooks.py
# Purpose:     Get Alma Analyic via Alma API and write (clean) xml file for:
#              OnDisplay, newbooks, esl collections pages
# Author:      Linda Ackers
#
# Created:     11/21/2016
# Copyright:   (c) ackersl 2016
#-------------------------------------------------------------------------------
from booklistsFunctions import cleanUpFile
from booklistsFunctions import getDataAPI  
   

def main():
    print ('***Creating xml files for OnDisplay****')
    listType = 'OnDisplay'    
    listFiles = ['OnDisplay', 'MainDisplay', 'SecondaryDisplay']    
    for file in listFiles:
        getDataAPI(listType, file)
        cleanUpFile(listType, file)    
    print ('***Creating xml files for esl***')
    listType = 'esl'
    listFiles = ['all','advanced','beginning','intermediate','LC','starter', 'audiobook']    
    for file in listFiles:
        getDataAPI(listType, file)
        cleanUpFile(listType, file)    
    print ('***Creating xml files for newbooks***')
    listType = 'newbooks'
    listFiles = ['B','C_D_E_F','DVD','G', 'H', 'J_K', 'L', 'M', 'N','P', 'PIC', 'Q', 'R', 'S_T']    
    for file in listFiles:
        getDataAPI(listType, file)            
        cleanUpFile(listType, file)          
   
   

if __name__ == '__main__':
    main()
