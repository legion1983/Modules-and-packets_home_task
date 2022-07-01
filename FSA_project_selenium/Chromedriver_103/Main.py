from selenium import webdriver
import time

url = "https://fsa.gov.ru/use-of-technology/servis-registratsii-deklaratsiy-o-sootvetstvii/"
driver = webdriver.Chrome(executable_path="C:\\Users\p.rudyakov\\PycharmProjects\\Netology_Rudyakov\\FSA_project_selenium\\Chromedriver_103\\chromedriver.exe")

try:
    driver.get(url=url)
    driver.save_screenshot("vk.png")
    time.sleep(5)

    driver.refresh(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
