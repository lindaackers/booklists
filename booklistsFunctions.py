#-------------------------------------------------------------------------------
# Name:        booklistsFunctions.py
# Purpose:     Functions for booklists
#
# Author:      Linda Ackers
#
# Created:     11/21/2016
# Copyright:   (c) ackersl 2016
#-------------------------------------------------------------------------------
import sys, os, time, re  #re for re.search
import requests #http://www.python-requests.org/en/master/
from xml.etree import ElementTree
from array import *

  
def getDataAPI(listType, file): #(ESL, newbooks, OnDisplay) get data and write to file 
    resumptionToken = ''
    IsFinished = 'false'
    myXmlFile = open('temp.xml','w', encoding='utf-8') #must have encoding utf-8!
    count = 1
    while (count <50 or IsFinished =='true'): 
        url = 'https://api-na.hosted.exlibrisgroup.com/almaws/v1/analytics/reports?path=/shared/Lane Community College/Reports/Collections/'+listType+'/'+file+'&limit=25&apikey=[the key]&token='+resumptionToken #api key removed on git
        
        myxml = requests.get(url) #get xml
        #print (myxml.encoding) # get encoding (UTF-8) #debug       
        if myxml.status_code == requests.codes.ok:       
            root = ElementTree.fromstring(myxml.text)
            myXmlFile.write(myxml.text)
            if (count == 1):
                resumptionToken = root[0][0].text # ResumptionToken Value
            IsFinished = root[0][1].text # IsFinished Value 'false' or 'true'
            try:
                findstr = '<IsFinished>false'
                myxml.text.index(findstr)                
                IsFinished = 'false'
            except ValueError:
                IsFinished ='true'
                print(file+' IsFinished: '+IsFinished)
                break                

            count=count+1  
            
            #################################################           
            #print ('status code= '+ str(myxml.status_code)) #debug
            #print (root[0][0].tag) #<ResumptionToken>
            #print (root[0][0].text) # ResumptionToken Value 
            #print (root[0][1].tag) #<IsFinished>
            #print (IsFinished) #debug
            #print(myxml.text) #debug         
            #print (root[0][2].tag) #<ResultXml>
            #print (root[0][2][0].tag) #rowset
            #print (root[0][2][0][1].tag) #Row
            ###################################################     
            
        
        else:
            print ('Cannot get data from the Alma API')
            break
        
    myXmlFile.close()
    
def cleanUpFile(listType, file): #(ESL, newbooks, OnDisplay)
    count = 0
    readFile =  open('temp.xml', 'r', encoding='utf-8') #must have encoding utf-8!)
    writeFile = open(listType+'//'+file+'.xml', 'w', encoding='utf-8') #must have encoding utf-8!)
    with readFile as lines:
        for line in lines:            
            count = count +1
            #print (count) #debug
            if (count <= 24):
                writeFile.write(line)
            if (count > 24):
                #print ('only write lines that start with <Row></Rows> or <column*')
                if re.search('<Column', line):
                    #print ('found it') #debug
                    writeFile.write(line)
                if re.search('<Row', line):
                    writeFile.write(line)
                if re.search('</Row', line):
                    writeFile.write(line)                
                    
    writeFile.write('</rowset>\n</ResultXml>\n</QueryResult>\n</report>') #write closing tags
    readFile.close
    writeFile.close       

def getPagedListAPI(listType): #get data and write to file picturebooks and funreads
    resumptionToken = ''
    IsFinished = 'false'    
    count = 1
    pageNumber = 1
    print ('Starting' +listType)
    while (count <21 or IsFinished =='true'): #max 20 times        
        url = 'https://api-na.hosted.exlibrisgroup.com/almaws/v1/analytics/reports?path=/shared/Lane Community College/Reports/Collections/'+listType+'&limit=100&apikey=[the key]&token='+resumptionToken #api key removed on git
        myXmlFile = open(listType.lower()+'//'+listType.lower()+'_pg'+str(pageNumber)+'.xml','w', encoding='utf-8') #must have encoding utf-8!        
        myxml = requests.get(url) #get xml
        #print (myxml.encoding) # get encoding (UTF-8) #debug       
        if myxml.status_code == requests.codes.ok:       
            root = ElementTree.fromstring(myxml.text)
            myXmlFile.write(myxml.text)
            if (count == 1):
                resumptionToken = root[0][0].text # ResumptionToken Value
            IsFinished = root[0][1].text # IsFinished Value 'false' or 'true'
            try:
                findstr = '<IsFinished>false'
                myxml.text.index(findstr)                
                IsFinished = 'false'
            except ValueError:
                IsFinished ='true'
                print('FunReads IsFinished: '+IsFinished)
                break                

            count=count+1
            pageNumber=pageNumber+1
            
            #################################################           
            #print ('status code= '+ str(myxml.status_code)) #debug
            #print (root[0][0].tag) #<ResumptionToken>
            #print (root[0][0].text) # ResumptionToken Value 
            #print (root[0][1].tag) #<IsFinished>
            #print (IsFinished) #debug
            #print(myxml.text) #debug         
            #print (root[0][2].tag) #<ResultXml>
            #print (root[0][2][0].tag) #rowset
            #print (root[0][2][0][1].tag) #Row
            ###################################################     
            
        
        else:
            print ('Cannot get data from the Alma API')
            break
        
        myXmlFile.close()  
