from selenium import webdriver
from MyJsconConverter import MyJsconConverter

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://www.example-site.com") #Change website address

# Get all the cookies
mycookies = driver.get_cookies()

MyJsconConverter(mycookies)
if(mycookies):
    print(f"SameSite Cookie is: {mycookies[0]["sameSite"]}")
else:
    print("No cookies found") 
