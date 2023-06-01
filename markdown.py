import flet as ft

def main(page: ft.Page):
    page.title = "markdown Editor"
    page.theme_mode="light"
    page.theme_mode="system"
    page.theme_mode="dark"
    page.window_height=600
    page.window_width=400

    page.appbar = ft.AppBar(
        title=ft.Text("Markdown Editor", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLUE,
    )

    text_field = ft.TextField(
        value="## Hello from Markdown",
        multiline=True,
        ##expand=True,
        ##height=page.window_height,
        height=100,
        border_color=ft.colors.TRANSPARENT,
    )
        
    page.add(text_field)
    
    page.add(ft.Text(value="Hello, world!"))
    page.add(ft.Text("Hello, world!"))

ft.app(target=main)
