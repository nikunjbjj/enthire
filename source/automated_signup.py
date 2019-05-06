from selenium import webdriver
import os

DRIVER_BIN = os.path.join("", "/Users/cusgadmin/Downloads/chromedriver")

browser = webdriver.Chrome(executable_path=DRIVER_BIN)
browser.get('https://recruiter.mightyrecruiter.com/login')

#### Page 1
job_description = "Outline the core responsibilities of the position. Make sure your list of responsibilities is detailed but concise. Also emphasize the duties that may be unique to your organization. For example, if you are hiring for an “Event Management” role and the position requires social media expertise to promote events, include this detail to ensure candidates understand the requirements and can determine if they’re qualified."
company_description = "Individualize. Engage. Transform. Understand and Influence the Intent of Each Customer in Real-time Learn how Wrevie can help you: Grow revenue and increase customer loyalty Actively listen to interests and purchase intent of each customer Engage your online shoppers through AI-powered personalization"

company_name = browser.find_element_by_id("Company.Name")
job_title = browser.find_element_by_id("Title")
location = browser.find_element_by_id("autocomplete")
job_description_elem = browser.find_element_by_id("Description")
company_description_elem = browser.find_element_by_id("Company.Overview")

company_name.send_keys("Wrevie")
job_title.send_keys("Software Engineer")
location.send_keys("Menlo Park, NJ, USA")
browser.find_element_by_xpath("//*[@id='locality']").setAttribute("value", "Edison")
job_description_elem.send_keys(job_description)
company_description_elem.send_keys(company_description)

browser.find_element_by_xpath("//*[@id='savepost']").click()

### Page 2
browser.find_element_by_xpath("//*[@id='btnContinue']/span").click()


#### Page 3

email_address = browser.find_element_by_id("User.EmailAddress")
first_name = browser.find_element_by_id("User.FirstName")
last_name = browser.find_element_by_id("User.LastName")
phone = browser.find_element_by_id("User.Phone")

email_address.send_keys("trial1@gmail.com")
first_name.send_keys("Trial")
last_name.send_keys("Kumar")
phone.send_keys("(453) 567-7654")

# Number of employees
browser.find_element_by_xpath("//*[@id='frmSignUp]/div/div[8]/div/div/ul/li[7]").click()
# Company type
browser.find_element_by_xpath("//*[@id='frmSignUp']/div/div[9]/div/div/ul/li[2]").click()
# Continue
browser.find_element_by_xpath("//*[@id='btnContinue']").click()

