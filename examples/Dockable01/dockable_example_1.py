# ==========================================
# Project: PyRetroGUI
# File: main_screen
# Author: Davide Sattin 
# Created: 04/01/2026 11:00
# Description:Example Create the main screen.
# ==========================================
from examples.Dockable01.main_container import MainContainer
from pyretrogui.app import App

#Create the App.
app =  App.create_instance("Main Screen", (600,600), (8,16))
app.run(MainContainer)
