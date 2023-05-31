

import flet as ft

if __name__ == "__main__":

    def click_init():
        pass
    def click_cell_can_be():
        pass    
    def main(page: ft.Page):

        page.title="Ft page tests"
        page.window_height=500
        page.window_width=500


        page.add(ft.Divider(height=10,thickness=5,color='black'))

        page.add( ft.Row(
	        		controls=[
	        			ft.ElevatedButton(text='Init',on_click=click_init),
	        			ft.ElevatedButton(text='Cell',on_click=click_cell_can_be),
	            		]
	                ),
                )
        page.add(ft.Divider(height=10,thickness=5,color='black'))

        page.add( ft.Row(
	        		controls=[
	        			ft.ElevatedButton(text='Init',on_click=click_init),
                        ft.VerticalDivider(width=10,thickness=5, color="white"),
	        			ft.ElevatedButton(text='Cell',on_click=click_cell_can_be),
	            		]
	                ),
                )
        page.add(ft.Divider(height=10,thickness=5,color='black'))

    ft.app(target=main)