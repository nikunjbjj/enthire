import requests
import json
import os
from selenium import webdriver


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
    data=payload,
    headers=headers
)

print("Login Status code: " + str(result.status_code))

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
print("Resumes status code: " + str(resumes_list_result.status_code))

json_response = resumes_list_result.json()
print(json_response)


error_file = 'errorfile'
res_id = 'someid'
res_link = 'somepath'
### Loop over the resumes data and fetch the resume HTML ####

DRIVER_BIN = os.path.join("", "/Users/cusgadmin/Downloads/chromedriver")
browser = webdriver.Chrome(executable_path=DRIVER_BIN)

browser.get('https://recruiter.mightyrecruiter.com/login')
username = browser.find_element_by_id("UserName")
password = browser.find_element_by_id("Password")

username.send_keys("Sreetasai@gmail.com")
password.send_keys("Wrevie123")

browser.find_element_by_xpath("//*[@id='frmlogin']/div[1]/div[4]/div/button").click()

for idx, res in enumerate(json_response['ResultList']):
    try:
        res_id = res.get('ID', 'someid')
        res_link = res.get('FilePathURI_HTML', 'somepath')

        print("ID: ", res_id, res_link)

        resume_params = (
            ('path', res_link),
            ('documentid', res_id),
            ('search_string', 'software'),
        )

        browser.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview?path=%s&documentid=%s&search_string=%s'
                    % (res_link, res_id, 'software'))
        html_text = browser.page_source
        # resume_response = session_requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview',
        #                                        headers=headers,
        #                                        params=resume_params)
        with open('data/resume_%s_%s.html' % (idx, res_id), 'w') as f:
            f.write(html_text)
    except Exception as e:
        with open(error_file, 'a') as f:
            f.write("Failed for %s, %s, %s, %s\n" % (idx, res_id, res_link, e))
            # f.write("%s\n" % e)

#
# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)
#
#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)
#
#     def handle_data(self, data):
#         print("Encountered some data  :", data)
#
# parser = MyHTMLParser()
# parser.feed(resume_response.text)

