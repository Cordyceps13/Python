import flet as ft
from flet import *

def main(page: ft.Page):
    page.title = "Calculadora"
    page.update()

    def btn_click(e):
        pass 

ft.app(target=main)