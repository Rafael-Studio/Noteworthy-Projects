"""
Python exercise from "Python Journey" Python training by Hashtag.

Challenge: given a CSV file ("produtos.csv") containing various information about hypothetical products,
such as "codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs", create an automation program
to read and extract the information on that file and register them in the e-commerce mock website:
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

# pause to ensure that the browser window and website have loaded properly before proceeding with the next steps.
sleep(3)

# sign-up process
# selecting "email" field
pyautogui.press("tab")

# filling the "email"  and "password" fields
pyautogui.write("pythonimpressionador@gmail.com")  # mock email
pyautogui.press("tab")
pyautogui.write("udhfe98046")  # mock password
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)

# Creating a table using pandas and the information contained in the file.
table = pd.read_csv("produtos.csv")

# Registering a product in the website
for line in table.index:
    # clicking the "codigo" field in the website
    pyautogui.click(x=653, y=294)  # Attention: coordinates may vary according to resolution. May need calibration

    # fetching from the table the value to be registered in the website
    code = table.loc[line, "codigo"]

    # filling the field
    pyautogui.write(str(code))

    # next field
    pyautogui.press("tab")

    # continuing
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[line, "obs"]

    # In this case, some values in the "obs" field were flagged as NaN. The following line of code addresses this issue
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # clicks the "send" button. Product will be registered and the process will start again

    # full scroll so the script can correctly click on the "codigo" field again
    pyautogui.press("home")
