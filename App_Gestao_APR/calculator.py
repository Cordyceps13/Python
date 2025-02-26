import flet as ft
import main as m
import math as mt

NUM_COLOR = 'bluegrey400'


def abrir_calculadora(page: ft.Page):

    def voltar(e):
        page.clean()
        m.main(page)

    def btn_click(e):
        data = e.control.data

        if data in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '+', '-', 'x', '÷', '(', ')', 'π', '√', '²', '³']:
            caixa_input.value = str(caixa_input.value) + str(data)
            page.update()
        
        if data == '=':
            try:
                expression = (caixa_input.value
                            .replace('x', '*')
                            .replace('÷', '/')
                            .replace('²', '**2')
                            .replace('³', '**3')
                            .replace('π', str(mt.pi))
                            .replace('√', 'mt.sqrt(') + ')' * caixa_input.value.count('√') # Adiciona ')' após a expressão
                            )
                
                resultado = eval(expression)
                
                if resultado == int(resultado):
                    resultado = int(resultado)
                caixa_input.value = str(resultado)
            except Exception as ex:
                caixa_input.value = 'Erro de Sintaxe' 
            page.update()
            
        if data == 'C':
            caixa_input.value = ''
            page.update()
        
        if data == '⌫':
            caixa_input.value = str(caixa_input.value)[:-1] # Remove o último caractere que foi inserido, funciona como POP numa lista
            page.update()

        
    caixa_input = ft.TextField(
        read_only=True,
        border_color='grey',
        text_align=ft.TextAlign.RIGHT,
    )

    # COLUNA PRINCIPAL DA PAGINA
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        'Calculadora',
                        size=m.TEXT_SIZE,
                        weight='bold'
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK_IOS_NEW,
                        icon_size=15,
                        on_click=voltar,
                    ),
                ]
            ),
            ft.Divider(
                height=2,
                color='white24'
            ),
            ft.Container(
                margin=ft.margin.only(bottom=30),
            ),
            ft.Image(
                src='assets/calc.svg',
                width=80,
                height=80,
                fit=ft.ImageFit.COVER,
                # border_radius=50,
                color='green500',
            ),
            ft.ListView(
                expand=True,
            ),
            caixa_input,
            ft.Container(
                margin=ft.margin.only(bottom=10)
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='π',
                        data='π',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                            color='white800',
                        )
                    ),
                    ft.ElevatedButton(
                        text='√',
                        data='√',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                            color='white800',
                        )
                    ),
                    ft.ElevatedButton(
                        text='x²',
                        data='²',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                            color='white800',
                        )
                    ),
                    ft.ElevatedButton(
                        text='x³',
                        data='³',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            padding=10,
                            color='white800',
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='C',
                        data='C',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor='red',
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='(',
                        data='(',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text=')',
                        data=')',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='÷',
                        data='÷',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    )
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='7',
                        data='7',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='8',
                        data='8',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='9',
                        data='9',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='x',
                        data='x',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    )
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='4',
                        data='4',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='5',
                        data='5',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='6',
                        data='6',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='-',
                        data='-',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    )
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='1',
                        data='1',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='2',
                        data='2',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='3',
                        data='3',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='+',
                        data='+',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    )
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text='⌫',
                        data='⌫',
                        # text_size=20,
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='red',
                            padding=10,  # Ajusta o espaçamento do botão
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='0',
                        data='0',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=NUM_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='.',
                        data='.',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=m.BTN_COLOR,
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    ),
                    ft.ElevatedButton(
                        text='=',
                        data='=',
                        on_click=btn_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor='green900',
                            color='white800',
                            padding=10,
                            text_style=ft.TextStyle(size=15), 
                        )
                    )
                ]
            ),
            ft.Container(
                margin=ft.margin.only(bottom=20),
            )
        ]
    )
    
    # Interface completa
    page.add(
        ft.Container(
            height=m.WINDOW_HEIGHT - 80,
            bgcolor='bluegrey900',
            border_radius=20,
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=600,
                        width=320,
                        bgcolor=ft.colors.with_opacity(0.6, '#161716'),
                        border=ft.border.all(0.5, 'white'),
                        border_radius=30,
                        padding=ft.padding.only(
                            top=20, left=25, right=25, bottom=20),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[_main_column_]
                        )
                    )
                ],
            )
        ),
    )