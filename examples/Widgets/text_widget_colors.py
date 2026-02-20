# ==========================================
# Project: PyRetroGUI
# File: text_widget_colors
# Author: Davide Sattin 
# Created: 04/01/2026 11:00
# Description:Example Create the main screen, with text widget and colors.
# ==========================================
from pyretrogui.ui_elements.text_widget import TextWidget
from pyretrogui.app import App

#Create the app.
app = App.create_instance("Main Screen", (600,600), (8,16))
app.run(TextWidget)
