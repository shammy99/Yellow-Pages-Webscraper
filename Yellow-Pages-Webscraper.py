import selenium
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Postcode_Details = pd.read_csv("NSW-Postcodes.csv")

for i in range(len(Postcode_Details)):
    Suburb = Postcode_Details.at[i,"Suburb"]
    Postcode = Postcode_Details.at[i,"Postcode"]
    Suburb_Search = str(Suburb) + ", NSW " + str(Postcode)
    #print(Suburb_Search)
    
def Yellow_Page_Search():
    browser = webdriver.Chrome()
    browser.get("https://www.yellowpages.com.au/")
    Trade_Enter = browser.find_element_by_id('clue')
    Trade = "Tree & Stump Removal Services"
    Trade_Enter.send_keys(Trade)
    time.sleep(2)
    browser.find_element_by_id('where').clear()
    Suburb_Enter = browser.find_element_by_id('where')
    Suburb_Enter.send_keys("Blacktown, NSW 2148")
    Search_Button = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/form/div/div[3]/div/button/span')
    Search_Button.click()
    CurrentURL = browser.current_url
    print(CurrentURL)
Yellow_Page_Search()

#login_buttom = browser.find_element_by_id('loginbutton')
#login_buttom.click()

