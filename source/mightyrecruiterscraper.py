import requests
import json

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
print("Resumes status code: " + str(resumes_list_result.status_code))

json_response = resumes_list_result.json()
print(json_response)


error_file = 'errorfile'
res_id = 'someid'
res_link = 'somepath'
### Loop over the resumes data and fetch the resume HTML ####
for idx, res in enumerate(json_response['ResultList'][:3]):
    try:
        res_id = res.get('ID', 'someid')
        print("ID: ", res_id)
        res_link = res.get('FilePathURI_HTML', 'somepath')
        resume_params = (
            ('path', res_link),
            ('documentid', res_id),
            ('search_string', 'software'),
        )
        # headers.update({'cookie': 'optimizelyEndUserId=oeu1556771288707r0.9429390521310967; ajs_group_id=null; vstr=7c265542-f036-45a1-873c-9f51968fc7bd; ref=13127; visitinfo=cuofn2UmFz8HqM1qiI+BZcR5/i9CANW9AAHoCMZrIMgxltIrMwZCIVwfJVdw2wMHmV2wOKMqpVJRvnBjGSFSsl5pP/t6R8jDPjq+2CIuBK0SMcl5jbWeQ8IeLLoQNFvqAMmtN7kicJXoODUULQ02Xz7pV9UAdD3g; vsuid=358fae98-214f-47e4-84c3-26954a9d418f; _ga=GA1.2.1765843271.1556771290; _gid=GA1.2.980701982.1556771290; __unam=86b865-16a76ccb5db-57709dee-2; vsutms=1788d846-804c-43c9-b90b-3ed7aee4d747#7c265542-f036-45a1-873c-9f51968fc7bd#a1cee15f-d9e2-40dd-a207-3881f0b27c51#1556771993#google|sem|brand_-_us_-_search|mightyrecruiter|; _gac_UA-3289623-12=1.1556771994.CLii-uK449MCFcdffgodE_oLqg; utmParams=%7C%7C%7C%7C; pnctest=1; G_ENABLED_IDPS=google; _mwr_trk_m={"requiresidentify":"false","requiresignup":"true","userid":"b0a41b67-a4cb-4c80-8330-068425a72ea2","email":"nikunjbjj@gmail.com","firstname":"Nikunj","lastname":"Bajaj","cname":"Wrevie","ctype":"Employer","cwebsite":"wrevie.com","mediapermission":"TRUE","contactbyphonepermission":"TRUE","accountstatus":"Pending","planstatus":null,"noofjobs":null}; _mwr_visitortype=true; IR_gbd=mightyrecruiter.com; IR_5168=1556772248047%7C0%7C1556772248047; __ssid=e3db82b8fe87acf0dfbb35705bb851b; IR_PI=1806628e-9e78-3699-c3e1-cb68a9b2d1c6%7C1556858648047; G_AUTHUSER_H=0; JobTap=l7WYlhcYgOfrOYB3VqVz1F2IE9NFeAdAiCkH93MqtBOvzlZKZ54Wp37baNrVyT_56zQ3s5aGNnZzs18-HTJZNCQIFzqn3bFo-OFz2hAc_9Wq0fQSEGJ4P6BsCbuZtsuIRKBNg4NM33Z2huiBbE3YHuZ-47Xn8-1kTSWmzmOmNB4C1ofQaW8U_CFMRiiXARJaEv_irCZHjZQorkigi2JkcgN0iiAqlG7A0HpFFbgtUWuMGKZGXu3wFhhlfc9umcSrlMdbAUoS5C0-x1Xi8v0Wf3E4-vsx8DNVt_n2rkI5wTWq4Ue3PIZBZoiCpyJzRuqr89CbBv5bAj5sBu7I8WfuQMb8lb1qD77bNp097bXAlhf8uh0400cEilSw2UyX-rzYqH03EnEHrDCqtASg6S6mO54yHtdCPmf0Ol19O52thzLczMkH0NjHyYaG0yrLaYeWOZhpIPKPN8Joe9szQ1SrEExDslmEt4xqEHcsU_J8owZdVvqOWa8yY8Eo7lAEwIKvFcIRjakBrIwH_Jz1sb0aYckljipQla-_WH95E2ZEfEKuUzrtlbFNa9VAeEVISz3mM_-3wb5TJlORpS515fiGZeeCQbXFe_Sm0WdnMnUzeEJOH2aQCNF9KIUjrXZnDU7f; _mwr_trk=%7B%22requiresignin%22%3A%22False%22%2C%22userid%22%3A%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22email%22%3A%22sreetasai%40gmail.com%22%2C%22firstname%22%3A%22Sreeta%22%2C%22lastname%22%3A%22Gorripaty%22%2C%22cname%22%3A%22Wrevie%22%7D; __insp_wid=473465058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9yZWNydWl0ZXIubWlnaHR5cmVjcnVpdGVyLmNvbS9yZXN1bWVz; __insp_targlpt=UmVzdW1lIERhdGFiYXNl; __insp_norec_sess=true; _gat=1; __insp_slim=1556855841996; ajs_user_id=%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22; ajs_anonymous_id=%22d1d19e5d-6e69-42a4-bc90-a56a0379036f%22; mp_0568fc1726576866d45cfa17ad4837b9_mixpanel=%7B%22distinct_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24device_id%22%3A%20%2216a76ccb9e01e6-03ab1f48aae2b4-366e7e04-13c680-16a76ccb9e1539%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22utm_source%22%3A%20%22google%22%2C%22utm_medium%22%3A%20%22sem%22%2C%22utm_campaign%22%3A%20%22brand_-_us_-_search%22%2C%22utm_term%22%3A%20%22mightyrecruiter%22%2C%22%24user_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22mp_name_tag%22%3A%20%22sreetasai%40gmail.com%22%2C%22userId%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22Company%20Name%22%3A%20%22Wrevie%22%2C%22Company%20Type%22%3A%20%22Employer%22%2C%22Number%20Of%20Jobs%22%3A%20null%2C%22Company%20Website%22%3A%20%22wrevie.com%22%2C%22Media%20Permission%20For%20Job%20Board%20Performance%22%3A%20%22TRUE%22%2C%22Contact%20By%20Phone%20Permission%22%3A%20%22TRUE%22%2C%22Account%20Status%22%3A%20%22Pending%22%2C%22Plan%20Status%22%3A%20null%2C%22Platform%22%3A%20%22Web%22%2C%22Product%22%3A%20%22Mightyworks%20Recruiter%22%2C%22Login%20Status%22%3A%20%22TRUE%22%2C%22id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24email%22%3A%20%22sreetasai%40gmail.com%22%2C%22%24first_name%22%3A%20%22Nikunj%22%2C%22%24last_name%22%3A%20%22Bajaj%22%2C%22%24name%22%3A%20%22Nikunj%20Bajaj%22%7D'})
        resume_response = requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview',
                                       headers=headers,
                                       params=resume_params)
        with open('data/resume_data_%s_%s' % (idx, res_id), 'w') as f:
            f.write("%s\n" % json.dumps(res))
            f.write(resume_response.text)
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

