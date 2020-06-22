# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:01:36 2020

@author: Nelusa
"""
import sys
#from selenium import webdriver
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium.common.exceptions import StaleElementReferenceException
import random
import time

c=0
n=2
def crawlerTableauGallery(pages):
    try:
        driver=webdriver.Chrome()

       
  
  
        j=1
        #loop throug the given No of pages
        while(j<pages+1):
            driver.get('https://public.tableau.com/en-gb/gallery/?tab=viz-of-the-day&type=viz-of-the-day&page='+str(j))
            wait = WebDriverWait(driver, 20)
            #wait until all elements are loaded
            first=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gallery-items-list')))   
            images=first.find_elements_by_tag_name('li')  
            c=1
            file2write=open("GalleryText",'w')
            #loop through all images on a page
            for i in images:
               container= i.find_element_by_class_name("gallery-list-item-container")   
               imagesrc=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div[1]')
               imgTitel=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div/div[1]/div[1]/a').text
               titleText=container.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div[2]/section/div/ol/li['+str(c)+']/div/div/div[2]/div[1]/div[1]/p').text
               image=imagesrc.find_element_by_tag_name('img')
               imageFiles=image.get_attribute('src')
               c+=1
               img_name=str(j)+'.'+str(c-1)
               full_name=str(img_name)+".jpg"
               urllib.request.urlretrieve(imageFiles,full_name)     
               file2write.write(img_name+':'+imgTitel+'\n')
               file2write.write(titleText+'\n')              
            j+=1                     
    finally:
        driver.quit()
        file2write.close()
        

crawlerTableauGallery(1)
