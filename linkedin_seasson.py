import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Open browser for manual login
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com/login")

# Wait for user to log in manually and press ENTER on the terminal after successfully logging in.
input(" Log in manually & press ENTER to save cookies...")

# Save session cookies
pickle.dump(driver.get_cookies(), open("linkedin_cookies.pkl", "wb"))
print("Cookies saved successfully!")
driver.quit()
