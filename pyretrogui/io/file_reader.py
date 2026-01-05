# ==========================================
# Project: PyRetroGUI
# File: file_reader
# Author: Davide Sattin 
# Created: 05/01/2026 16:21
# Description: Helper Class for file management.
# ==========================================
class FileReader:
    @staticmethod
    def read_text_file(path: str) -> str:
        """
        Legge un file di testo e restituisce il contenuto come stringa.
        """
        with open(path, "r", encoding="utf-8") as file:
            return file.read()