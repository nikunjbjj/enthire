import requests
import json
import os
import time
from selenium import webdriver


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
log_file = 'data/resume.log'

for i in range(1000):
    try:
        filename = 'data/resume_list/resume_list_page_%s' % i
        data = json.load(open(filename, 'r'))
        for idx, res in enumerate(data['ResultList']):
            s = time.time()
            res_id = res.get('ID', 'someid')
            res_link = res.get('FilePathURI_HTML', 'somepath')
            browser.get('https://recruiter.mightyrecruiter.com/resumes/ResumePreview?path=%s&documentid=%s&search_string=%s'
                        % (res_link, res_id, 'software'))
            html_text = browser.page_source

            with open('data/resumes/resume_list_page_%s_%s' % (i, idx), 'w') as g:
                json.dump(html_text, g)
            time.sleep(2)
            e = time.time()
            with open(log_file, 'a') as f:
                f.write("Successfully downloaded resume: %s, %s. Time taken: %s  \n" % (i, idx, e-s))
            print("Successfully downloaded resume: %s, %s. Time taken: %s  \n" % (i, idx, e-s))
    except Exception as e:
        with open(log_file, 'a') as f:
            f.write("Error happened in page number: %s. Error is: %s \n" % (i, e))
        print("Error happened in page number: %s. Error is: %s \n" % (i, e))
        browser.close()
        time.sleep(60)
        browser = webdriver.Chrome(executable_path=DRIVER_BIN)

        browser.get('https://recruiter.mightyrecruiter.com/login')
        username = browser.find_element_by_id("UserName")
        password = browser.find_element_by_id("Password")

        username.send_keys("Sreetasai@gmail.com")
        password.send_keys("Wrevie123")

        browser.find_element_by_xpath("//*[@id='frmlogin']/div[1]/div[4]/div/button").click()



