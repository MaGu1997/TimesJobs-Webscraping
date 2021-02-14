from bs4 import BeautifulSoup
import requests
import time
# Scraping the timesjobs website for python related jobs
unfamiliar_skills = input('>')
print(f'Filering out:{unfamiliar_skills}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ','') # replace method replaces spaces with ''
            skills=job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:

                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f'More Info:{more_info}\n')
                print(f'File Saved:{index}')



if __name__== '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting: {time_wait} minutes...')
        time.sleep(time_wait * 60)

        # print(published_date)
        # print(f'''
        # Company Name:{company_name}
        # Required Skills: {skills}
        # ''')
# print(skills)
# print(company_name)
# print(html_text)
