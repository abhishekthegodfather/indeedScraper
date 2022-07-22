from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def indeed_post(job_name):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://in.indeed.com/')

    search = driver.find_element(By.ID, "text-input-what")
    search.send_keys(job_name)

    sbtBtn = driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
    sbtBtn.click()

    time.sleep(10)
    RoleName = driver.find_elements(By.CSS_SELECTOR, "a.jcs-JobTitle")
    name_Role = []
    for i in RoleName:
        i = i.text
        name_Role.append(i)
    print(name_Role)

    time.sleep(10)
    CompanyName = driver.find_elements(By.CSS_SELECTOR, "span.companyName>a.turnstileLink")
    name_Company = []
    for i in CompanyName:
        i = i.text
        name_Company.append(i)
    print(name_Company)

    time.sleep(10)
    CompanyLocation = driver.find_elements(By.CSS_SELECTOR, "div.companyLocation")
    loc_Company = []
    for i in CompanyLocation:
        i = i.text
        loc_Company.append(i)
    print(loc_Company)

    time.sleep(10)
    CompanyRating = driver.find_elements(By.CSS_SELECTOR, "span.ratingNumber")
    rat_Company = []
    for i in CompanyRating:
        i = i.text
        rat_Company.append(i)
    print(rat_Company)

    time.sleep(10)
    CompanySumamry = driver.find_elements(By.CSS_SELECTOR, "div.job-snippet")
    sum_Company = []
    for i in CompanySumamry:
        i = i.text
        i = i.replace('\n', ' ')
        sum_Company.append(i)
    print(sum_Company)

    data = pd.DataFrame({'Role':pd.Series(name_Role), 'Company Name':pd.Series(name_Company), 'Company Rating':pd.Series(rat_Company), 'Company Location': pd.Series(loc_Company),'Job Summary':pd.Series(sum_Company)})
    data.to_csv("Indeed_scap.csv")
    driver.close()

job_name = input("Name the job you want to scrap: ")
indeed_post(job_name)