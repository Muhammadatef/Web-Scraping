import time
from bs4 import BeautifulSoup
import requests
# with open('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'html.parser')
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
#         # print(course_name)
#         # print(course_price)

#         print(f'{course_name} costs {course_price}')

print("Put some skill that you are not familiar with")
unfamiliar_skill = input('')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'html.parser')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        # print(job)
        job_date = job.find('span', class_='sim-posted').text
        if 'few' in job_date:
            job_skill = job.find('span', class_='srp-skills').text.replace(' ', '')
            company_name= job.find('h3',  class_='joblist-comp-name').text.replace(' ', '')
            job_link = job.header.h2.a['href']
            if unfamiliar_skill not in job_skill:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills: {job_skill.strip()} \n")
                    f.write(f"Job Link : {job_link} \n")
                    print(f'File Saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)