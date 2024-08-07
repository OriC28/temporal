from flet import Page, Column, Text, Container, Control, icons, colors, Icon
import flet as ft


class CustomGreetingText(ft.Text):
    def __init__(self, name: str):
        super().__init__(
            # value=f"Hello, {name} !",
            # color=ft.colors.RED,
            # size=23
        )

        self.value = f"Hello, {name} !"
        self.color = ft.colors.RED
        self.size = 23

def main(page: ft.Page):
    page.add(CustomGreetingText("TheEthicalBoy"))

ft.app(main)