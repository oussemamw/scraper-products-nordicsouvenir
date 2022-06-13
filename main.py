from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import csv

driver = webdriver.Chrome()

driver.get('https://www.nordicsouvenir.com/')

table_info = ['title', 'price', 'description', 'image', 'sub_categ', 'categ']


csv_data=[]

categ_link=["https://www.nordicsouvenir.com/produkter/nyheter","https://www.nordicsouvenir.com/produkter/gosedjur","https://www.nordicsouvenir.com/produkter/magnet","https://www.nordicsouvenir.com/produkter/nyckelringar","https://www.nordicsouvenir.com/produkter/muggar-skalar-glas","https://www.nordicsouvenir.com/produkter/hemmet","https://www.nordicsouvenir.com/produkter/figur","https://www.nordicsouvenir.com/produkter/skriv-leksaker","https://www.nordicsouvenir.com/produkter/flagga-dekal-pin","https://www.nordicsouvenir.com/produkter/klader-vaskor","https://www.nordicsouvenir.com/produkter/ovrigt"]
categ_name=["Nyheter","Gosedjur","Magnets","Nyckelringar","Muggar, skålar & glas","Hemmet","Figurer","Skriv- & Leksaker","Flagga dekal & pin","Kläder & väskor","Övrigt"]

def crawl(d,categ):
    data={}

    for product in d:
        
        driver.get(product)
        data['title']=driver.find_element_by_id('ctl00_main_ctl00_ctl00_labName').text
        data['price']=driver.find_element_by_id('ctl00_main_ctl00_ctl00_labPrice2').text
        data['description']=driver.find_element_by_id('ctl00_main_ctl00_ctl00_tabContent_pnlProductDescription_productDescription').text
        data['image']=driver.find_element_by_id('FrontImage').get_attribute("src")
        
        data['categ']=categ
        csv_data.append(data)
        

            
        data={}
for link in categ_link:
    driver.get(link)
    list=[]
    while True:
        time.sleep(3)
        try:
            driver.find_element_by_class_name("action--dynamicFilter-fetch-products").click()

        except:
            break

    products_id=driver.find_elements_by_class_name('product-outer-wrapper')
    for product in products_id:

        product_link=driver.find_element_by_xpath('//a[@data-productid="'+str(product.get_attribute('product-id'))+'"]')
        list.append(product_link.get_attribute('href'))

    categ=categ_link.index(link)


    crawl(list,categ_name[categ])


    
with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = table_info)
        writer.writeheader()
        writer.writerows(csv_data)

        