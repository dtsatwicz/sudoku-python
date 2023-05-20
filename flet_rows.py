import flet as ft

if __name__ == "__main__" or True:

    cell_containers = []
    sudoku_numbers = ['1','2','3','4','5','6','7','8','9']
    highlighted_cell = ''

    def main(page: ft.Page):
        page.title="Sudoku"
        page.window_height=400
        page.window_width=300
        ##page.window_center()

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
            highlighted_cell = e
            highlighted_cell.control.bgcolor=ft.colors="red"
            print (highlighted_cell.control.data)

        def action_click(highlighted_cell):
            print (highlighted_cell.control.content.semantics_label)
            ##print (e.control.data["cell_index"])
            print (highlighted_cell.control.data)
            print ("new_value=", new_value.current.value)
            if new_value.current.value in sudoku_numbers:
                highlighted_cell.control.content = ft.Text(new_value.current.value)
                highlighted_cell.control.data["cell_current_value"] = new_value.current.value
                highlighted_cell.control.data["cell_value_source"] = "cell_click"
                highlighted_cell.control.alignment=ft.alignment.center
                highlighted_cell.control.bgcolor=ft.colors="green"
            elif new_value.current.value == '':
                highlighted_cell.control.content = ft.Text(new_value.current.value)
                highlighted_cell.control.alignment=ft.alignment.center
                highlighted_cell.control.bgcolor=ft.colors="blue"
            elif new_value.current.value == 'rn':
                print("rn row_needs", row_of(highlighted_cell.control.data["cell_index"]))
                row_needs(row_of(highlighted_cell.control.data["cell_index"]))

            elif new_value.current.value == 'cn':
                print ("col_needs")    
            elif new_value.current.value == 'bn':
                print ("box needs")    
            else:
                print ("something else", new_value.current.value)    

            e.control.update()

        def row_needs(row):
            print ("row_needs", row)

        cell_index = 0
        for row in range (1,10):
            this_row = []
            for col in range (1,10):
                c = ft.Container(
                    content=ft.Text(""),
                    width=20,
                    height=20,
                    bgcolor="blue",
                    ink=False,
                    data= {"cell_index": cell_index,
                           "cell_row": row,
                           "cell_col": col,
                           "cell_box": box_of(row,col),
                           "cell_current_value": '',
                           "cell_value_source": ''},
                    on_click=cell_click,
                )
                cell_index += 1

                cell_containers.append(c)
                this_row.append(c)

            page.add(ft.Row(this_row))

        page.add(
            ft.TextField(ref=new_value, 
                         label="Action 1-9 set, rn=row_needs, cn=col_needs, bn=box_needs", 
                         autofocus=True, width=200),
            )

    ft.app(target=main)
