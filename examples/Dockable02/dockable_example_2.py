# ==========================================
# Project: PyRetroGui
# File: dockable_example_2
# Author: Davide Sattin
# Created: 18/02/2026 13:29
# Description:Example Create the main screen with dockable panel
# ==========================================
from examples.Dockable01.main_container_02 import MainContainer
from pyretrogui.app import App

# Create the App.
# This example demonstrate the header, content, footer panel arrangement.
# Check the custom implementation of DockableContainer in the MainContainer class.
app =  App.create_instance("Main Screen", (600,600), (8,16))
app.run(MainContainer02)