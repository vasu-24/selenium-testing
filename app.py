from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


username = "9380936730"
password = "vasuc@2004"
wrong_password = " voidnv"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

# Test Case 1: Successful Login
def test_successful_login(driver, username, password):
    driver.get("http://www.facebook.com")
    
    try:
        username_field = wait_for_element(driver, By.ID, "email")
        password_field = wait_for_element(driver, By.ID, "pass")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        element = wait_for_element(driver, By.CSS_SELECTOR, "div[aria-label='Facebook']")
        print("Test Case 1: Successful Login - Passed")
    except TimeoutException:
        print("Test Case 1: Successful Login - Failed")
        driver.save_screenshot("test_case_1_failed.png")

# Test Case 2: Login with Incorrect Password
def test_login_incorrect_password(driver, username, wrong_password):
    driver.get("http://www.facebook.com")
    
    try:
        username_field = wait_for_element(driver, By.ID, "email")
        password_field = wait_for_element(driver, By.ID, "pass")
        
        username_field.send_keys(username)
        password_field.send_keys(wrong_password)
        
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        element = wait_for_element(driver, By.CSS_SELECTOR, "div._9ay7")
        print("Test Case 2: Login with Incorrect Password - Passed")
    except TimeoutException:
        print("Test Case 2: Login with Incorrect Password - Failed")
        driver.save_screenshot("test_case_2_failed.png")

# Test Case 3: Login with Empty Fields
def test_login_empty_fields(driver):
    driver.get("http://www.facebook.com")
    
    try:
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        element = wait_for_element(driver, By.CSS_SELECTOR, "div._9ay7")
        print("Test Case 3: Login with Empty Fields - Passed")
    except TimeoutException:
        print("Test Case 3: Login with Empty Fields - Failed")
        driver.save_screenshot("test_case_3_failed.png")

# Test Case 4: Check for Error Messages
def test_check_error_messages(driver, username, wrong_password):
    driver.get("http://www.facebook.com")
    
    try:
        username_field = wait_for_element(driver, By.ID, "email")
        password_field = wait_for_element(driver, By.ID, "pass")
        
        username_field.send_keys(username)
        password_field.send_keys(wrong_password)
        
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        error_message = wait_for_element(driver, By.CSS_SELECTOR, "div._9ay7")
        print("Test Case 4: Check for Error Messages - Passed")
        print("Error Message:", error_message.text)
    except TimeoutException:
        print("Test Case 4: Check for Error Messages - Failed")
        driver.save_screenshot("test_case_4_failed.png")

# Main function to run all test cases
def main():
    driver = webdriver.Chrome(service=service)
    
    try:
        test_successful_login(driver, username, password)
        driver.delete_all_cookies()
        
        test_login_incorrect_password(driver, username, wrong_password)
        driver.delete_all_cookies()
        
        test_login_empty_fields(driver)
        driver.delete_all_cookies()
        
        test_check_error_messages(driver, username, wrong_password)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
# hi how are you i am good  and wt about you can i know ur name please just for the enquire purpose