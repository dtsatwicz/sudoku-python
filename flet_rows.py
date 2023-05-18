import flet as ft

if __name__ == "__main__":

    cell_containers = []
    cell_row = []
    cell_col = []
    cell_box = []
    cell_value = []
    sudoku_numbers = ['1','2','3','4','5','6','7','8','9']

    def main(page: ft.Page):
        page.title="Sudoku"
        page.window_height=600
        page.window_width=500
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
            print (e.control.content.semantics_label)
            print (e.control.data["cell_index"])
            print ("new_value=", new_value.current.value)
            if new_value.current.value in sudoku_numbers:
                e.control.content = ft.Text(new_value.current.value)
                e.control.alignment=ft.alignment.center
                e.control.bgcolor=ft.colors="green"
            elif new_value.current.value == 'rn':
                print("rn row_needs", row_of(e.control.data["cell_index"]))
                row_needs(row_of(e.control.data["cell_index"]))

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
                    ##content=ft.Text("r"+str(row)+"c"+str(col), semantics_label=str(row)+ " " + str(col) ),
                    content=ft.Text(""),
                    width=20,
                    height=20,
                    bgcolor="blue",
                    ink=False,
                    data= {"cell_index": cell_index,
                           "cell_row": row,
                           "cell_col": col,
                           "cell_box": box_of(row,col),
                           "cell_initial_value": '',
                           "cell_current_value": '',
                           "cell_value_source": ''},
                    on_click=cell_click,
                )
                cell_index += 1

                ##cell_row.append(row)
                ##cell_col.append(col)
                ##cell_box.append(box_of(row,col))
                ##cell_value.append('')
                cell_containers.append(c)
                this_row.append(c)

            page.add(ft.Row(this_row))

        page.add(
            ft.TextField(ref=new_value, 
                         label="Action 1-9 set, rn=row_needs, cn=col_needs, bn=box_needs", 
                         autofocus=True, width=500),
            )

    ft.app(target=main)