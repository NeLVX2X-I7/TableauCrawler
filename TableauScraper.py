#!/usr/bin/env python3
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:01:36 2020

@author: Nelusa
"""
import sys
from sys import argv
#from selenium import webdriver
import os
from TableauWorkBooks import WorkBook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium.common.exceptions import StaleElementReferenceException
import random
import time
import re
import numpy
c=0
n=2

def crawlerTableauGallery(j,pages,path,WithWB):
    try:
        driver=webdriver.Chrome()

       
  
  
        #j=1
        #loop through the given No of pages
        while(j<pages+1):
            driver.get('https://public.tableau.com/en-gb/gallery/?tab=viz-of-the-day&type=viz-of-the-day&page='+str(j))
            wait = WebDriverWait(driver, 20)
            #wait until all elements are loaded
            first=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gallery-items-list')))   
            images=first.find_elements_by_tag_name('li')  
            c=1
          
            #loop through all images on a page
            for i in images:
               container= i.find_element_by_class_name("gallery-list-item-container")   
               imagesrc=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div[1]')
               imgTitel=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div/div[1]/div[1]/a').text
               titleText=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div/div[2]/div[1]/div[1]/p').text
               referenceTag=imagesrc.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div[1]/a')
               reference=referenceTag.get_attribute('href')
               image=imagesrc.find_element_by_tag_name('img')
               imageFiles=image.get_attribute('src')
               imageName=image.get_attribute('alt')
               c+=1
               img_name=str(j)+'.'+str(c-1)
               #imageName=re.sub('[^a-zA-Z]+', '', imageName)
               imageName=re.sub(r"^\s+|\s+$", "", imageName)
               imageName=imageName.strip("?")
               imageName=imageName.strip('"')
               imageName=imageName.strip("|")
               imageName=imageName.strip(">")
               imageName=imageName.strip("<")
               imageName=imageName.strip("*")
               imageName=imageName.strip("\\")
               imageName=imageName.strip("/")
           
               print(imageName)
               full_name=imageName+".jpg"
               print(full_name)
              # img = Image.open(imageFiles)
               #img.save("C:\\Users\\Nelusa\\Documents\\Uni\\Master\\HiWi\\CrawlerTableau\\TableauCrawler\\" + img_name)
               try:
                   os.mkdir(imageName)
                   urllib.request.urlretrieve(imageFiles,path+'\\'+imageName+'\\'+full_name)  
                   save_path=path+"\\"+imageName
                   name_of_file=imageName
                   completeName = os.path.join(save_path, name_of_file+".txt")
                   file2write=open(completeName,'w')
                   file2write.write(img_name+':'+imgTitel+'\n')
                   file2write.write(titleText+'\n')    
                   file2write.close()
               
                   if(WithWB):
                       WorkBook(reference,save_path)
                   
               except OSError:
                   print('Already Exists')
               
            j+=1                     
    finally:
        #driver.quit()
        driver.close()
        print("end")
     
def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        rangePage=s.split('-')
        for i in rangePage:
            int(i)
        return True
    except ValueError:
        return False     
def main():
    wrong=True   
    ispath=False
    WithWB=False
    #number=input('Type Range of pages you want to scrape from (e.g:2-4, 1): ')
    #path=input('Give a path:')
    print(len(argv))
    for i in range(1,len(argv)+1):
        if(argv[i-1]=="True"):
            WithWB=True
            #isinstance(argv[i-1],(int))
        elif(is_number_tryexcept(argv[i-1])):
            number=argv[i-1]
        elif(os.path.isdir(argv[i-1])):
            path=argv[i-1]
        else:
            path=os.path.abspath(os.getcwd())
            #print(path)
            number="10"
        

        
   # ispath=os.path.isdir(path)
    
        
    rangePage=number.split('-')
    
    try:
        
      
        if(len(rangePage)==1 and not rangePage[0]=="10"):
            #rangePage.insert(10)
            print(len(rangePage))
            last=rangePage[0]
           # rangePage.append(rangePage[0])
            #print(rangePage[1])
            #rangePage[1]==last
            rangePage.insert(0,1)
            rangePage.append(last)
        elif(len(rangePage)==1):
            
            rangePage.insert(0,1)
            rangePage.append(10)
        print("Page",rangePage[0],rangePage[1])    
        crawlerTableauGallery(int(rangePage[0]),int(rangePage[1]),path,WithWB)   
        wrong=False
    except ValueError:
        print("Typing mistake!")
        
main()           

