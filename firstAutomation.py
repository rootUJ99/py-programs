from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
time.sleep(3) # Let the user actually see something!
username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys('rootuj')
password = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys('wanted99UJWALARAK')
login = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
time.sleep(3)
sayno = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
explore = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(5)
first_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
time.sleep(2)
first_element_modal = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').click()
time.sleep(3)
profile = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').click()
time.sleep(5)
first_post = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
time.sleep(2)
likeit = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
# print('login', )
# driver.quit()
