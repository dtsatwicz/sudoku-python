
import flet as ft

if __name__ == "__main__":

    def main(page: ft.Page):

        page.title="Sudoku"
        page.window_height=400
        page.window_width=300

        result = ft.Text(value='0')
        new_cell_value = ft.Text(value='0')
        action_to_take = ft.Text(value='No Action Set')
        next_cell_value = ''
        new_number = ''

        sudoku_numbers = ['1','2','3','4','5','6','7','8','9']

        def box_of(row, col):
            if row in range (1,4):
                if col in range (1,4): return 1
                if col in range (4,7): return 2
                return 3
            if row in range (4,7):
                if col in range (1,4): return 4
                if col in range (4,7): return 5
                return 6
            if col in range (1,4): return 7
            if col in range (4,7): return 8
            return 9
    
        def cell_clicked(e):
            global next_cell_value
            global new_number
            print ('cell_clicked', e.control.data)
            print ('new_cell_value=', next_cell_value, new_number)

            e.control.content = ft.Text(next_cell_value)
            e.control.bfcolor="red"

            page.update()

        def number_clicked(e):
            global next_cell_value
            ###global action_to_take
            global new_number

            print ('number_clicked', e.control.data)

            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text('Set Cell To'))
            page.update()

            new_number = e.control.data["sudoku_number"]

            new_cell_value.current.controls.clear()
            new_cell_value.current.controls.append(ft.Text(new_number))
            next_cell_value = new_number
            page.update()

        def sudoku_grid():
            global cell_containers
            global cell_index

            cell_containers=[]
            cell_index = 0
            for row in range (1,10):
                this_row = []
                for col in range (1,10):
                    c = ft.Container(
						content=ft.Text("__"),
						width=20,
						height=20,
						bgcolor="blue",
						ink=False,
						data= {"cell_index": cell_index,
								"cell_row": row,
								"cell_col": col,
								"cell_box": box_of(row,col),
								"cell_current_value": '',
                                "cell_bgcolor": "blue",
                                "cell_highlighted": False,
								"cell_value_source": ''},
						on_click=cell_clicked,
						)
                    cell_index += 1

                    cell_containers.append(c)
                    this_row.append(c)

                page.add(ft.Row(this_row))

            ##page.add(
                ##ft.Row(controls=[action_to_take],ref=action_to_take,data=ft.Text('No Action Set')),
                ##ft.Row(controls=[new_cell_value],ref=new_cell_value,data='__'),
                ##)
            page.add(ft.Row(controls=[action_to_take],ref=action_to_take,data=ft.Text('No Action Set')))
            page.add(ft.Row(controls=[new_cell_value],ref=new_cell_value,data=ft.Text('__')))

            set_numbers = []        
            for number in sudoku_numbers:
                c = ft.Container(
    				    content=ft.Text(number),
    			    	width=20,
    				    height=20,
    				    bgcolor="green",
    				    ink=False,
					    data= {
    					    "sudoku_number": number,
                           "bgcolor": "green",
                            },
    				    on_click=number_clicked,
    				)

                set_numbers.append(c)
            page.add(ft.Row(set_numbers))

        sudoku_grid()

    ft.app(target=main)