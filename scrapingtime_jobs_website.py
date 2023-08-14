# Import necessary libraries
import time
from bs4 import BeautifulSoup
import requests

# Uncomment the following lines to read HTML content from a local file
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

# Get input from the user for an unfamiliar skill
print("Put some skill that you are not familiar with")
unfamiliar_skill = input('')
print(f'Filtering out {unfamiliar_skill}')

# Define a function to find jobs
def find_jobs():
    """
    Scrapes job listings from timesjobs.com based on the specified skill and filters out jobs requiring the unfamiliar skill.
    Saves job details to separate text files.

    Returns:
        None
    """
    # Send an HTTP GET request to the job search page
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all job listings on the page
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        # Get the posted date of the job
        job_date = job.find('span', class_='sim-posted').text

        # Check if the job was posted recently
        if 'few' in job_date:
            # Get the required skills for the job
            job_skill = job.find('span', class_='srp-skills').text.replace(' ', '')

            # Get the company name
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')

            # Get the job link
            job_link = job.header.h2.a['href']

            # Check if the job requires the unfamiliar skill
            if unfamiliar_skill not in job_skill:
                # Write job details to a text file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills: {job_skill.strip()} \n")
                    f.write(f"Job Link : {job_link} \n")
                    print(f'File Saved: {index}')

# Main code execution starts here
if __name__ == '__main__':
    while True:
        # Call the find_jobs function to scrape and filter job listings
        find_jobs()

        # Set the waiting time interval in minutes
        time_wait = 10

        # Print a message and wait for the specified time
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
