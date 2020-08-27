# TableauCrawler
Scrape images from Tableau Gallery
Prerequisites:
-chromeDriver

TODO:

-Run TableauScraper.

-scrapes by default the images of the first 10 pages of the gallery.

-saves the path by default in the same directory from where the script is running

-If True is typed in as a parameter Workbooks get scraped too

-If path is also given as a parameter the chosen path is selected to save the scraped data

-If a number is given the amount of pages will be scraped:

  -If number is given like : 1-10 or 4-8 ... the given number of pages will be scraped
  
  -If only one number is typed then pages from 1 until given number are scraped
  
-Already existing images or Workbooks in a given directory  will not be downloaded
  
