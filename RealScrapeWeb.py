from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with:')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').text.replace(' ', '')
        if 'few' in date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill.lower() not in skills:
                # w is for writing inside a file
                with open('posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')
                    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10  # in minutes
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)


"""
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
"""

