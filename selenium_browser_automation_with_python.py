import time
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

# find the links within the div that contain the class 'elementor-column-wrap'that contains the h2
# tag with '7 IN 1' within it, limit results to divs that contain only two anchor tags and retrieve 
# those tags
book_links = driver.find_elements("xpath", 
"//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

# Loop through the book links and print the inner html of each 
# for book_link in book_links:
#     print(book_link.get_attribute("href"))

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

# find anchor elements with a span that contains 'Paperback', then go into those elements and find the span that contains the text '$'
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print(button.get_attribute("innerHTML"))