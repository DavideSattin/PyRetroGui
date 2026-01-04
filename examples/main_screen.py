# ==========================================
# Project: PyRetroGUI
# File: main_screen
# Author: Davide Sattin 
# Created: 04/01/2026 11:00
# Description:
# ==========================================
from pyretrogui.UIPanel import TextWidget
from pyretrogui.app import App

# width = int(300 / 8) * 8
# height = int(300 / 16) * 16
# print(width, height)

app = App("Main Screen", (300,300), (8,16))
app.run(TextWidget)
