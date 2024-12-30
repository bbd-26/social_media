from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your ChromeDriver
PATH = "D:/python/chromedriver-win64/chromedriver.exe"

# Create ChromeOptions object
options = Options()
options.chrome_executable_path = "D:/chromedriver-win64/chromedriver.exe"

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.get("http://market.dcview.com/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.title_is("DCView 二手市場"))

# Find the search input element and perform a search
search = driver.find_element(By.NAME, "keyword")
search.send_keys("A73")
search.send_keys(Keys.RETURN)

# Wait for the search results to load
locator = (By.CLASS_NAME, "fa-search")  # Update this with the correct class name
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(locator),
    "找不到指定的元素"
)

# Find all title elements and print their text
titles = driver.find_elements(By.CLASS_NAME, "h5")  # Use find_elements to get a list
for title in titles:
    print(title.text)

# Close the browser
driver.quit()
