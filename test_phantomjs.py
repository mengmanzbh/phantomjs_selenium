from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.PhantomJS("/usr/local//bin/phantomjs",
                              service_args=["--ignore-ssl-errors=true", "--ssl-protocol=any"])

# obtain wait object
wait = ui.WebDriverWait(driver, 30)

# navigate
driver.get("https://qa-interview-test.herokuapp.com/app/mapping")
# take screenshot
driver.save_screenshot("screenshot0.png")
# wait for element
wait.until(lambda driver: driver.find_element_by_name("Log In"))
# take screenshot
driver.save_screenshot("screenshot1.png")



# get elements
el_email = driver.find_element_by_name("email")
el_password = driver.find_element_by_name("password")
#enter wrong email
el_email.send_keys("qa-test2@example.com")
el_password.send_keys("5MyHUfNnPBr9xQ")
#press the button
el_password.submit()
wait.until(lambda driver: driver.title.lower().startswith("Wrong Email or password"))

driver.save_screenshot("screenshot2.png")



# get elements
el_email = driver.find_element_by_name("email")
el_password = driver.find_element_by_name("password")
#enter correct text
el_email.send_keys("qa-test@example.com")
el_password.send_keys("5MyHUfNnPBr9xQ")
#press the button
el_password.submit()
wait.until(lambda driver: driver.title.lower().startswith("Sites"))

driver.save_screenshot("screenshot3.png")

#get elements
el_site_settings = driver.find_element_by_xpath("//*[@id="root"]/div/div/div[1]/div/nav[2]/ul/li/a")
#mouseover
hover = ActionChains().move_to_element(el_site_settings)
hover.perform()


#get element
el_units = driver.find_element_by_name(Units).click()
wait.until(lambda driver: driver.title.lower().startswith("Unit Selection"))

#get element
el_value = driver.find_element_by_xpath("//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/span[3]/span").click()
# select by text
el_value.select_by_visible_text("y")

#get element
el_close_button = driver.find_element_by_xpath ("//*[@id="root"]/div/div/div[3]/div/div[1]/i").click()
wait.until(lambda driver: driver.title.lower().startswith("Sites"))

driver.quit()