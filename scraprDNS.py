#script aspect to scrape ViewDNS.info
from selenium import webdriver
from selenium.webdriver.comon.keys import Keys

driver = webdriver.Chrome(executeable_path='')
driver.get('https://viewdns.info')

command_box = driver.find_element_by_id()
command_box.send_keys(input)
command_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

result = driver.find_element_by_id('resultBox')
print(result.text)

driver.quit()
