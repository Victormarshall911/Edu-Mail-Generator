import seleniumwire.undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    from __dwnldDrivers.versions import get_chrome_version, get_major_version
    v = int(get_major_version(get_chrome_version()))
except:
    v = 146

driver = uc.Chrome(version_main=v)
driver.get('https://www.opencccapply.net/uPortal/AccountCreation/251/false/en')
time.sleep(10) # wait for page to load

with open('scratch/form_source.html', 'w') as f:
    f.write(driver.page_source)

print("Current URL:", driver.current_url)
driver.quit()
