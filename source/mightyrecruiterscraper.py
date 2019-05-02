# from http.cookiejar import LWPCookieJar
#
# import mechanize
# import cookiejar
# from bs4 import BeautifulSoup
# import html2text
# import requests
# from lxml import html
#
#
#
# # # Browser
# # br = mechanize.Browser()
# #
# # # Cookie Jar
# # cj = LWPCookieJar()
# # br.set_cookiejar(cj)
# #
# # # Browser options
# # br.set_handle_equiv(True)
# # br.set_handle_gzip(True)
# # br.set_handle_redirect(True)
# # br.set_handle_referer(True)
# # br.set_handle_robots(False)
# # br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# #
# # br.addheaders = [('User-agent', 'Chrome')]
# #
# # # The site we will navigate into, handling it's session
# # br.open('https://recruiter.mightyrecruiter.com/accounts')
# #
# # # View available forms
# # for idx, f in enumerate(br.forms()):
# #
# #     print(idx, f)
# #
# # # Select the second (index one) form (the first form is a search query box)
# # br.select_form(nr=1)
# #
# # # User credentials
# # br.form['UserName'] = 'sreetasai@gmail.com'
# # br.form['Password'] = 'Wrevie123'
# #
# # # Login
# # br.submit()
# #
# # print(br.open('https://www.mightyrecruiter.com/resumes').read())
#
#
# session_requests = requests.session()
# login_url = "https://recruiter.mightyrecruiter.com/accounts"
# result = session_requests.get(login_url, headers={'User-Agent': 'Mozilla/5.0'})
# tree = html.fromstring(result.text)
# payload = {'UserName': 'sreetasai@gmail.com', 'Password': 'Wrevie123'}
# response = session_requests.post(
#     login_url,
#     data=payload,
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# #print(response.raw, response.text)
# # url = 'http://recruiter.mightyrecruiter.com/resumes/Get?jobID=0&page_number=1&page_size=20&search_on=jt&search_string=software&location=&sortBy=score&radius=30&min_experience=0&max_experience=1200&mned=NA&min_age=1&max_age=5000&hide_viewed_resume=false&hide_reviewed_resume=false&documentId=0&similarResumeSearch=false'
# # result = session_requests.get(
# #     url,
# #     headers={'User-Agent': 'Mozilla/5.0'}
# # )
# # import pdb; pdb.set_trace()
# # print(result, result.content)
# #
# # tree = html.fromstring(result.content)
# # import pdb; pdb.set_trace()
# # print(dir(tree))
# # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")
# #
# # print(bucket_names)
#
# import urllib.request, json
# # import requests
# # import json
# # # with urllib.request.urlopen(url, data={'User-Agent': 'Mozilla/5.0'}) as url:
# # #     data = json.loads(url.read().decode())
# # #     print(data)
# #
# # res = requests.post(url,
# #                  headers={'User-Agent': 'Mozilla/5.0', 'application/json'}
# #                  )
# # import pdb; pdb.set_trace()
# # # dataform = str(r).strip("'<>() ").replace('\'', '\"')
# # struct = json.loads(dataform)
# # print(struct)
#
# # res = urllib.request.urlopen('urllib')
# # res_body = res.read()
# #
# # # https://docs.python.org/3/library/json.html
# # j = json.loads(res_body.decode("utf-8"))
# # print(j)

