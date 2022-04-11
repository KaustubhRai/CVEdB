from selenium import webdriver
from exploit_price import vulrul
from selenium.webdriver.common.by import By

"""
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
url_a = "https://chandanbn.github.io/cvss/#CVSS:3.1/"

vulurl_results = vulrul("CVE-2010-3333")
url_b = vulurl_results[2]
url = url_a + url_b
# "https://chandanbn.github.io/cvss/#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
driver.get(url)

elem = driver.find_element_by_class_name("cvssjs") 
elem.screenshot('Screenshots/Element.png') 
driver.quit()

# screenshot = driver.save_screenshot('my_screenshot.png')
# driver.quit()
"""

def cvss_screenshot(cve_id):
	DRIVER = 'chromedriver'
	driver = webdriver.Chrome(DRIVER)
	url_a = "https://chandanbn.github.io/cvss/#CVSS:3.1/"
	vulurl_results = vulrul(cve_id)
	url_b = vulurl_results[2]
	url = url_a + url_b
	driver.get(url)
	# elem = driver.find_element_by_class_name("cvssjs")
	elem = driver.find_element(By.CLASS_NAME, "cvssjs")
	# screenshot_name = "Screenshots/"+ cve_id + "_cvss" + ".png"
	screenshot_name = cve_id + "_cvss" + ".png"
	screenshot_folder = "static/Screenshots/" + screenshot_name
	elem.screenshot(screenshot_folder)
	driver.quit()
	return screenshot_name

# cvss_screenshot("CVE-2010-3333")