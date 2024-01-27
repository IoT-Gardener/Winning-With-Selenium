import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://www.sporcle.com/games/RobPro/1-100-click-me')

frame = driver.find_element(By.XPATH, '//*[@id="sp_message_iframe_756623"]')
print("Found frame")
driver.switch_to.frame(frame)
print("Switched to frame")
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/button[2]').click()
print("Clicked accept")
driver.find_element(By.XPATH, '//*[@id="button-play"]').click()
print("Clicked play")

for i in range(0,100):
    button = f"border{i}"
    driver.find_element(By.XPATH, f'//*[@id="{button}"]').click()
    time.sleep(1.8)