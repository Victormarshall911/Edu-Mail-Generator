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
driver.get('https://www.opencccapply.net/gateway/apply?cccMisCode=251')
time.sleep(5)
try:
    create_btn = driver.find_element(By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'create')]")
    print("Found element:", create_btn.get_attribute('outerHTML'))
    if create_btn.get_attribute('href'):
        print("HREF:", create_btn.get_attribute('href'))
except Exception as e:
    print("Could not find create account button", e)

print("Current URL:", driver.current_url)
print("Page source:", driver.page_source[:500])
driver.quit()
