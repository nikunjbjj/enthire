import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import string
import time

login_url = "https://www.linkedin.com/"

error_file = 'errorfile'
res_id = 'someid'
res_link = 'somepath'

DRIVER_BIN = os.path.join("", "/Users/cusgadmin/work/enthire/source/chromedriver")
browser = webdriver.Chrome(executable_path=DRIVER_BIN)

browser.get(login_url)
browser.find_element_by_xpath("/html/body/nav/a[3]").click()

username = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

username.send_keys("nikunjbjj@gmail.com")
password.send_keys("Enthire1")

browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').click()


all_chars = [i for i in string.ascii_lowercase[15:17]]
try:
    with open('linkedin_error_file', 'a') as ef:
        with open('linkedin_log_file', 'a') as lf:
            for character in all_chars:
                try:
                    main_url = "https://www.linkedin.com/directory/people-%s-1" % character
                    browser.get(main_url)
                    soup_level1 = BeautifulSoup(browser.page_source, 'lxml')
                    num_pages = len(soup_level1.find_all('a', {'href': re.compile(r'people-%s' % character)})) - 2
                    lf.write("Character: %s\n" % character)
                    lf.write("Number of page: %s\n" % num_pages)
                    for idx in range(1, num_pages+1):
                        try:
                            main_url = "https://www.linkedin.com/directory/people-%s-%s" % (character, idx)
                            browser.get(main_url)
                            soup_level1 = BeautifulSoup(browser.page_source, 'lxml')
                            data = soup_level1.find_all('a', {'href': re.compile(r'people_directory')})
                            lf.write("Idx: %s\n" % idx)
                            lf.write("Length of data: %s\n" % len(data))
                            with open('linkedin_data/%s_%s' % (character, idx), 'w') as df:
                                for i, d in enumerate(data[:-1]):
                                    try:
                                        href = d.get('href')
                                        text = d.get_text()
                                        df.write('%s, %s \n' % (href, text))
                                    except Exception as e:
                                        ef.write("Error 3rd loop, idx = %s, Error = %s \n" % (i, e))
                            time.sleep(1)
                        except Exception as e:
                            ef.write("Error 2nd loop, idx = %s, Error = %s \n" % (idx, e))
                except Exception as e:
                    ef.write("Error 1st loop, character = %s, Error = %s \n" % (character, e))
except Exception as e:
    ef.write("Error 0th loop, Error = %s \n" % e)


# all_chars = [i for i in string.ascii_lowercase[2:26]]
# try:
#     with open('linkedin_error_file', 'a') as ef:
#         with open('linkedin_log_file', 'a') as lf:
#             for character in all_chars:
#                 try:
#                     main_url = "https://www.linkedin.com/directory/people-%s-1" % character
#                     browser.get(main_url)
#                     soup_level1 = BeautifulSoup(browser.page_source, 'lxml')
#                     num_pages = len(soup_level1.find_all('a', {'href': re.compile(r'people-%s' % character)})) - 2
#                     lf.write("Character: %s\n" % character)
#                     lf.write("Number of page: %s\n" % num_pages)
#                     for idx in range(1, num_pages+1):
#                         try:
#                             main_url = "https://www.linkedin.com/directory/people-%s-%s" % (character, idx)
#                             browser.get(main_url)
#                             soup_level1 = BeautifulSoup(browser.page_source, 'lxml')
#                             data = soup_level1.find_all('a', {'href': re.compile(r'people_directory')})
#                             lf.write("Idx: %s\n" % idx)
#                             lf.write("Length of data: %s\n" % len(data))
#                             with open('linkedin_data/%s_%s' % (character, idx), 'w') as df:
#                                 for i, d in enumerate(data[:-1]):
#                                     try:
#                                         href = d.get('href')
#                                         text = d.get_text()
#                                         df.write('%s, %s \n' % (href, text))
#                                     except Exception as e:
#                                         ef.write("Error 3rd loop, idx = %s, Error = %s \n" % (i, e))
#                             time.sleep(1)
#                         except Exception as e:
#                             ef.write("Error 2nd loop, idx = %s, Error = %s \n" % (idx, e))
#                 except Exception as e:
#                     ef.write("Error 1st loop, character = %s, Error = %s \n" % (character, e))
# except Exception as e:
#     ef.write("Error 0th loop, Error = %s \n" % e)
#
