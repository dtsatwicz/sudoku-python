
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
            #print ('cell_clicked', e.control.data)
            #print ('cell_clicked', next_cell_value, new_number)
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

        def row_can_be(data):
            global cells_in_row
            global cells_in_col
            global cells_in_box
            global cell_containers

            print ('row_can_be')
            print ('row_can_be', 'cell_row=', data["cell_row"], 'cell_col=', data["cell_col"], 
                   'cell_box=', data["cell_box"], data["cell_index"])
            print ('cells_in_row', cells_in_row[data["cell_row"]])

            needed=[]
            not_needed=[]
            print ('row_can_be', sudoku_numbers())
            
            needed= sudoku_numbers()
            print ('row_can_be needed=', needed)

            for index in cells_in_row[data["cell_row"]]:
                cell_current_value = cell_containers[index].data["cell_current_value"]
                print ('index=', index, 
                       cell_current_value,
                       'cell_current_value=',cell_containers[index].data["cell_current_value"],
                       )
                if cell_current_value != "__":
                    not_needed.append(cell_current_value)
                    needed.remove ( cell_current_value)

            print ('row_can_be     needed=',     needed)
            print ('row_can_be not_needed=', not_needed)

            cell_indexes = cells_in_row[data["cell_row"]]
            for cell_index in cell_indexes:
                cell_current_value = cell_containers[cell_index].data["cell_current_value"]
                
                if cell_current_value == "__":
                    for need in needed:
                        can_be_count = 0
                        cells = cells_in_col[data["cell_col"]]
                        for cell in cells:
                            already_has = cell_containers[cell].data["cell_current_value"] 
                            if already_has != need and already_has != "__": 
                                can_be_count += 1
                        cells = cells_in_box[data["cell_box"]]
                        for cell in cells:
                            already_has = cell_containers[cell].data["cell_current_value"] 
                            if already_has != need and already_has != "__": 
                                can_be_count += 1
                    
                        if can_be_count == 1:
                            print ('row_can_be found', index, need, cell_index ) 

            
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

                ##print ('click_init', cell_index, cell_containers[cell_index].content)
                cell_containers[cell_index].content = ft.Text(text_new_value)
                cell_containers[cell_index].bgcolor="green"
                cell_containers[cell_index].data["cell_current_value"] = text_new_value
                ##cell_containers[cell_index].data[
				##				"cell_current_value": '',
                ##                "cell_bgcolor": "blue",
                ##                "cell_highlighted": False,
				##				"cell_value_source": ''],
                page.update()

        def sudoku_grid():
            global cell_containers
            global cell_index

            global cells_in_row
            global cells_in_col
            global cells_in_box

            cells_in_row = [[],[],[],[],[],[],[],[],[],[]]
            cells_in_col = [[],[],[],[],[],[],[],[],[],[]]
            cells_in_box = [[],[],[],[],[],[],[],[],[],[]]

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
        "cells_in_row"
        "cells_in_col"
        "cells_in_box"
								"cell_value_source": ''},
						on_click=cell_clicked,
						)

                    cells_in_row[row].append(cell_index)    
                    cells_in_col[col].append(cell_index)    
                    cells_in_box[box].append(cell_index)    
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

    ft.app(target=main)