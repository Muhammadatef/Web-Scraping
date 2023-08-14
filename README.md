# Job Search and Filtering Script

This is a Python script that scrapes job listings from a job search website and filters them based on a specified skill. It saves relevant job details to separate text files for further analysis.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)


## Description

The script uses the BeautifulSoup library to parse the HTML content of a job search website and extract job listings' details. It then filters out jobs that require a specific skill that you're not familiar with. The relevant job details are saved to individual text files for later reference.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/job-search-script.git
```



1-Navigate to the project directory:
cd job-search-script

2-Run the script by executing the following command:

python job_search.py

3- Follow the instructions in the terminal to enter the skill you're not familiar with. The script will then start scraping job listings, filtering out unwanted jobs, and saving the relevant details to text files.

The script will run in a loop with a specified interval. It will keep searching for new jobs and filtering them as long as the script is running.


#Installation

Make sure you have Python 3.x installed on your system.

Install the required dependencies using pip:

pip install beautifulsoup4 requests

#Dependencies

 BeautifulSoup: A library for pulling data out of HTML and XML files.
 Requests: A library for making HTTP requests.

#Configuration

You can customize the behavior of the script by modifying the following variables:

unfamiliar_skill: Replace this with the skill you're not familiar with.
time_wait: Set the waiting time interval (in minutes) between job search cycles.

#Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, feel free to create a pull request.
