import selenium
from bs4 import BeautifulSoup as soup
import pandas as pd
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Postcode_Details = pd.read_csv("NSW-Postcodes.csv")
from Postcodes_NSW import Suburbs_And_Postcodes
Company_Names = []
Emails = []
Phone_Numbers = []
Suburbs = []
Postcodes = []

def Browser_Start():
    global browser
    browser = webdriver.Chrome()
    
def Suburb_And_Postcode(Suburb_To_Search):
    global Postcode, Suburb
    Suburb = Suburb_To_Search
    Postcode = Suburbs_And_Postcodes[Suburb]
    Suburb_Search = str(Suburb) + ", NSW " + str(Postcode)
    print(Suburb_Search)
    Browser_Start()
    Yellow_Page_Search(Suburb_Search)
    Web_Scrape()
    Quit_Browser()
    Export_CSV()

def Main():
    for i in range(len(Postcode_Details)):
        Suburb = Postcode_Details.at[i,"Suburb"]
        Postcode = Postcode_Details.at[i,"Postcode"]
        Suburb_Search = str(Suburb) + ", NSW " + str(Postcode)
        print(Suburb_Search)
        Yellow_Page_Search(Suburb_Search)
        Web_Scrape()
        Quit_Browser()
    
def Yellow_Page_Search(Suburb_Search):
    browser.get("https://www.yellowpages.com.au/")
    Trade_Enter = browser.find_element_by_id('clue')
    Trade = "Tree & Stump Removal Services"
    Trade_Enter.send_keys(Trade)
    time.sleep(2)
    browser.find_element_by_id('where').clear()
    Suburb_Enter = browser.find_element_by_id('where')
    Suburb_Enter.send_keys(Suburb_Search)
    Search_Button = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/form/div/div[3]/div/button/span')
    Search_Button.click()
    CurrentURL = browser.current_url
  
def Web_Scrape():
    Search_Results_Xpath = '//*[@id="search-results-page"]/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[2]/div'
    content_element = browser.find_element_by_xpath(Search_Results_Xpath)
    content_html = content_element.get_attribute("innerHTML")

    page_soup = soup(content_html, "html.parser")
    Contact_Container = page_soup.findAll("div",{"class":"cell in-area-cell find-show-more-trial middle-cell"})
    num_contacts = len(Contact_Container)
    for i in range(num_contacts):
        print ("Search Result: " + str(i))
        Company_Name_Container = Contact_Container[i].findAll("a",{"class":"listing-name"})
        Suburbs.append(Suburb)
        Postcodes.append(Postcode)
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

def Quit_Browser():
    browser.quit()

def Export_CSV():
    Company_Name_Table = pd.DataFrame({'Company Name': Company_Names})
    Phone_Numbers_Table = pd.DataFrame({'Phone Number': Phone_Numbers})
    Emails_Table = pd.DataFrame({'Email': Emails})
    Suburbs_Table = pd.DataFrame({'Suburb': Suburbs})
    Postcode_Table = pd.DataFrame({'Postcode': Postcodes})
    Final_Table = pd.concat([Company_Name_Table, Phone_Numbers_Table, Emails_Table, Suburbs_Table, Postcode_Table], axis=1)
    print(Final_Table)
    Final_Table.to_csv(str(Suburb) + " Tree Loppers.csv")
    #print("The Table has been stored as 'Completed Plant Schedule.csv'! ")
#Main()
