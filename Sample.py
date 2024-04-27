import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()

#table=driver.find_element(By.XPATH,"//table[@id='customers']")

#table=driver.find_element(By.XPATH,"(//table)[1]")

#list_table=driver.find_elements(By.TAG_NAME,"table")
#table=list_table[0]

#Scenario-3
table=driver.find_element(By.XPATH,"//table[@id='customers']")

list_Rows=table.find_elements(By.TAG_NAME,"tr")

for each_row in list_Rows:

    list_data=each_row.find_elements(By.TAG_NAME,"td")
    for each_data in list_data:
        txt=each_data.text
        txt.startswith("Cana")
        print(txt)

time.sleep(5)



