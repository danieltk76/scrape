from bs4 import BeautifulSoup
from datetime import datetime
# all this does is gather information from the website
import requests

# url = input("Enter the url you want to scrape: #")
current_time = datetime.now()

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="

html_text = requests.get(url).text
# if we get a response 200 then we got the text successfully in terminal
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
#.replace(' ', '') replaces extra white spaces with nothing
company_name = job.find('h3', class_='joblist-comp-name').text.replace('', '')
skills = job.find('span', class_='srp-skills').text.replace('', '')
date = job.find('span', class_='sim-posted').text.replace('', '')
print(f'''
Current date: {current_time}
Company Name:{company_name}
Required Skills:{skills}
{date}
''')

