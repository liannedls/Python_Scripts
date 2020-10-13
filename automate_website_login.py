#Script to load webpage 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_window_size(1600,800)
driver.set_window_position(0,0)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
print(driver.execute_script("return navigator.userAgent;"))

# Opening the website 
url = "https://example.com"
driver.get(url) 
time.sleep(5)
print("Waiting for website to load.")
 
# Complete code using the specific selenium actions for your webpage
