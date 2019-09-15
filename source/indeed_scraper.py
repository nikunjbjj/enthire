from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from parsel import Selector
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
f = open("urls.txt", "r")
urls = f.readlines()
urls = [url.replace('\n', '') for url in urls]
f.close()

driver = webdriver.Chrome()
driver.maximize_window()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def hover(elem):
    ActionChains(driver).move_to_element(elem).perform()


def start_end_date(date):
    if date is not None:
        date = date.split(' to ')
        try:
            start = date[0]
            end = date[1]
        except IndexError:
            end = ''
    else:
        start = ''
        end = ''
    return start, end


input("Entered captcha?")
for link_no, url in enumerate(urls, start=1):
    driver.get(url)
    resume_no = 1
    page_no = 0
    while True:
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class,"icl-TextLink--primary rezemp-u-h4")]')))
        except:
            input('Please check browser and press enter')
        resume_cards = driver.find_elements_by_xpath('//div[@class="rezemp-ResumeSearchCard-contents"]')
        for card in resume_cards:
            hover(card)
            sel = Selector(driver.page_source)
            location = sel.xpath('//div[@class="rezemp-ResumeDisplay-body"]/div/div/div[contains(@class,"icl-u-textColor--secondary")]/text()').extract_first()
            personal_summary = sel.xpath('//div[@class="rezemp-ResumeDisplay-body"]/div/div[not (descendant::div[contains(@class,"icl-u-textColor--secondary")]) and not(@class)]/text()').extract()
            work_exp_elems = sel.xpath('//div[@class="rezemp-ResumeDisplay-body"]//div[@class="rezemp-WorkExperience"]')
            work_exp_list = []
            for elem in work_exp_elems:
                title = ''.join(elem.xpath('./div[@class="rezemp-u-h4"]/span/descendant-or-self::*/text()').extract())
                company_name = elem.xpath('./div[@class="rezemp-WorkExperience-subtitle"]/div/span[@class="icl-u-textBold"]/span/text()').extract_first()
                date = elem.xpath('./div[@class="rezemp-WorkExperience-subtitle"]/div[@class="icl-u-textColor--tertiary"]/text()').extract_first()
                start, end = start_end_date(date)
                project_description = ''.join(elem.xpath('./div[not(@class)]/descendant-or-self::*/text()').extract())
                work_exp_list.append({
                    'company_name': company_name,
                    'title': title,
                    'start': start,
                    'end': end,
                    'project_description': project_description,
                })
            education_elems = sel.xpath('//div[@class="rezemp-ResumeDisplaySection" and ./span[contains(text(),"Education")]]/div[@class="rezemp-ResumeDisplaySection-content"]/div[not(@class)]')
            education_list = []
            for elem in education_elems:
                degree_name = ''.join(elem.xpath('./span[@class="rezemp-ResumeDisplay-itemTitle"]/descendant-or-self::*/text()').extract())
                school_name = elem.xpath('./div[@class="rezemp-ResumeDisplay-university"]/div[not(@class)]/span[@class="icl-u-textBold"]/span/text()').extract_first()
                date = elem.xpath('./div[@class="rezemp-ResumeDisplay-university"]/span[@class="rezemp-ResumeDisplay-date"]/text()').extract_first()
                start, end = start_end_date(date)
                location = elem.xpath('./div[@class="rezemp-ResumeDisplay-university"]/div/span[@class="rezemp-ResumeDisplay-universityLocation"]/span/text()').extract_first()
                # description=
                education_list.append({
                    'school_name': school_name,
                    'degree_name': degree_name,
                    'start': start,
                    'end': end,
                    'location': location,
                })
            skills = [''.join(skill.xpath("descendant-or-self::*/text()").extract()) for skill in sel.xpath('//div[@class="rezemp-ResumeDisplaySection" and ./span[contains(text(),"Skills")]]/div[@class="rezemp-ResumeDisplaySection-content"]/span/span')]
            additional_information = ''.join(sel.xpath('//div[@class="rezemp-ResumeDisplaySection" and ./span[contains(text(),"Additional Information")]]/div[@class="rezemp-ResumeDisplaySection-content"]/div[not(@class)]/descendant-or-self::*/text()').extract())
            resume_data = {
                'location': location,
                'personal_summary': personal_summary,
                'work_exprience': work_exp_list,
                'education': education_list,
                'skills': skills,
                'additional_information': additional_information,
            }
            if not os.path.exists(f'resumes_link_no_{link_no}'):
                os.makedirs(f'resumes_link_no_{link_no}')
            with open(f'resumes_link_no_{link_no}/Resume#{resume_no}.json', 'w') as fp:
                json.dump(resume_data, fp, indent=4)
            resume_no += 1
        if check_exists_by_xpath('//span[contains(@class,"pagination-nextbutton")]'):
            # driver.find_element_by_xpath('//span[contains(@class,"pagination-nextbutton")]').click()
            page_no += 50
            driver.get(url + '&start=' + str(page_no))
        else:
            break

print('Scraping completed')
