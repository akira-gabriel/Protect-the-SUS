from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()

driver.get("https://datasus.saude.gov.br/acesso-a-informacao/morbidade-hospitalar-do-sus-sih-sus/")

time.sleep(2)

def csv_download():

    i = 0
    j = 0
    wait = WebDriverWait(driver, 10)
    radios = wait.until(EC.presence_of_all_elements_located((By.NAME, "radiobutton")))
    radios[i].click()

    time.sleep(3)

    select_element = driver.find_element(By.ID, "mySelect")
    options = select_element.find_elements(By.TAG_NAME, "option")
    options[1].click()
    

    select_linha = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "L"))
    )
    select_linha = Select(select_linha)

    linha_option = [option for option in select_linha.options]
    linha_list = [opt.get_attribute("value") for opt in linha_option]    
    
    select_element = linha_list[1]

    time.sleep(3)
    
    select_linha.select_by_value(select_element)

    time.sleep(3)

csv_download()