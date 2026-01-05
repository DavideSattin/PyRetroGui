# ==========================================
# Project: PyRetroGUI
# File: main_screen
# Author: Davide Sattin 
# Created: 04/01/2026 11:00
# Description:Example Create the main screen.
# ==========================================
from pyretrogui.ui_panel import TextWidget
from pyretrogui.app import App

#Create the Main screen.
app = App("Main Screen", (600,600), (8,16))
app.run(TextWidget)
