import flet as ft
import main as m
import database as db
import time
import to_do as td


conexao = db.criar_conexao()


def abrir_login(page: ft.Page):
    
    def voltar(e):
        page.clean()
        m.main(page)
        
    def fechar_alert(page):
        page.dialog.open = False
        page.update()
    
    def efetuar_login(e):
        username = username_field.value
        password = password_field.value
        
        db.Login(conexao, username, password)
        if db.verificar_sessao():
            page.dialog = ft.AlertDialog(
                bgcolor=m.DIALOG_BG,
                title = ft.Text(
                    "Bem vind@..",
                    text_align= "center",
                    size=m.TITLE_SIZE,
                ),
                content = ft.Text(
                    "" + str(db.sessao) + "!",
                    text_align = "center",
                    size = m.TEXT_SIZE,
                )
            )
            page.dialog.open = True
            voltar(e)
            page.update()
            time.sleep(1.5)
            fechar_alert(page)
            
        else:
            page.dialog = ft.AlertDialog(
                alignment=ft.alignment.center,
                bgcolor=m.DIALOG_BG,
                title=ft.Text(
                    "Login inválido!",
                    text_align="center",
                ),
                content=ft.Text(
                    "Username ou senha incorretos",
                    text_align="center",
                ),
                actions_alignment=ft.MainAxisAlignment.CENTER,
                actions=[
                    ft.TextButton(
                        "Tentar novamente",
                        on_click=lambda e: fechar_alert(page),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color=ft.colors.WHITE,
                            bgcolor=m.BTN_COLOR,
                        )
                    ),
                ]
            )
            page.dialog.open = True
            page.update()
                
    username_field = ft.TextField(
        hint_text='Nome de utilizador...',
        bgcolor='bluegrey300',
    )
    
    password_field = ft.TextField(
        hint_text='Password...',
        bgcolor='bluegrey300',
        password=True,
    )
    
    
    #COLUNA PRINCIPAL DA PAGINA DE LOGIN
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        'Login', 
                        size=m.TITLE_SIZE, 
                        weight='bold'
                    ),
                ]
            ),
            ft.Divider(
                height=2, 
                color='white24',
            ),
            ft.Container(
                margin=ft.margin.only(bottom=20),
            ),
            ft.Image(
                src='assets/alien.svg',
                width=80,
                height=80,
                fit=ft.ImageFit.COVER,
                border_radius=50,
                color='green500',
            ),
            ft.Container(
                margin=ft.margin.only(bottom=50),
            ),
            username_field,
            ft.Container(
                margin=ft.margin.only(bottom=10),
            ),
            password_field,
            ft.Container(
                margin=ft.margin.only(bottom=50),
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        text='Login',
                        on_click=efetuar_login,
                        style=ft.ButtonStyle(
                            color='white',
                            shape=ft.RoundedRectangleBorder(radius=6),
                            bgcolor= m.BTN_COLOR,
                        )
                    ),
                ]
            ),
            ft.Container(
                margin=ft.margin.only(bottom=15),
            ),
            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK_IOS_NEW,
                        icon_size = 15,
                        on_click=voltar,
                    )  
                ]
            ),
        ]
    )
    
    #CONTEUDO DA PAGINA DE LOGIN
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
                        padding=ft.padding.only(top=20, left=25, right=25, bottom=20),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[_main_column_],
                        )
                    )
                ]
            )
        )
    )