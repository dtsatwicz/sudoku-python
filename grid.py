import flet as ft

if __name__ == "__main__":



    def main(page: ft.Page):
        page.title = "gridview"
        page.theme_mode = ft.ThemeMode.LIGHT
        ##page.theme_mode = ft.ThemeMode.DARK
        page.padding = 5
        page.window_height=500
        page.window_width=320
        page.update()

        images = ft.GridView(
            expand=1,
            runs_count = 9,
            max_extent=81,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )

        page.add()

        for i in range (0,81):
            images.controls.append(
                ft.Image(
                    src=ft.Text(str(i)),
                    fit=ft.ImageFit.NONE,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                )
            )
        page.update()

    ft.app(target=main)
