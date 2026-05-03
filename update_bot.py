import re

with open('bot.py', 'r') as f:
    content = f.read()

# Update import
content = content.replace('import seleniumwire.undetected_chromedriver.v2 as uc', 'import seleniumwire.undetected_chromedriver as uc')

# Replace find_element_by_*
content = re.sub(r'\.find_element_by_id\((.*?)\)', r'.find_element(By.ID, \1)', content)
content = re.sub(r'\.find_element_by_xpath\((.*?)\)', r'.find_element(By.XPATH, \1)', content)
content = re.sub(r'\.find_element_by_name\((.*?)\)', r'.find_element(By.NAME, \1)', content)
content = re.sub(r'\.find_element_by_class_name\((.*?)\)', r'.find_element(By.CLASS_NAME, \1)', content)
content = re.sub(r'\.find_element_by_tag_name\((.*?)\)', r'.find_element(By.TAG_NAME, \1)', content)
content = re.sub(r'\.find_element_by_css_selector\((.*?)\)', r'.find_element(By.CSS_SELECTOR, \1)', content)

# Replace find_elements_by_*
content = re.sub(r'\.find_elements_by_id\((.*?)\)', r'.find_elements(By.ID, \1)', content)
content = re.sub(r'\.find_elements_by_xpath\((.*?)\)', r'.find_elements(By.XPATH, \1)', content)
content = re.sub(r'\.find_elements_by_name\((.*?)\)', r'.find_elements(By.NAME, \1)', content)
content = re.sub(r'\.find_elements_by_class_name\((.*?)\)', r'.find_elements(By.CLASS_NAME, \1)', content)
content = re.sub(r'\.find_elements_by_tag_name\((.*?)\)', r'.find_elements(By.TAG_NAME, \1)', content)
content = re.sub(r'\.find_elements_by_css_selector\((.*?)\)', r'.find_elements(By.CSS_SELECTOR, \1)', content)

with open('bot.py', 'w') as f:
    f.write(content)

print("Updated bot.py successfully")
