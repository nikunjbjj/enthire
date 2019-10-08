# Script to scrape mightyrecruiter

import requests
from lxml import html

session_requests = requests.session()
login_url = "https://recruiter.mightyrecruiter.com/login"
payload = {
	"UserName": "Sreetasai@gmail.com",
	"Password": "Wrevie123",
	"IsPersistent": "" 	
}

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'authority': 'recruiter.mightyrecruiter.com',
    'referer': 'https://recruiter.mightyrecruiter.com/accounts',
    'upgrade-insecure-requests': '1',
    'origin': 'https://recruiter.mightyrecruiter.com',
    'content-type': 'application/x-www-form-urlencoded'
}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = headers
)

print ("Login Status code: " + str(result.status_code))

#### Get List of resumes ####
url = "https://recruiter.mightyrecruiter.com/resumes/Get"
params = (
    ('jobID', '0'),
    ('page_number', '1'),
    ('page_size', '20'),
    ('search_on', 'jt'),
    ('search_string', 'software'),
    ('location', ''),
    ('sortBy', 'score'),
    ('radius', '30'),
    ('min_experience', '0'),
    ('max_experience', '1200'),
    ('mned', 'NA'),
    ('min_age', '1'),
    ('max_age', '5000'),
    ('hide_viewed_resume', 'false'),
    ('hide_reviewed_resume', 'false'),
    ('documentId', '0'),
    ('similarResumeSearch', 'false'),
)

resumes_list_result = session_requests.get(url, headers=headers, params=params)
print ("Resumes status code: " + str(resumes_list_result.status_code))

### Loop over the resumes data and fetch the resume HTML ####
json_response = resumes_list_result.json()
print (json_response)
