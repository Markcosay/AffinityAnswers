from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

url = "https://www.olx.in/items/q-car-cover"
driver.get(url)

try:
    listings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[data-aut-id='itemBox']"))
    )
except Exception as e:
    print("Failed to load listings:", e)
    driver.quit()
    exit()

with open("olx_car_covers.txt", "w", encoding="utf-8") as f:
    for listing in listings:
        try:
            title = listing.find_element(By.CSS_SELECTOR, "span[data-aut-id='itemTitle']").text
        except:
            title = "No title"

        try:
            price = listing.find_element(By.CSS_SELECTOR, "span[data-aut-id='itemPrice']").text
        except:
            price = "No price"

        try:
            location = listing.find_element(By.CSS_SELECTOR, "span[data-aut-id='item-location']").text
        except:
            location = "No location"

        f.write(f"Title: {title}\nPrice: {price}\nLocation: {location}\n{'-'*40}\n")

print("✅ Done! Check 'olx_car_covers.txt'.")

driver.quit()
