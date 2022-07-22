# indeedScraper
This Program Scrap the indeed Jobs and its description based on role and make into csv containing all the information about the job. It also scrap the reviews of the company by giving the company name. saves the all the comments, reviews and rating in the form of text files. This Script is written in python3 and the library used is Selenium. This Selenium library handles the all the automation stuff like opening of browser , put request to website fill search box and scraping stuff.

For using the selenium first download the geckodriver driver which is a driver for firefox browser and chromedriver for chrome browser. I used so Firefox browser so, i have included the geckodriver in this repository so, no need to download externally.

> indeed_job.py ---> this files scrap the jobs from the indeed page based on role enter like "analyst"

> indeed_company_review.py ----> the file scrap the company review and the ratings based on the enter company when asked in terminal (during runtime)
