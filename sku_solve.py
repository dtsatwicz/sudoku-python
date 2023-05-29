
import flet as ft

if __name__ == "__main__":

    def main(page: ft.Page):

        page.title="Sudoku"
        page.window_height=500
        page.window_width=300

        result = ft.Text(value='0')
        new_cell_value = ft.Text(value='0')
        text_action_to_take = 'No Action Set'
        action_to_take = ft.Text(value=text_action_to_take)
        next_cell_value = ''
        new_number = ''
        cell_containers=[]

        def sudoku_numbers():  
            return ['1','2','3','4','5','6','7','8','9']
        
        def cells_in_row(row):
            cells = [[],
                     [ 0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [ 9,10,11,12,13,14,15,16,17],
                     [18,19,20,21,22,23,24,25,26],
                     [27,28,29,30,31,32,33,34,35],
                     [36,37,38,39,40,41,42,43,44],
                     [45,46,47,48,49,50,51,52,53],
                     [54,55,56,57,58,59,60,61,62],
                     [63,64,65,66,67,68,69,70,71],
                     [72,73,74,75,76,77,78,79,80],
                     ]
            return cells[row]
                     
        def cells_in_col(col):
            cells = [[],
                     [ 0, 9,18,27,36,45,54,63,72],
                     [ 1,10,19,28,37,46,55,64,73],
                     [ 2,11,20,29,38,47,56,65,74],
                     [ 3,12,21,30,39,48,57,66,75],
                     [ 4,13,22,31,40,49,58,67,76],
                     [ 5,14,23,32,41,50,59,68,77],
                     [ 6,15,24,33,42,51,60,69,78],
                     [ 7,16,25,34,43,52,61,70,79],
                     [ 8,17,26,35,44,53,62,71,80],
                     ]
            return cells[col]
                     
        def cells_in_box(box):
            cells = [[],
                     [ 0, 1, 2, 9,10,11,18,19,20],
                     [ 3, 4, 5,12,13,14,21,22,23],
                     [ 6, 7, 8,15,16,17,24,25,26],
                     [27,28,29,36,37,38,45,46,47],
                     [30,31,32,39,40,41,48,49,50],
                     [33,34,35,42,43,44,51,52,53], 
                     [54,55,56,63,64,65,72,73,74],
                     [57,58,59,66,67,68,75,76,77],
                     [60,61,62,69,70,71,78,79,80],
                     ]
            return cells[box]
                     
        def rows_of_cell_index(cell_index):
            rows = [[],
                    [1,1,1,1,1,1,1,1,1],
                    [2,2,2,2,2,2,2,2,2],
                    [3,3,3,3,3,3,3,3,3],
                    [4,4,4,4,4,4,4,4,4],
                    [5,5,5,5,5,5,5,5,5],
                    [6,6,6,6,6,6,6,6,6],
                    [7,7,7,7,7,7,7,7,7],
                    [8,8,8,8,8,8,8,8,8],
                    [9,9,9,9,9,9,9,9,9],
                   ]
            return rows[cell_index]

        def cols_of_cell_index(cell_index):
            cols = [[],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                   ]
            return cols[cell_index]

        def boxs_of_cell_index(cell_index):
            boxs = [[],
                    [1,1,1,2,2,2,3,3,3],
                    [1,1,1,2,2,2,3,3,3],
                    [1,1,1,2,2,2,3,3,3],
                    [4,4,4,5,5,5,6,6,6],
                    [4,4,4,5,5,5,6,6,6],
                    [4,4,4,5,5,5,6,6,6],
                    [7,7,7,8,8,8,9,9,9],
                    [7,7,7,8,8,8,9,9,9],
                    [7,7,7,8,8,8,9,9,9],
                   ]
            return boxs[cell_index]

        def col_of_cell_index(cell_index):
            global cell_containers
            col = cell_containers[cell_index].data["cell_col"]
            return col

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
            global text_action_to_take

            print ('cell_clicked', text_action_to_take)

            if text_action_to_take == 'No Action Set':
                print ('No Action Set')
            
            elif text_action_to_take == 'Set Cell To':
                e.control.content = ft.Text(next_cell_value)
                e.control.bfcolor="red"
                page.update()
            
            elif text_action_to_take == 'Run Row Can Be':
                row_can_be(e.control.data)
                page.update()
            
            elif text_action_to_take == 'Run Col Can Be':
                col_can_be(e)
                page.update()
            
            elif text_action_to_take == 'Run Box Can Be':
                box_can_be(e)
                page.update()
            
            elif text_action_to_take == 'Run All Can Be':
                all_can_be(e)
                page.update()
            
            else:
                print (text_action_to_take, ' is not implimented', )


        def number_clicked(e):
            global next_cell_value
            global text_action_to_take
            global new_number

            print ('number_clicked', e.control.data)

            text_action_to_take = "Set Cell To"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()

            new_number = e.control.data["sudoku_number"]

            new_cell_value.current.controls.clear()
            new_cell_value.current.controls.append(ft.Text(new_number))
            next_cell_value = new_number
            page.update()

        def click_row_can_be(e):
            global text_action_to_take
            print ('click_row_can_be')
            text_action_to_take = "Run Row Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_col_can_be(e):
            global text_action_to_take
            print ('click_col_can_be')
            text_action_to_take = "Run Col Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_box_can_be(e):
            global text_action_to_take
            print ('click_box_can_be')
            text_action_to_take = "Run Box Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_all_can_be(e):
            global text_action_to_take
            print ('click_all_can_be')
            text_action_to_take = "Run All Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def values_in_cells(cells):
            global cell_containers
            values = []
            for cell in cells:
                cell_current_value = cell_containers[cell].data["cell_current_value"]
                if cell_current_value != "__":
                    values.append(cell_current_value)
            return values

        def row_can_be(data):
            global cell_containers

            row = data["cell_row"]
            print (' 1 row_can_be', row)

            row_needs = sudoku_numbers()
            row_cells = cells_in_row(row)
            for row_cell in row_cells:
                cell_current_value = cell_containers[row_cell].data["cell_current_value"]
                if cell_current_value != "__":
                    row_needs.remove (cell_current_value)
            print (' 2 row_can_be', row, 'row_needs ', row_needs)
             
            for needs in row_needs:
                print ('3a row_can_be row, needs ==>', row, needs)

                can_be_count = 0
                can_be_cell = -1
                can_be_col = -1
                cannot_reason = ''

                for col_cell in cells_in_row(row):
                    if can_be_count <= 1:
                        cell_current_value = cell_containers[col_cell].data["cell_current_value"]
                        col = cell_containers[col_cell].data["cell_col"]
            
                        print ('3b row_can_be row, col ', row, col, needs, can_be_count,  cell_current_value)

                        if cell_current_value == "__":
                            print ('3c row_can_be row, col ', 
                                   row, col, needs, can_be_count,  cell_current_value)

                            col_cells = cells_in_col(col)
                            col_values = values_in_cells(col_cells)
                            cannot_reason = ''
                            if needs in col_values:
                                can_be = False
                                cannot_reason = 'col cannot put value ' + needs + ' in col ' \
                                                  + str(col)
                                print ('5a row_can_be', row, col, needs, can_be_count, cannot_reason)
                            else:
                                box =  box_of(row,col)
                                box_cells = cells_in_box(box)
                                box_values = values_in_cells(box_cells)

                                if needs in box_values:
                                    can_be = False
                                    cannot_reason = 'box cannot put value ' + needs + ' in box ' \
                                                      + str(box)
                                    print ('5b row_can_be', row, col, needs, can_be_count, cannot_reason)
                                else:
                                    ## needs can go in this col_cell
                                    can_be_count += 1
                                    can_be_cell = col_cell
                                    can_be_col = col
                                    print (' 4 row_can_be row, col needs ==> cellCanBe', 
                                           row, col, needs, ' of row_needs', row_needs, col_cell)

                if can_be_count == 1:
                    print ('6a row_can_be ==>', row, col, needs, can_be_count)
                    print ()
                else:
                    cannot_reason = 'cannot put value ' + needs + ' in col ' \
                    + str(col) + ' box ' + ' can_be_count= ' + str(can_be_count)
                    print ('6b row_can_be ', row, col, needs, cannot_reason)

                print (' 9 end of needs loop ', row, can_be_col, needs, can_be_count, 
                                               can_be_cell, cannot_reason)
                print ()
            pass

        def col_can_be(data):
            print ('col_can_be')

        def box_can_be(data):
            print ('box_can_be')

        def all_can_be(data):
            print ('all_can_be')

        def click_init(e):
            global next_cell_value
            global cell_containers
            global test_new_value

            ##if next_cell_value == "1":
            if False:
                init_values = '81.4...5.' + '......9..' + '92.7...18' \
                            + '5..9.....' + '.92...57.' + '.....4..6' \
                            + '26...8.45' + '..7......' + '.8...5.63'
            else:
                init_values = '...65....' + '.96..14..' + '...9..3.1' \
                            + '..5..7.9.' + '.1......6' + '2..1...3.' \
                            + '5..71.6..' + '.....45..' + '.8.2.....'

            print ("click_init" )

            for cell_index in range (81):

                text_new_value = init_values[cell_index]
                if text_new_value == '.': text_new_value = '__'

                cell_containers[cell_index].content = ft.Text(text_new_value)
                cell_containers[cell_index].bgcolor="green"
                cell_containers[cell_index].data["cell_current_value"] = text_new_value

                page.update()

        def sudoku_grid():
            global cell_containers
            global cell_index

            cell_containers=[]
            cell_index = 0
            for row in range (1,10):
                this_row = []
                for col in range (1,10):
                    box = box_of(row,col)
                    c = ft.Container(
						content=ft.Text("__"),
						width=20,
						height=20,
						bgcolor="blue",
						ink=False,
						data= {"cell_index": cell_index,
								"cell_row": row,
								"cell_col": col,
								"cell_box": box,
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

            page.add(ft.Row(controls=[action_to_take],ref=action_to_take,data=ft.Text('No Action Set')))
            page.add(ft.Row(controls=[new_cell_value],ref=new_cell_value,data=ft.Text('__')))

            set_numbers = []        

            for number in sudoku_numbers() + ['__']:
                c = ft.Container(
    				    content=ft.Text(number),
    			    	width=18,
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

            page.add(
	        	ft.Row(
	        		controls=[
	        			ft.ElevatedButton(text='Row',on_click=click_row_can_be),
	        			ft.ElevatedButton(text='Col',on_click=click_col_can_be),
	        			ft.ElevatedButton(text='Box',on_click=click_box_can_be),
	        			ft.ElevatedButton(text='All3',on_click=click_all_can_be),
	        			ft.ElevatedButton(text='Init',on_click=click_init),
	            		]
	                ),
                )    

            page.add(
	        	ft.Row(
	        		controls=[
	        			ft.ElevatedButton(text='Init',on_click=click_init),
	            		]
	                ),
                )    


        sudoku_grid()

        click_init(1)
        click_row_can_be(3)

    ft.app(target=main)