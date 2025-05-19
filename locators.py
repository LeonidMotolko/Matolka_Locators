from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

path = os.path.abspath("example.html")
driver.get("file://" + path)

# task 1: Basic Attributes
driver.find_element(By.XPATH, "//input[@id='username']")
driver.find_element(By.XPATH, "//input[@name='pass']")
driver.find_element(By.XPATH, "//button[@class='login-button']")

driver.find_element(By.CSS_SELECTOR, "#username")
driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
driver.find_element(By.CSS_SELECTOR, ".login-button")

# task 2: Dynamic Elements
driver.find_element(By.XPATH, "//li[@data-id='about']")
driver.find_element(By.XPATH, "//li[a[contains(text(),'Services')]]")

driver.find_element(By.CSS_SELECTOR, "li[data-id='contact']")
driver.find_element(By.CSS_SELECTOR, "li[data-id='home'] a")

# task 3: XPath Axes
driver.find_element(By.XPATH, "//label[@for='email']")
driver.find_element(By.XPATH, "//label[@for='email']/following-sibling::input")
driver.find_element(By.XPATH, "//input[@id='password']/following::button")

# task 4: CSS Pseudo-classes
driver.find_element(By.CSS_SELECTOR, ".items .item:first-child")
driver.find_element(By.CSS_SELECTOR, ".items .item:last-child")
driver.find_element(By.CSS_SELECTOR, ".items .item:nth-child(3)")

# task 5: XPath Wildcards and Functions
driver.find_element(By.XPATH, "//td[text()='Doe']")
driver.find_element(By.XPATH, "//td[starts-with(text(),'jane')]")
emails = driver.find_elements(By.XPATH, "//td[contains(text(),'@')]")

# task 6: Multiple Classes
driver.find_element(By.XPATH, "//div[contains(@class, 'button') and contains(@class, 'primary')]")
driver.find_element(By.CSS_SELECTOR, ".button.secondary")
driver.find_element(By.CSS_SELECTOR, ".primary.large")

# task 7: contains / starts-with
driver.find_element(By.XPATH, "//a[contains(@href,'456')]")
driver.find_element(By.XPATH, "//a[starts-with(@href,'product')]")

driver.find_element(By.CSS_SELECTOR, "a[href*='789']")
driver.find_element(By.CSS_SELECTOR, "a[href^='product']")

# task 8: Dynamic Element Handling
driver.find_element(By.XPATH, "//button[text()='Load More']")
driver.find_element(By.XPATH, "(//div[@class='content-item'])[last()]")
driver.find_element(By.CSS_SELECTOR, "div[data-id^='item']")

time.sleep(60)
driver.quit()
