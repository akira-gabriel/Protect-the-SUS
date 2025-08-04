from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()

driver.get("https://datasus.saude.gov.br/acesso-a-informacao/morbidade-hospitalar-do-sus-sih-sus/")

time.sleep(2)

def select_option(i=0):

    wait = WebDriverWait(driver, 10)
    radios = wait.until(EC.presence_of_all_elements_located((By.NAME, "radiobutton")))
    radios[i].click()
    time.sleep(3)

    select_element = driver.find_element(By.ID, "mySelect")
    options = select_element.find_elements(By.TAG_NAME, "option")
    options[1].click()
    

    select_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "L"))
    )

    options = select_element.find_elements(By.TAG_NAME, "option")

    options[1].click()

select_option()