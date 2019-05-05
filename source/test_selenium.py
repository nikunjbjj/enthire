from selenium import webdriver
import os

DRIVER_BIN = os.path.join("", "/Users/cusgadmin/Downloads/chromedriver")

browser = webdriver.Chrome(executable_path=DRIVER_BIN)
browser.get('https://recruiter.mightyrecruiter.com/login')

username = browser.find_element_by_id("UserName")
password = browser.find_element_by_id("Password")

username.send_keys("Sreetasai@gmail.com")
password.send_keys("Wrevie123")

browser.find_element_by_xpath("//*[@id='frmlogin']/div[1]/div[4]/div/button").click()

browser.get('https://recruiter.mightyrecruiter.com/resumes')

browser.find_element_by_id("txtrsjobtitle").send_keys("software")

browser.find_element_by_id("resumeSearch").click()

browser.implicitly_wait(5)

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[2]/div[3]/a").click()

# html_text = browser.find_element_by_id("ifrmLoadRsm")

browser.switch_to.frame(browser.find_element_by_id("ifrmLoadRsm"))

html_text = browser.page_source

with open('/Users/cusgadmin/Downloads/resume.html', 'w') as f:
    f.write(html_text)




# headers = {
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-US,en;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#     'accept': 'application/json, text/plain, */*',
#     'authority': 'recruiter.mightyrecruiter.com',
#     'referer': 'https://recruiter.mightyrecruiter.com/accounts',
#     'upgrade-insecure-requests': '1',
#     'origin': 'https://recruiter.mightyrecruiter.com',
#     'content-type': 'application/x-www-form-urlencoded'
# }
#
#
#
# for key, value in enumerate(headers):
#     capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
#     webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value