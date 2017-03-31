from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.PhantomJS('/usr/local/bin/phantomjs',
                              service_args=['--ignore-ssl-errors=yes', '--ignore-ssl-errors=true', '--ssl-protocol=any', '--debug=true'])

# obtain wait object
wait = ui.WebDriverWait(driver, 10)

# navigate
driver.get('https://app.burstorm.com/projects')

# take screenshot
driver.save_screenshot('screenshot0.png')

# wait for element
wait.until(lambda driver: driver.find_element_by_id('email'))

# take screenshot
driver.save_screenshot('screenshot1.png')

# get elements
el_email = driver.find_element_by_id('email')
#enter text
el_email.send_keys('evoskoley@rocketmail.com')
#press the button
el_email.submit()

# get elements
el_password = driver.find_element_by_id('user_password')
#enter text
el_password.send_keys('Password')
#press the button
el_password.submit()

# wait for title, if any
#wait.until(lambda driver: driver.title.lower().startswith('welcome!'))

driver.save_screenshot('screenshot2.png')
driver.quit()