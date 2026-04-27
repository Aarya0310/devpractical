from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up driver
driver = webdriver.Chrome()

# Open the HTML file
driver.get("file://" + r"C:\Users\sit.lab1\Downloads\simple-web-app\index.html")

# Test 1: Verify page title
title = driver.title
print(f"Page title: {title}")
assert title == "My App", f"Expected 'My App', got '{title}'"
print("✓ Test 1 passed: Page title is correct")

# Test 2: Verify heading text
heading = driver.find_element(By.TAG_NAME, "h1").text
print(f"Heading text: {heading}")
assert heading == "Welcome to My App", f"Expected 'Welcome to My App', got '{heading}'"
print("✓ Test 2 passed: Heading text is correct")

# Test 3: Verify counter starts at 0
counter = driver.find_element(By.ID, "counter").text
print(f"Initial counter: {counter}")
assert counter == "0", f"Expected '0', got '{counter}'"
print("✓ Test 3 passed: Counter starts at 0")

# Test 4: Test increment button
driver.find_element(By.ID, "incrementBtn").click()
time.sleep(0.5)
counter = driver.find_element(By.ID, "counter").text
print(f"Counter after increment: {counter}")
assert counter == "1", f"Expected '1', got '{counter}'"
print("✓ Test 4 passed: Increment button works")

# Test 5: Test decrement button
driver.find_element(By.ID, "decrementBtn").click()
time.sleep(0.5)
counter = driver.find_element(By.ID, "counter").text
print(f"Counter after decrement: {counter}")
assert counter == "0", f"Expected '0', got '{counter}'"
print("✓ Test 5 passed: Decrement button works")

# Test 6: Test reset button
driver.find_element(By.ID, "incrementBtn").click()
driver.find_element(By.ID, "incrementBtn").click()
time.sleep(0.5)
driver.find_element(By.ID, "resetBtn").click()
time.sleep(0.5)
counter = driver.find_element(By.ID, "counter").text
print(f"Counter after reset: {counter}")
assert counter == "0", f"Expected '0', got '{counter}'"
print("✓ Test 6 passed: Reset button works")

# Test 7: Test form submission
name_input = driver.find_element(By.ID, "nameInput")
name_input.send_keys("John Doe")
driver.find_element(By.ID, "contactForm").submit()
time.sleep(0.5)
message = driver.find_element(By.ID, "formMessage")
print(f"Form message displayed: {message.is_displayed()}")
assert message.is_displayed(), "Form message should be visible"
print("✓ Test 7 passed: Form submission works")

# Clean up
driver.quit()

print("\n✅ All tests passed!")