
# install selenium and chromedriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import math
import pandas as pd
import os
import time
class ScrapeFunction:

    def setup_chrome():
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    
        return chrome_options
    # This functions scraps the website "https://askdruniverse.wsu.edu/"
    # csv file is saved as "query + "_" +  website_name" + .csv
    def scrape_askdruniverse(search_query, website, website_link,chrome_options, total_link_results):
    
        # to get to the search element in the browser
        browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH") ,options=chrome_options)
        browser.get(website_link)
        search_element = browser.find_element_by_id("site-header-widgets-open").click()
        time.sleep(2)
        search_element = browser.find_element_by_name("s")
    
        # send the query to the search element
        search_element.send_keys(search_query)
        search_element.send_keys(Keys.RETURN)
    
        df = pd.DataFrame(columns=['links'])
    
        filename = search_query + '_' + website + '.csv'
    
        row_count = 0
    
        # gets all the links from the webpage as a result of search query
        # and writes it to the csv file
        titles = browser.find_elements_by_class_name("article-title")
        for title in titles:
            link = title.find_element_by_css_selector('a').get_attribute('href')
            df.loc[row_count] = link
            row_count+=1
            if row_count == total_link_results:
                break
        df.to_csv(filename,index=False)
        browser.quit()
    
    # This functions scraps the website "https://www.teachengineering.org/k12engineering/what"
    # csv file is saved as "query + "_" +  website_name" + .csv
    def scrape_teachengineering(search_query, website, website_link,chrome_options, total_link_results):
    
        browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"),options=chrome_options)
        browser.get(website_link)
    
        # to get to the search element in the browser
        # and send the query to the search element
        time.sleep(2)
        search_element = browser.find_element_by_name("q")
        search_element.send_keys(search_query)
        search_element.send_keys(Keys.RETURN)
    
    
        # to get access to the number of results that is spread
        # across number of total number of pages
        # We divide total results by number of results shown per page
        time.sleep(2)
        links = browser.find_elements_by_class_name("col-md-9")
        centernav = links[0].find_elements_by_class_name('text-center')[0]
        li = centernav.find_elements_by_tag_name('li')
        span_text = li[2].find_elements_by_tag_name('span')[0]
        text = span_text.get_attribute('innerHTML')
        split_text = text.split(" ")
        total_results = split_text[-1]
        number_of_pages = math.ceil(float(total_results)/10)
    
        df = pd.DataFrame(columns=['links'])
        filename = search_query + '_' + website + '.csv'
        row_count=0
        links_list = []
    
    
        # to store all the links of all pages to csv
        for i in range(number_of_pages):
            time.sleep(1)
            links = browser.find_elements_by_class_name("col-md-9")
            table = links[0].find_elements_by_tag_name('table')[0]
            tbody = table.find_elements_by_tag_name('tbody')[0]
            td = tbody.find_elements_by_tag_name('td')
            for row in td:
                a = row.find_elements_by_tag_name('a')[0]
                df.loc[row_count] = a.get_attribute('href')
                row_count+=1
    
                if row_count == total_link_results:
                    break
    
    
            if row_count == total_link_results:
                break
    
    
            centernav = links[0].find_elements_by_class_name('text-center')[0]
            li = centernav.find_elements_by_tag_name('li')
            li[3].find_elements_by_tag_name('a')[0].click()
    
        df.to_csv(filename,index=False)
        browser.quit()
    
    # web scraper for two websites:
    # 1) https://askdruniverse.wsu.edu/
    # 2) https://www.teachengineering.org/k12engineering/what
    def scrapWebsite(self, search_query, website, total_results):
    
        # do the initial set up, so that we don't see the browser being opened
        chrome_options = ScrapeFunction.setup_chrome()
    
        if website == 'askdruniverse':
            website_link = 'https://askdruniverse.wsu.edu/'
            ScrapeFunction.scrape_askdruniverse(search_query, website, website_link, chrome_options, total_results)
        if website == 'teachengineering':
            website_link = 'https://www.teachengineering.org/k12engineering/what'
            ScrapeFunction.scrape_teachengineering(search_query, website, website_link, chrome_options, total_results)

#test = ScrapeFunction.scrapWebsite(0,"acid", 'askdruniverse', 5)

