
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Bug report
Programming language: Python
Selenium actions:
1. Open website
2. Write text "Paper Camp" in the search input field
3. Press ENTER (Keys.ENTER)
Expected results: after ENTER action the search function should begin and find "Paper Camp" movies.
Actual results: after ENTER action the user is redirected to the homepage:
1,2 Search results page -> search field -> text -> ENTER -> user is redirected to homepage.
3 Homepage -> search field -> text -> ENTER -> user is redirected to homepage.
'''

driver = webdriver.Chrome(executable_path = "C:\\Users\\Kamile\\Downloads\\chromedriver.exe")

# 1. Search results page search field
driver.get('https://www.wixgrow-qa2021.com/search-results/')
driver.find_element_by_class_name("Input1417681740__nativeInput").send_keys("Paper Camp", Keys.ENTER)

# 2. Search results page search field
driver.get('https://www.wixgrow-qa2021.com/search-results/')
driver.find_element_by_class_name("Input1417681740__nativeInput").send_keys("Paper Camp", Keys.RETURN)

# 3. Homepage search field
driver.get('https://www.wixgrow-qa2021.com/')
driver.find_element_by_id("input_search-box-input-comp-km1y414l").send_keys("Paper Camp", Keys.ENTER)











