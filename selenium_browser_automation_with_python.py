from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

# Find all the anchor tags on the page 
links = driver.find_elements("xpath", "//a[@href]")

for link in links:
    # print(link.get_attribute("innerHTML"))
    # if link contains "Books" click on link and break the loop
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break 

book_links = driver.find_elements("xpath", 
"//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]]")