import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

try:
    from __dwnldDrivers.versions import get_chrome_version, get_major_version
    v = int(get_major_version(get_chrome_version()))
except:
    v = 146

driver = uc.Chrome(version_main=v)
driver.get('https://www.opencccapply.net/uPortal/AccountCreation/251/false/en')
time.sleep(10)

with open('scratch/form_source3.html', 'w') as f:
    f.write(driver.page_source)

print("Current URL:", driver.current_url)
driver.quit()
