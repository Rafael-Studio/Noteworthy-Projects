"""
Python exercise from "Python Journey" Python training by Hashtag.

Challenge: given a file ("produtos.csv") containing various information about hypothetical products,
such as code, brand, type, category, price, note, etc., create an automation program to read and extract
the information on that file and register them in the e-commerce mock website:
(https://dlp.hashtagtreinamentos.com/python/intensivao/login).

Important: the program must use the following libraries - PyAutoGUI; pandas.
"""

import pyautogui
import pandas as pd
from time import sleep

# setting a fixed delay between each command to ensure the website is already open/updated before commands are issued.
pyautogui.PAUSE = 0.3

# open browser (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# accessing website
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)

# sign-up process
# selecting "email" field
pyautogui.press("tab")

# filling the "email"  and "password" fieldd
pyautogui.write("pythonimpressionador@gmail.com")  # mock email
pyautogui.press("tab")
pyautogui.write("udhfe98046")  # mock password
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)
