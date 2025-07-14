# 🤖 Product Registration Automation

This project is part of the **"Python Journey"** training by Hashtag Treinamentos. It automates the process of registering products into a mock e-commerce website using **data from a CSV file**, simulating human interaction with the browser.

## 🧠 Project Overview

The script reads a file named `produtos.csv`, which contains product details such as:

- `codigo` (product code)
- `marca` (brand)
- `tipo` (type)
- `categoria` (category)
- `preco_unitario` (unit price)
- `custo` (cost)
- `obs` (notes)

Using these values, the program **automatically fills out and submits** the product registration form at:

📎 [https://dlp.hashtagtreinamentos.com/python/intensivao/login](https://dlp.hashtagtreinamentos.com/python/intensivao/login)

## 🛠️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [`pandas`](https://pandas.pydata.org/) – For reading and processing the CSV data
- [`pyautogui`](https://pyautogui.readthedocs.io/) – For GUI automation (keyboard and mouse simulation)
- `time.sleep()` – To ensure page load synchronization

## 🚀 How to Run

1. Make sure you have Google Chrome installed and accessible via the system search.

2. Install dependencies (if needed):

   ```bash
   pip install pandas pyautogui
   Ensure the CSV file (produtos.csv) is in the same directory as the script and has the correct structure.


📄 CSV Format
Example of how your produtos.csv should look:

codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,BrandX,Mouse,Accessories,79.90,45.00,Wireless
002,BrandY,Keyboard,Accessories,129.90,80.00,
Note: The obs (notes) column is optional and may contain blank or NaN values.

💡 Highlights
Full browser automation from launch to login to form submission
Handles missing data (e.g., NaN in obs)
Simulates human interaction to bypass site limitations
Teaches practical use of pyautogui for automation tasks

⚠️ Important Notes
This script uses hardcoded screen coordinates, which may need adjustment depending on your screen resolution and UI layout.
The email and password used are placeholders and should be replaced with test credentials if you're replicating the environment.