import requests

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://recruiter.mightyrecruiter.com/resumes',
    'authority': 'recruiter.mightyrecruiter.com',
    'cookie': 'optimizelyEndUserId=oeu1556776003338r0.03323844251430619; ajs_group_id=null; _mwr_visitortype=true; ajs_anonymous_id=%226df02273-b0d5-4c1d-baa2-18975972077a%22; G_ENABLED_IDPS=google; _ga=GA1.2.1517422009.1556776004; _gid=GA1.2.914979616.1556776004; __insp_wid=473465058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9yZWNydWl0ZXIubWlnaHR5cmVjcnVpdGVyLmNvbS9hY2NvdW50cz9SZXR1cm5Vcmw9JTJGZGFzaGJvYXJk; __insp_targlpt=TG9naW4%3D; __insp_norec_sess=true; vstr=59a4f63f-b352-4c12-8819-105728c5b9b5; vsuid=2de64596-fed5-4fcd-acde-dc3950709d54; ref=13128; vsutms=1f6cd565-ccd4-4301-953f-cf98aa3d2065#59a4f63f-b352-4c12-8819-105728c5b9b5#2de64596-fed5-4fcd-acde-dc3950709d54#1556776004#||||; pnctest=1; JobTap=iunPYEODvNizWRz5lwR1WhbnSPe-UqJnXapPZZeoLBSI-jEmxTUO61aza_slM4MhOp7EaRqOWlo4hHTvi4eVMbp3iPyLUpZwgzWvAGJYAhhj8etbswauIfxYKQqixwMNAot0BesfYn9jIAYPwPeBFHAM1WZe55F9ERbwIDVbJnV7LqL3xVpT-aTWYmQg6pQ6BDWskr5S8VlDzwnM7z5pYHfLOp_XNmeJzn7uOr4tuX6KvtsTbfRQiL2OKmDRKOq58BWK1nH8Rnwt6ne6TQ4F4MMlat-V4tyXnn-5hn0Bl0VGPIGVoyv9aWC_uoNirgqI8z_-F-3MWDBdA7-Es7xNQF1YcMHD1nVf6nfshBgbpopwcQp4CbjYf7bw25aHUxpmmynosOqpkDq5kgtWIip7QQbN5TXLpmuS_r1-0P84X5LJQxccoxMtSMgBM0Z-yX2dC44eEPJywoLkJLPs077K6Sl2tk7-Hv0gLqix1SVPO_XAa5mfCukVDX2nUxhPSz4gK7ZxnCkdU5wtsJhP2deX20mnIDSjfG60SEq4zkfGoQ3Hmj_YlMftAgu6LxyJLkLmsRYqcfbJ9mOpjKQ2Y-AjeEyt05JASxJlb7UR50x6Gdl5TABepFL6vdyAV_jwPIh0; ajs_user_id=%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22; _mwr_trk=%7B%22requiresignin%22%3A%22False%22%2C%22userid%22%3A%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22email%22%3A%22sreetasai%40gmail.com%22%2C%22firstname%22%3A%22Sreeta%22%2C%22lastname%22%3A%22Gorripaty%22%2C%22cname%22%3A%22Wrevie%22%7D; __ssid=30ab9b5122ad16a2ccb743d02eab455; mp_0568fc1726576866d45cfa17ad4837b9_mixpanel=%7B%22distinct_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24device_id%22%3A%20%2216a7714a9122d7-06586eb482efa3-366e7e04-13c680-16a7714a9133b6%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22mp_name_tag%22%3A%20%22sreetasai%40gmail.com%22%2C%22userId%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22Platform%22%3A%20%22Web%22%2C%22Product%22%3A%20%22Mightyworks%20Recruiter%22%2C%22Login%20Status%22%3A%20%22TRUE%22%2C%22id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24email%22%3A%20%22sreetasai%40gmail.com%22%7D; __insp_slim=1556776949800',
}

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

response = requests.get('https://recruiter.mightyrecruiter.com/resumes/Get', headers=headers, params=params)
print(response.json()['ResultList'][0])
# import pdb; pdb.set_trace()


import requests

