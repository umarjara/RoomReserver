import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Script to reserve room 412 at 18th Avenue Library from 4:00 - 4:30 one week from now 

# Open the reservation page in Chrome
driver = webdriver.Chrome('C:\\Users\\Umar\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://library.osu.edu/room-reservation')

# Login to the OSU's system
login_button = driver.find_element_by_css_selector('a.btn')
login_button.click()
time.sleep(2) 
username_box = driver.find_element_by_id('username')
username_box.send_keys(os.environ.get('OSU_USER'))
pass_box = driver.find_element_by_id('password')
pass_box.send_keys(os.environ.get('OSU_PASS'))
submit_button = driver.find_element_by_id('submit')
submit_button.click()
driver.implicitly_wait(3) 

# Select 18th Ave library room 412
select_room_button = driver.find_element_by_id('openlocation')
select_room_button.click()
library_button = driver.find_element_by_css_selector('li.location:nth-child(5) > a:nth-child(1)')
library_button.click()
room_412 = driver.find_element_by_xpath('/html/body/div/div[5]/div[2]/ul/div[2]/div[11]/li/table/tbody/tr/td[1]')
room_412.click()

# Go to exactly one week from now
check_button = driver.find_element_by_id('update-calendar')
check_button.click()
five_day_button = driver.find_element_by_id('fiveDayAgenda')
five_day_button.click()
next_button = driver.find_element_by_id('next')
next_button.click()
time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
zero_elem = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]')

# Click on the day
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element(zero_elem)
action.click()
action.perform()
time.sleep(2)

# Fill out the reservation form fields and submit
start_time = driver.find_element_by_xpath('//*[@id="new_reservation"]/div[2]/input')
start_time.clear()
start_time.send_keys('4:00 PM')
end_time = driver.find_element_by_xpath('//*[@id="new_reservation"]/div[3]/input')
end_time.clear()
end_time.send_keys('4:30 PM')
participants = driver.find_element_by_xpath('//*[@id="new_reservation"]/div[5]/select/option[text() = 5]')
participants.click()
reason = driver.find_element_by_xpath('//*[@id="new_reservation"]/div[6]/select/option[text() = \'Group Study Session / Exam Prep\']')
reason.click()
save_button = driver.find_element_by_xpath('//*[@id="new_reservation"]/input[4]')
save_button.click()








