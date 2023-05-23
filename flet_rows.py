import flet as ft

if __name__ == "__main__":

    def main(page: ft.Page):

        page.title="Sudoku"
        page.window_height=400
        page.window_width=300

        cell_containers = []
        cell_index = 0
        sudoku_numbers = ['1','2','3','4','5','6','7','8','9']
        set_cell_value  = ''
        action_to_take = 'no action set'


        new_value = ft.TextField(label='1-9', autofocus=True)

        def cell_of(row, col):
            return ((row -1) * 9 ) + col -1

        def row_of(cell_index):
            if cell_index <=  8: return 1
            if cell_index <= 17: return 2
            if cell_index <= 26: return 3
            if cell_index <= 35: return 4
            if cell_index <= 44: return 5
            if cell_index <= 53: return 6
            if cell_index <= 62: return 7
            if cell_index <= 71: return 8
            return 9

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
    
        def cell_click(e):
            global cell_index

            if e.control.data["cell_highlighted"]==True:
                e.control.data["cell_highlighted"]=False
                e.control.bgcolor = ft.color=e.control.data["cell_bgcolor"]
            else:
                e.control.bgcolor=ft.colors="red"
                e.control.data["cell_highlighted"]=True
                cell_index = e.control.data["cell_index"]
            page.update()

        def action_click():
            global cell_containers
            global cell_index

            print (cell_index, cell_containers[cell_index])
            print ("new_value=", new_value.current.value)
            if new_value.current.value in sudoku_numbers:
                cell_containers[cell_index].control.content = ft.Text(new_value.current.value)
                cell_containers[cell_index].control.data["cell_current_value"] = new_value.current.value
                cell_containers[cell_index].control.data["cell_value_source"] = "cell_click"
                cell_containers[cell_index].control.alignment=ft.alignment.center
                cell_containers[cell_index].control.bgcolor=ft.colors="green"
            elif new_value.current.value == '':
                cell_containers[cell_index].control.content = ft.Text(new_value.current.value)
                cell_containers[cell_index].control.alignment=ft.alignment.center
                cell_containers[cell_index].control.bgcolor=ft.colors="blue"
            elif new_value.current.value == 'rn':
                print("rn row_needs", row_of(cell_containers[cell_index].control.data["cell_index"]))
                row_needs(row_of(cell_containers[cell_index].control.data["cell_index"]))

            elif new_value.current.value == 'cn':
                print ("col_needs")    
            elif new_value.current.value == 'bn':
                print ("box needs")    
            else:
                print ("something else", new_value.current.value)    

            page.update()

        def row_needs(row):
            print ("row_needs", row)

        def set_number_to(e):
            global set_cell_value  
            global action_to_take  

            set_cell_value = e.control.data["sudoku_number"]
            action_to_take= 'set_cell_to'
            page.update()

        def cell_clicked(e):
            global set_cell_value
            global action_to_take  
            
            if action_to_take == "no action set":
                return

            elif action_to_take == "set_cell_to":
                e.content = ft.Text(set_cell_value)
                e.control.data["cell_current_value"] = set_cell_value
                e.control.data["cell_value_source"] = "set_cell_to"
                e.bgcolor=ft.colors="green"

                page.update()

            else:
                return    

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

        sudoku_grid()

        action_to_take = ft.TextField(label="action to take", width=300)
        action_to_take.value = "no action set"
        page.add( action_to_take)
                

        set_numbers = []
        for number in sudoku_numbers:
            c = ft.Container(
				    content=ft.Text(number),
					width=20,
					height=20,
					bgcolor="white",
					ink=False,
					data= {
						"sudoku_number": number,
                        "bgcolor": "white",
                        },
					on_click=set_number_to,
					)

            set_numbers.append(c)
        page.add(ft.Row(set_numbers))

    ft.app(target=main)
