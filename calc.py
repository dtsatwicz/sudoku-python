import flet as ft

def main(page: ft.Page):
	page.title = 'Calc App'
	result = ft.Text(value='0')
	width=500

	def clicked_ac(e):
		print ('clicked_ac')
		result.current.controls.clear()
		result.current.controls.append(ft.Text(value='0'))
		page.update()

	def clicked_7(e):
		## if e.control.data["cell_highlighted"]==True:
		prior_value = result.data
		print ('clicked_7',result.value,prior_value)
		result.current.controls.clear()
		result.current.controls.append(ft.Text(value='7'))
		page.update()

	page.add(
		ft.Row(controls=[result],ref=result,data=0),
		ft.Row(
			controls=[
				ft.ElevatedButton(text='AC',on_click=clicked_ac),
				ft.ElevatedButton(text='+/-'),
				ft.ElevatedButton(text='%'),
				ft.ElevatedButton(text='/'),
			]
		),
		ft.Row(
			controls=[
				ft.ElevatedButton(text='7',on_click=clicked_7),
				ft.ElevatedButton(text='8'),
				ft.ElevatedButton(text='9'),
				ft.ElevatedButton(text='*'),
			]
		),
		ft.Row(
			controls=[
				ft.ElevatedButton(text='4'),
				ft.ElevatedButton(text='5'),
				ft.ElevatedButton(text='6'),
				ft.ElevatedButton(text='-'),
			]
		),
		ft.Row(
			controls=[
				ft.ElevatedButton(text='1'),
				ft.ElevatedButton(text='2'),
				ft.ElevatedButton(text='3'),
				ft.ElevatedButton(text='*'),
			]
		),
		ft.Row(
			controls=[
				ft.ElevatedButton(text='0'),
				ft.ElevatedButton(text='.'),
				ft.ElevatedButton(text='='),
				ft.ElevatedButton(text='*'),
			]
		),
	)

ft.app(target=main)
