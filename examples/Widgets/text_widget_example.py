# ==========================================
# Project: PyRetroGUI
# File: main_screen
# Author: Davide Sattin 
# Created: 04/01/2026 11:00
# Description:Example Create the main screen.
# ==========================================
from pyretrogui.ui_elements.text_widget import TextWidget
from pyretrogui.io.file_reader import FileReader
from pyretrogui.app import App

my_text_widget = TextWidget()
my_text_widget.text = FileReader.read_text_file("..\lorem_ipsum.txt")


#Create the Main screen.
app = App.create_instance("Main Screen", (600,600), (8,16))
app.run(my_text_widget)
