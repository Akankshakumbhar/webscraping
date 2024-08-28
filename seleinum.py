from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Set up ChromeDriver options if needed
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment if you don't need a GUI

# Start ChromeDriver
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')  # Replace with your URL

# Perform actions with the driver

box=driver.find_element_by_xpath('/html/body/div[1]')
box.send_keys("what is scraping") # allow to input text in search box
box.send_keys(Keys.ENTER)

#print(driver.title)  # Example: Print the title of the webpage

#clicking button
button=driver.find_element_by_xpath('')
button.click()

#or
link=driver.find_element_by_xpath('').click()
driver.save_screenshot()#filename in which we want to save the screen short
driver.execute_script('return document.body.scrollHeigth')




# Quit the driver

