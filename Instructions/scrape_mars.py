#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import time
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


def scrape():
infomars_dict = {}






url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')





type(soup)


# ## Title and News 




title_results = soup.find_all('div', class_="content_title")[0].find('a').text.strip()
print(title_results)




news_results = soup.find_all('div', class_="rollover_description_inner")[0].text.strip()
print(news_results)





#infomars_dict["title_results"] = title_results
#infomars_dict["news_results"] = news_results




#for result in result_two:
   # print(result.text)






#for result in results:
    #print(result.text)



# ##Featured Image 




executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)




url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)





html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#browser.click_link_by_partial_text('FULL IMAGE')

#html = browser.html

#sidebar = soup.find()





address_find = soup.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()





featured_image="https://www.jpl.nasa.gov"+address_find
print(featured_image)




#infomars_dict["featured_image"]=featured_image

print(featured_image)


# #weather




executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)







   # Visit visitcostarica.herokuapp.com
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)





html = browser.html
soup = BeautifulSoup(html, "html.parser")





avg_temps = soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text





#infomars_dict["avg_temps"]= avg_temps
print(avg_temps)


# #mars facts




url = 'https://space-facts.com/mars/'





tables = pd.read_html(url)
tables





df = tables[0]
df.columns = ['description','value']

df.head()





#below conversts the above table to HTML and makes it a .html file 
#df.to_html('table.html')







#new_html_table= html_table.replace('\n','')
#infomars_dict['Facts'] = new_html_table


# ##mars Hemisperes


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)





html = browser.html
soup = BeautifulSoup(html, "html.parser")





image_url= []





dict = {}





results = soup.find_all('h3')






for result in results:
    item = result.text
    time.sleep(1)
    browser.click_link_by_partial_text(item)
    #browser.find_link_by_partial_text(item)[0].click()
    time.sleep(1)
    html=browser.html
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)
    image_find = soup.find_all('div', class_="downloads")[0].find_all('a')[0].get("href")
    time.sleep(1)
    #image_find = soup.find('img', class_='wide-image')['src']
    #title = soup.find('h2', class_='title').text
    dict["title"]= item
    dict["img_url"]= image_find
    image_url.append(dict)
    dict ={}
    #dict["img_url"] = "https://astrogeology.usgs.gov" + image_find
    #dict["title"] = title
        
    
    browser.back()

#infomars_dict["image_url"]=image_url
    #return infomars_dict





image_url


















