import requests

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


#### Get List of resumes ####
url = "https://recruiter.mightyrecruiter.com/resumes/Get"
log_file = 'data/resume_list.log'

for page_number in range(1, 2):
    try:
        # s = time.time()
        params = (
            ('jobID', '0'),
            ('page_number', '%s' % page_number),
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
        json_response = resumes_list_result.json()
        for idx, res in enumerate(json_response['ResultList']):
            try:
                res_id = res.get('ID', 'someid')
                res_link = res.get('FilePathURI_HTML', 'somepath')
                print(page_number, idx, res_id)
                resume_params = (
                    ('path', res_link),
                    ('documentid', res_id),
                    ('search_string', 'software')
                )
                resume_response = session_requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview',
                                                       headers=headers,
                                                       params=resume_params)
                with open('data/resume_%s_%s.html' % (idx, res_id), 'w') as f:
                    f.write(resume_response.text)
            except Exception as e:
                print(page_number, idx, e)
    except Exception as e:
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

# #
# # from html.parser import HTMLParser
# #
# # class MyHTMLParser(HTMLParser):
# #     def handle_starttag(self, tag, attrs):
# #         print("Encountered a start tag:", tag)
# #
# #     def handle_endtag(self, tag):
# #         print("Encountered an end tag :", tag)
# #
# #     def handle_data(self, data):
# #         print("Encountered some data  :", data)
# #
# # parser = MyHTMLParser()
# # parser.feed(resume_response.text)
#
