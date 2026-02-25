# ==========================================
# Project: PyRetroGUI
# File: dockable_example_3
# Author: Davide Sattin 
# Created: 22/02/2026 18:07
# Description:Example Create the main screen with dockable panel
# ==========================================
from examples.Dockable03.main_container_03 import MainContainer03
from pyretrogui.app import App

# Create the App.
# This example demonstrates the header, 2 content, footer panel arrangement.
# Check the custom implementation of DockableContainer in the MainContainer class.
app =  App.create_instance("Main Screen", (600,600), (8,16))
app.run(MainContainer03)