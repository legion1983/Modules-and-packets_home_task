from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from pprint import pprint
import requests
from time import sleep

EXE_PATH = r'C:\Users\p.rudyakov\Desktop\Chrome_driver_103'
driver = webdriver.Chrome(executable_path=EXE_PATH)
# driver.get('https://fsa.gov.ru/use-of-technology/servis-registratsii-deklaratsiy-o-sootvetstvii/')
browser = webdriver.Chrome()
driver.get('https://youtube.com')

block = driver.find_element(By.CLASS_NAME, "style-scope ytd-watch-flexy")
print(block)

# block = driver.find_element_by_class_name("card-service__icon-wrap")
# print(block)


# activate_DOC_self_registration = driver.find_element(By.CLASS_NAME, "card-service__title")
# activate_DOC_self_registration = driver.find_element(By.CLASS_NAME, "card-service__title")
# activate_DOC_self_registration.click(clickable)
# clickable = driver.find_element_by_class_name("card-service__icon-wrap").click()


# # element = driver.find_element_by_class_name('card-service__title')
# # selenium.webdriver.common.actions.mouse_button.MouseButton(0)
# clickable = driver.find_element('card-service__title', "click")
# ActionChains(driver)\
#     .click(clickable)\
#     .perform()

# /html/body/main/main/section[4]/div/div/div/div/div[2]/div/div[4]/div/a/div[2]/div[1]



# def test_click_and_release(driver):
#     driver= driver.get('https://fsa.gov.ru/use-of-technology/servis-registratsii-deklaratsiy-o-sootvetstvii/')
#     clickable = driver.find_element(By.CLASS_NAME, "card-service__icon-wrap")
#     ActionChains(driver) \
#         .click(clickable) \
#         .perform()
#     assert "resultPage.html" in driver.current_url
#
#
# test_click_and_release(driver)