from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/ref=ap_frn_logo")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_ya_signin']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000676)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Loki@1234")
driver.find_element(By.ID, "auth-signin-button").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='nav-search-field ']/input["
                                                                      "@aria-label='Search Amazon.in']")))
driver.find_element(By.XPATH, "//div[@class='nav-search-field ']/input[@aria-label='Search Amazon.in']").send_keys("apple iphone 14 pro max 256 gb gold")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# a = "Apple iPhone 14 Pro Max (256 GB) - Gold"
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[.='Apple iPhone 14 Pro Max (256 GB) - Gold']")))
print(driver.find_element(By.XPATH, "//a[.='Apple iPhone 14 Pro Max (256 GB) - Gold']").text)

