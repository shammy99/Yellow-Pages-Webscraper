import selenium
from bs4 import BeautifulSoup as soup
import pandas as pd
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
browser = webdriver.Chrome()

Company_Names = []
Emails = []
Phone_Numbers = []

url = "https://www.yellowpages.com.au/search/listings?clue=Tree+%26+Stump+Removal+Services&locationClue=Blacktown%2C+NSW+2148&lat=&lon="
browser.get(url)
Search_Results_Xpath = '//*[@id="search-results-page"]/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[2]/div'
content_element = browser.find_element_by_xpath(Search_Results_Xpath)
content_html = content_element.get_attribute("innerHTML")

page_soup = soup(content_html, "html.parser")
print(page_soup.prettify())
Contact_Container = page_soup.findAll("div",{"class":"cell in-area-cell find-show-more-trial middle-cell"})
num_contacts = len(Contact_Container)
for i in range(num_contacts):
    print ("Search Result: " + str(i))
    Company_Name_Container = Contact_Container[i].findAll("a",{"class":"listing-name"})
    for x in range(len(Company_Name_Container)):
        Company_Name = Company_Name_Container[x].contents
        Company_Name = Company_Name[0]
        print (Company_Name)
        Company_Names.append(Company_Name)
    Phone_Number_Container = Contact_Container[i].findAll("span",{"class":"contact-text"})
    for x in range(len(Company_Name_Container)):
        Phone_Number = Phone_Number_Container[x].contents
        Phone_Number = Phone_Number[0]
        print (Phone_Number)
        Phone_Numbers.append(Phone_Number)
    Email_Container = Contact_Container[i].findAll("a",{"class":"contact contact-main contact-email"})
    try:
        Email = Email_Container[0].get("data-email")
        print(Email)
        Emails.append(Email)
    except:
        Email = "No Email Given!"
        print(Email)
        Emails.append(Email)
    print("\n")
        
