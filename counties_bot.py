import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://www.sporcle.com/games/RamRaider3546/hand-drawn-counties-of-england')

frame = driver.find_element(By.XPATH, '//*[@id="sp_message_iframe_756623"]')
print("Found frame")
driver.switch_to.frame(frame)
print("Switched to frame")
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/button[2]').click()
print("Clicked accept")
driver.find_element(By.XPATH, '//*[@id="button-play"]').click()
print("Clicked play")


counties = ["Bedfordshire", "Berkshire", "Bristol", "Buckinghamshire", "Cambridgeshire", "Cheshire",
            "City of London", "Cornwall", "County Durham", "Cumbria", "Derbyshire", "Devon", "Dorset",
            "East Riding", "East Sussex", "Essex", "Gloucestershire", "Greater London", "Greater Manchester",
            "Hampshire", "Herefordshire", "Hertfordshire", "Isle of Wight", "Kent", "Lancashire",
            "Leicestershire", "Lincolnshire", "Merseyside", "Norfolk", "North Yorkshire","Northamptonshire",
            "Northumberland", "Nottinghamshire", "Oxfordshire", "Rutland",
            "Shropshire", "Somerset", "South Yorkshire", "Staffordshire", "Suffolk", "Surrey", 
            "Tyne and Wear", "Warwickshire", "West Midlands", "West Sussex", "Wiltshire",
            "Worcestershire", "West Yorkshire"]

for county in counties:
    driver.find_element(By.XPATH, f'//*[@id="gameinput"]').send_keys(county)
    time.sleep(2.5)