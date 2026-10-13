# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome() 
# driver.get("https://example.com")
# driver.get("C:\\Users\\HP\\Desktop\\python_for-_backend\\week 7\\index.html")
# print(driver.title)


# element = driver.find_element(By.CSS_SELECTOR, "h1")
# print(element.text)


# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# driver.get("https://learncompletefrontend.vercel.app/")
driver.get("https://hospitalmanager-beta.vercel.app/")


element = driver.find_element(By.CSS_SELECTOR, "h1")
print(element.text)

driver.quit()  # always close!