# This is Scratch file for Webscraping
# Using BeautifulSoup and Selenium

#!/usr/bin/python
# -*- coding: UTF-8 -*-


## -- This is the first Try -- 
# from googlesearch import search
#
# # List of CEOs and their company domains
# ceo_domains = {
#     "GARY HERSHAM": "beauchamp.com",
#     "William Lindsay Bell": "bbrroofing.co.uk",
#     "Paul Philpott": "tmsmotorgroup.co.uk",
#     "Martin Dodd": "huntswood.com",
#     "Jumoke Ogundare": "arm.com",
#     "Julian Hamood": "trustedtechteam.com",
#     "Gonçalo Cardador": "oneenergyprojects.com",
#     "Phillip Palmer": "teknobu.co.uk",
#     "Ryan Roslansky": "linkedin.com",
#     "George Ogden": "srcf.net",
#     "Jonathan Gibson": "wellsgibson.uk",
#     "Brian Bachelor": "e-van-guru.co.uk",
#     "Grzegorz Witkowski": "insignistfi.pl",
#     "Patrick Andersen": "cwt.org.uk",
#     "Paul Lindley": "reading.ac.uk",
#     "Mark Newall": "bchnarchitects.co.uk",
#     "Paul Sanderson": "recyclingexpo.co.uk",
#     "Yatin Manuel": "halvex.net",
#     "Dave Trolle": "customerfirstdigital.com",
#     "Nancy Lindborg": "responsez.org",
#     "Aleesha Brown": "amexoutsourcing.com",
#     "David Souza": "teamworkswarwick.com",
#     "Martin Jennings": "parmenion.co.uk",
#     "Tom Vernon": "stateraenergy.co.uk",
#     "Mohammed Abuhijleh": "forvismazars.com",
#     "Fergal Mullen": "highlandeurope.com",
#     "Ayman Rahman": "dare.global",
#     "Darren McDermott": "drvnautomotivegroup.com",
#     "Nick Emery": "jellyfish.com",
#     "Edward Canty": "centrefield.law",
#     "Espen Skogen": "rocketfin.co",
#     "Debbie.Poulten": "harrisstjohnswood.org.uk",
#     "Anthony Koumi": "bullybillows.com",
#     "Neil Armstrong": "unitedliving.co.uk",
#     "Gary Perry": "altecnic.co.uk",
#     "Brad Karp": "paulweiss.com",
#     "Alexandre J. L'Heureux": "wsp.com",
#     "David Ross": "ardonagh.com",
#     "Nerio Alessandri": "technogym.com"
# }
#
# # Function to search for CEO of a company domain
# def search_ceo(company_domain):
#     query = f"CEO of {company_domain}"
#     for j in search(query, num=1, stop=1, pause=2):
#         return j
#
# # Loop through each CEO and search for the CEO of their respective company domain
# for ceo, domain in ceo_domains.items():
#     ceo_search_result = search_ceo(domain)
#     print(f"CEO for {domain}: {ceo_search_result}")


## Second Try, using BeautifulSoup

"""
from bs4 import BeautifulSoup
import requests

# Specify the URL of the webpage you want to scrape
url = "URL_OF_THE_WEBPAGE"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the HTML elements containing CEO names (You need to inspect the webpage's HTML structure to find the relevant elements)
ceo_elements = soup.find_all('tag', class_='ceo-class')  # Example: Replace 'tag' and 'ceo-class' with actual HTML tags and classes

# Extract and print the CEO names
for element in ceo_elements:
    ceo_name = element.text
    print(ceo_name)
"""

## Third Try using Selenium


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Specify the LinkedIn profile URL you want to scrape
url = "https://uk.linkedin.com/in/andrewwafer"

driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(5)
ceo_element = driver.find_element(By.XPATH, "//html/body/main/section[1]/div/section/section[1]/div/div[2]/div[1]/button/h1")

ceo_name = ceo_element.text

print("CEO Name: ", ceo_name)


driver.quit()
