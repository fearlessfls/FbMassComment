from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from getpass import getpass
usname = input("Enter Your Username :::: > ")
psword = getpass()
postid = input('Enter Post Path :::: >')
comt = input('Enter Your Comment :::: >')
num = input('Number of commnets :::: >')
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://mbasic.facebook.com')
uname = driver.find_element_by_id('m_login_email')
uname.send_keys(usname)
pw = driver.find_element_by_name('pass')
pw.send_keys(psword)
driver.find_element_by_name('login').click()
print('Logging In .....')
time.sleep(3)
driver.get('https://mbasic.facebook.com/'+ postid)
for i in range(0,int(num)):
    cmt = driver.find_element_by_id('composerInput')
    cmt.send_keys(comt)
    driver.find_element_by_xpath("//input[@value='Comment']").click()
    i = i+1
    print(str(i) + 'Done')
input('Press Enter To Exit')
driver.close()
