from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

REGISTER_URL = "https://hospitalmanager-beta.vercel.app/patient-portal?register=true"

driver = webdriver.Chrome()

try:
    driver.get(REGISTER_URL)
    wait = WebDriverWait(driver, 15)

    # --- 1. First name ---
    first = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="First name"]'))
    )
    first.clear()
    first.send_keys("Bot")

    # --- 2. Last name ---
    last = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last name"]')
    last.clear()
    last.send_keys("Account")

    # --- 3. Date of birth (type="date" needs YYYY-MM-DD) ---
    dob = driver.find_element(By.CSS_SELECTOR, 'input[type="date"]')
    dob.send_keys("1995-06-15")

    # --- 4. Gender <select> ---
    gender_select = driver.find_element(By.CSS_SELECTOR, 'select')
    Select(gender_select).select_by_value("male")

    # --- 5. Email ---
    email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    email.clear()
    email.send_keys("botaccount1@gmail.com")

    # --- 6. Password (first password field) ---
    password = driver.find_element(
        By.CSS_SELECTOR, 'input[type="password"][placeholder="Password (8+ characters)"]'
    )
    password.clear()
    password.send_keys("StrongPass123!")

    # --- 7. Confirm password (second password field) ---
    confirm = driver.find_element(
        By.CSS_SELECTOR, 'input[type="password"][placeholder="Confirm password"]'
    )
    confirm.clear()
    confirm.send_keys("StrongPass123!")

    # --- 8. Click "Create account" ---
    create_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Create account')]")
        )
    )
    create_btn.click()

    # --- 9. Wait for navigation or error ---
    try:
        wait.until(lambda d: "register=true" not in d.current_url)
        print(f"✅ Account creation likely succeeded. URL: {driver.current_url}")
    except TimeoutException:
        print("⚠️ Still on register page — checking for error")
        driver.save_screenshot("register_error.png")
        print("📸 Screenshot saved: register_error.png")

    import time
    time.sleep(3)

finally:
    driver.quit()