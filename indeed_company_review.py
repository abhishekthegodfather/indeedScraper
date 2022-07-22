from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def indeed_review(company_name):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://in.indeed.com/companies?from=gnav-acme--acme-webapp')

    ser = driver.find_element(By.ID, 'ifl-InputFormField-3')
    ser.send_keys(company_name)

    btn = driver.find_element(By.CLASS_NAME, 'css-wmdpsd.e8ju0x51')
    btn.click()

    getURL = driver.find_element(By.CSS_SELECTOR, 'a.css-p6v9z3.eu4oa1w0')
    reviewURL = str(getURL.get_attribute('href'))

    driver.get(reviewURL)

    time.sleep(10)
    majorRev = driver.find_elements(By.CSS_SELECTOR, 'span > span.css-82l4gy.eu4oa1w0')
    str1 = ""   
    for i in majorRev:
        str1 += i.text + "\n"

    with open('review.txt', 'a') as file:
        file.write(str1)


    time.sleep(10)
    rating_stars = driver.find_elements(By.CSS_SELECTOR, "button.css-1c33izo.e1wnkr790")
    rat_stars = []
    for i in rating_stars:
        i = i.text
        rat_stars.append(i)
    print(rat_stars)

    str2 = ""
    for i in rat_stars:
        str2 += i+"\n"
    with open('review.txt', 'a') as file:
        file.write("**********Company Review rating out of 5******************")
        file.write(str2)

    driver.close()

company_name = input("Name of the Company to scrap: ")
indeed_review(company_name)
