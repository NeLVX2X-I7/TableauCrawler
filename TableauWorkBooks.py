# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:31:24 2020

@author: Nelusa
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:51:31 2020

@author: Nelusa
"""

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

import time
import shutil
import os
number = 10

    
def WorkBook(url,path='C:\\Users\\Nelusa\\Documents\\Uni\\Master\\HiWi\\CrawlerTableau\\TableauCrawler\\WorkBooks'):
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : path}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    location = url
    j=0


   # while j< number:
        #location = 'https://public.tableau.com/en-gb/gallery/exploring-history-juneteenth?tab=viz-of-the-day&type=viz-of-the-day'
        #driver.get(location)
    driver.refresh
    #driver.get(location)
   
    
    driver.get(location)

    wait = WebDriverWait(driver, 20)
  #  first=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gallery-page-container"]/div/div/div/div[1]/div[1]/div/div/div/div[2]/ul/a[1]')))
  #  src=first.get_attribute('href')
    
   # location=src
    
    j+=1
    #wait for module, which ha iframe element 
    #wait2=WebDriverWait(driver,20)
    #embedded-viz-wrapper
    title=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gallery-page-container"]/div/div/div/div[2]/div[2]')))
    titleName=title.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div/div[2]/div[2]/div[1]/h2').text

    nex_t=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gallery-page-container"]/div/div/div/div[2]/div[1]')))
    seq = nex_t.find_element_by_xpath('//*[@id="gallery-page-container"]/div/div/div/div[2]/div[1]/iframe')
    #newSrc=seq.get_attribute('src')
    #print(newSrc)
    #wait2=(seq,20)
    
    driver.switch_to.frame(seq)
   
    #waitButton
    nex_t=wait.until(EC.presence_of_element_located((By.ID, 'download-ToolbarButton')))
    element = driver.find_element_by_xpath('//*[@id="loadingGlassPane"]')
    driver.execute_script("arguments[0].style.visibility='hidden'", element)
    newFrame=driver.find_element_by_xpath('//*[@id="download-ToolbarButton"]')
    newFrame.click()
    try:
        #waitDownloadFrametoOpen
        wait = WebDriverWait(newFrame, 20)
        nex_t= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="DownloadDialog-Dialog-Body-Id"]/div/button[6]')))
        nex_t.click()
        wait = WebDriverWait(driver, 20)
        newFrame=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="DownloadAsVersionDialog-Dialog-Body-Id"]/div/div[3]/button')))
        newFrame.click()
 
        driver.switch_to_default_content
        driver.refresh
    #for workbooks with no permission to download
    except:
        
        
        driver.switch_to_default_content
        
        driver.refresh
    driver.quit    
    driver.close        
   
    
#WorkBook('https://public.tableau.com/en-gb/gallery/access-water-and-sanitation-around-world?tab=viz-of-the-day&type=viz-of-the-day','C:\\Users\\Nelusa\\Documents\\Uni\\Master\\HiWi\\CrawlerTableau\\TableauCrawler\\WorkBooks')
    
     
       
    