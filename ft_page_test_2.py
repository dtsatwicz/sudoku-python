import flet as ft

def main(page: ft.Page):

    page.add(ft.Divider(height=5,thickness=5,color='black'))
    page.add(
        ft.Row(
            [
                ft.VerticalDivider(width=5, thickness=5, color="black"),
                ft.Container(
                    bgcolor=ft.colors.ORANGE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=3, thickness=1, color="black"),
                ft.Container(
                    bgcolor=ft.colors.BROWN_400,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=5, thickness=5, color="black"),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=3, thickness=1, color="black"),
                ft.Container(
                    bgcolor=ft.colors.GREEN_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=5, thickness=5, color="black"),
            ],
            spacing=0,
            expand=True,
        )
    )
    ##page.add(ft.Row(ft.Divider(height=3,thickness=1,color='black')))
    page.add(ft.Divider(height=1,thickness=1,color='black'))

    page.add(
        ft.Row(
            [
                ft.VerticalDivider(width=5, thickness=5, color="black"),
                ft.Container(
                    bgcolor=ft.colors.ORANGE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=3, thickness=1, color="black"),
                ft.Container(
                    bgcolor=ft.colors.BROWN_400,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=5, thickness=5, color="black"),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=3, thickness=1, color="black"),
                ft.Container(
                    bgcolor=ft.colors.GREEN_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.VerticalDivider(width=5, thickness=5, color="black"),
            ],
            spacing=0,
            expand=True,
        )
    )
    page.add(ft.Divider(height=1,thickness=5,color='black'))

ft.app(target=main)