resume_headers = {
    'authority': 'recruiter.mightyrecruiter.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://recruiter.mightyrecruiter.com/resumes',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'optimizelyEndUserId=oeu1556776003338r0.03323844251430619; ajs_group_id=null; _mwr_visitortype=true; ajs_anonymous_id=%226df02273-b0d5-4c1d-baa2-18975972077a%22; G_ENABLED_IDPS=google; _ga=GA1.2.1517422009.1556776004; _gid=GA1.2.914979616.1556776004; __insp_wid=473465058; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9yZWNydWl0ZXIubWlnaHR5cmVjcnVpdGVyLmNvbS9hY2NvdW50cz9SZXR1cm5Vcmw9JTJGZGFzaGJvYXJk; __insp_targlpt=TG9naW4%3D; __insp_norec_sess=true; vstr=59a4f63f-b352-4c12-8819-105728c5b9b5; vsuid=2de64596-fed5-4fcd-acde-dc3950709d54; ref=13128; vsutms=1f6cd565-ccd4-4301-953f-cf98aa3d2065#59a4f63f-b352-4c12-8819-105728c5b9b5#2de64596-fed5-4fcd-acde-dc3950709d54#1556776004#||||; pnctest=1; JobTap=iunPYEODvNizWRz5lwR1WhbnSPe-UqJnXapPZZeoLBSI-jEmxTUO61aza_slM4MhOp7EaRqOWlo4hHTvi4eVMbp3iPyLUpZwgzWvAGJYAhhj8etbswauIfxYKQqixwMNAot0BesfYn9jIAYPwPeBFHAM1WZe55F9ERbwIDVbJnV7LqL3xVpT-aTWYmQg6pQ6BDWskr5S8VlDzwnM7z5pYHfLOp_XNmeJzn7uOr4tuX6KvtsTbfRQiL2OKmDRKOq58BWK1nH8Rnwt6ne6TQ4F4MMlat-V4tyXnn-5hn0Bl0VGPIGVoyv9aWC_uoNirgqI8z_-F-3MWDBdA7-Es7xNQF1YcMHD1nVf6nfshBgbpopwcQp4CbjYf7bw25aHUxpmmynosOqpkDq5kgtWIip7QQbN5TXLpmuS_r1-0P84X5LJQxccoxMtSMgBM0Z-yX2dC44eEPJywoLkJLPs077K6Sl2tk7-Hv0gLqix1SVPO_XAa5mfCukVDX2nUxhPSz4gK7ZxnCkdU5wtsJhP2deX20mnIDSjfG60SEq4zkfGoQ3Hmj_YlMftAgu6LxyJLkLmsRYqcfbJ9mOpjKQ2Y-AjeEyt05JASxJlb7UR50x6Gdl5TABepFL6vdyAV_jwPIh0; ajs_user_id=%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22; _mwr_trk=%7B%22requiresignin%22%3A%22False%22%2C%22userid%22%3A%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22email%22%3A%22sreetasai%40gmail.com%22%2C%22firstname%22%3A%22Sreeta%22%2C%22lastname%22%3A%22Gorripaty%22%2C%22cname%22%3A%22Wrevie%22%7D; __ssid=30ab9b5122ad16a2ccb743d02eab455; mp_0568fc1726576866d45cfa17ad4837b9_mixpanel=%7B%22distinct_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24device_id%22%3A%20%2216a7714a9122d7-06586eb482efa3-366e7e04-13c680-16a7714a9133b6%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22mp_name_tag%22%3A%20%22sreetasai%40gmail.com%22%2C%22userId%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22Platform%22%3A%20%22Web%22%2C%22Product%22%3A%20%22Mightyworks%20Recruiter%22%2C%22Login%20Status%22%3A%20%22TRUE%22%2C%22id%22%3A%20%221637792f-9c61-4e53-b5ea-49ebc8a55b71%22%2C%22%24email%22%3A%20%22sreetasai%40gmail.com%22%7D; _gat=1; __insp_slim=1556778475139',
}

