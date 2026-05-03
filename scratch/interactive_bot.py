import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    from __dwnldDrivers.versions import get_chrome_version, get_major_version
    v = int(get_major_version(get_chrome_version()))
except:
    v = 146

print("Starting Chrome...")
driver = uc.Chrome(version_main=v)
driver.get('https://www.opencccapply.net/uPortal/AccountCreation/251/false/en')

print("Waiting for email input...")
email_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "email"))
)

# Use a test email (e.g., from user's history "ralphfransis@gmail.com" or a temporary one)
# Wait, maybe it's better if I just prompt for an email or hardcode one for testing
test_email = "test.openccc.xyz123@gmail.com" 
email_input.send_keys(test_email)
print(f"Entered email: {test_email}")

submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_btn.click()

print("Clicked send code. Waiting for OTP input field...")
# wait for OTP field
try:
    otp_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "verificationCode"))
    )
    print("Found OTP input field!")
    with open('scratch/otp_page.html', 'w') as f:
        f.write(driver.page_source)
except Exception as e:
    print("Error finding OTP input:", e)
    with open('scratch/error_page.html', 'w') as f:
        f.write(driver.page_source)

driver.quit()
