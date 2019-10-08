import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.postjobfree.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ASP.NET_SessionId=4yig4edo31iladznps4yqzl0; tsource=a60327659; _ga=GA1.2.1611376518.1557700105; _gid=GA1.2.232431499.1557700105; _gat=1; ldl=',
}

params = (
    ('q', 'software'),
    ('l', ''),
    ('radius', '2500'),
    ('p', '1'),
)

response = requests.get('https://www.postjobfree.com/resumes', headers=headers, params=params)

candidate_list = BeautifulSoup(response.text)
for candidate in candidate_list.find_all("h3", {"class": "itemTitle"}):
    resume_link = candidate.find_all("a")[0]['href']
    resume_response = requests.get('https://www.postjobfree.com/resume/%s' % resume_link)
    print(resume_link)


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.postjobfree.com/resumes?q=software+engineer&l=&radius=2500&p=1', headers=headers)
