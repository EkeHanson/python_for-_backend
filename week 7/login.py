from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 1. Launch the browser ---
driver = webdriver.Chrome()

try:
    # --- 2. Open the login page ---
    driver.get("https://hospitalmanager-beta.vercel.app/login")

    # --- 3. Wait for the email field to be ready ---
    wait = WebDriverWait(driver, 15)
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    # --- 4. Fill in the email ---
    email_input.clear()
    email_input.send_keys("botaccount1@gmail.com")

    # --- 5. Fill in the password ---
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("StrongPass123!")

    # --- 6. Click the Sign in button ---
    # The button has type="submit" and no ID, so CSS selector is cleanest:
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    sign_in_btn.click()

    # --- 7. Optional: wait a few seconds so you can see what happens ---
    import time
    time.sleep(5)

    # --- 8. Confirm we left the login page (login succeeded) ---
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    if "login" not in driver.current_url:
        print("✅ Login appears successful!")
    else:
        print("⚠️ Still on login page — check credentials or error message.")

finally:
    driver.quit()