resume_params = (
    ('path', 'zDtiQ/mH5rW5+iQMGfXDS8TFt8+cbnZLHrMgG/eRia49Rkh8pHW501ZLksrASY8sIoczEO1jBCFWJV7VYs3RcwyVcp76BL1E+En1OpSjSbVxkdIi2l8ptvOQ6Ji8UGi6dUBq3XnI7eYJA5L5E9qVicY388iDA9Ou1l0C3qSui02+nMQxpVk/O0bcOi6tObKN3725E2V/4ao3wOv1i50gxIOE0OhgjdRtz0O6ZDLV5t+aXwKegO74WMxFrHFYKB0DHPC+kZ0eqbhn0gTGceLAXL9Mwgw16bglPxi7rbmzLuEMgWKefBfqPOYUY78d3Rqr/nPX8hSgYJW+L0jXXMO56cnWxNAstJphw3ov1P1DfNNKqXvAtW+ECLJTCOrqDArjvJrSqXrK1EFGIOL1h9WpiI4hUZZhe2ym7TFWK1UgHRye/DCF01FAPSmHaXYOfsRGZZWyMPmV39PmWWBtV4oavR4YN/+tr1RvqPRf2xrrdgx8nx4IHB4d5T7B/jz26bMkWUZDmp71/HtDPZojTnRQAw=='),
    ('documentid', '92424785'),
    ('search_string', 'software'),
)

resume_response = requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview', headers=resume_headers, params=resume_params)
# resume_response = requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview?path=zDtiQ%2FmH5rW5%2BiQMGfXDS8TFt8%2BcbnZLHrMgG%2FeRia49Rkh8pHW501ZLksrASY8sIoczEO1jBCFWJV7VYs3RcwyVcp76BL1E%2BEn1OpSjSbVxkdIi2l8ptvOQ6Ji8UGi6dUBq3XnI7eYJA5L5E9qVicY388iDA9Ou1l0C3qSui02%2BnMQxpVk%2FO0bcOi6tObKN3725E2V%2F4ao3wOv1i50gxIOE0OhgjdRtz0O6ZDLV5t%2BaXwKegO74WMxFrHFYKB0DHPC%2BkZ0eqbhn0gTGceLAXL9Mwgw16bglPxi7rbmzLuEMgWKefBfqPOYUY78d3Rqr%2FnPX8hSgYJW%2BL0jXXMO56cnWxNAstJphw3ov1P1DfNNKqXvAtW%2BECLJTCOrqDArjvJrSqXrK1EFGIOL1h9WpiI4hUZZhe2ym7TFWK1UgHRye%2FDCF01FAPSmHaXYOfsRGZZWyMPmV39PmWWBtV4oavR4YN%2F%2Btr1RvqPRf2xrrdgx8nx4IHB4d5T7B%2Fjz26bMkWUZDmp71%2FHtDPZojTnRQAw%3D%3D&documentid=92424785&search_string=software',
#                                headers=resume_headers)
# print(resume_response.json())

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(resume_response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview?path=zDtiQ%2FmH5rW5%2BiQMGfXDS8TFt8%2BcbnZLHrMgG%2FeRia49Rkh8pHW501ZLksrASY8sIoczEO1jBCFWJV7VYs3RcwyVcp76BL1E%2BEn1OpSjSbVxkdIi2l8ptvOQ6Ji8UGi6dUBq3XnI7eYJA5L5E9qVicY388iDA9Ou1l0C3qSui02%2BnMQxpVk%2FO0bcOi6tObKN3725E2V%2F4ao3wOv1i50gxIOE0OhgjdRtz0O6ZDLV5t%2BaXwKegO74WMxFrHFYKB0DHPC%2BkZ0eqbhn0gTGceLAXL9Mwgw16bglPxi7rbmzLuEMgWKefBfqPOYUY78d3Rqr%2FnPX8hSgYJW%2BL0jXXMO56cnWxNAstJphw3ov1P1DfNNKqXvAtW%2BECLJTCOrqDArjvJrSqXrK1EFGIOL1h9WpiI4hUZZhe2ym7TFWK1UgHRye%2FDCF01FAPSmHaXYOfsRGZZWyMPmV39PmWWBtV4oavR4YN%2F%2Btr1RvqPRf2xrrdgx8nx4IHB4d5T7B%2Fjz26bMkWUZDmp71%2FHtDPZojTnRQAw%3D%3D&documentid=92424785&search_string=software', headers=headers)
