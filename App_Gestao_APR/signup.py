import flet as ft
import main as m
import database as db
import login as lg
import time

conexao = db.criar_conexao()


def abrir_signup(page: ft.Page):
    
    def voltar(e):
        page.clean()
        m.main(page)
        
    def fechar_alert(page):
        page.dialog.open = False
        page.update()
    
    def ir_para_login():
        fechar_alert(page)
        time.sleep(0.2)
        page.clean()
        lg.abrir_login(page)
        page.update()
    
    def efetuar_registo(e):
        username = username_field.value.strip()
        password = password_field.value.strip()
        
        if not username or not password:
            page.dialog = ft.AlertDialog(
                bgcolor=m.DIALOG_BG,
                title=ft.Text(
                    "Erro!",
                    text_align="center",
                    size=m.TITLE_SIZE,
                ),
                content=ft.Text(
                    "Por favor, preencha todos os campos.",
                    text_align="center",
                    size=m.TEXT_SIZE,
                ),
            )
            page.dialog.open = True
            page.update()
            time.sleep(1.5)
            fechar_alert(page)
            return
        
        success = db.signup(conexao, username, password)
        if success:
            page.dialog = ft.AlertDialog(
                bgcolor=m.DIALOG_BG,
                title=ft.Text(
                    "Registo efetuado com sucesso!",
                    text_align="center",
                    size=m.TITLE_SIZE,
                ),
                content=ft.Text(
                    "A redirecionar para a página de login...",
                    text_align="center",
                    size=m.TEXT_SIZE,
                ),
            )
            page.dialog.open = True
            page.update()
            time.sleep(1.5)
            ir_para_login()
        else:
            page.dialog = ft.AlertDialog(
                bgcolor=m.DIALOG_BG,
                title=ft.Text(
                    "ERRO!",
                    text_align="center",
                    size=m.TITLE_SIZE,
                ),
                content=ft.Text(
                    "Não foi possível efetuar o registo.",
                    text_align="center",
                    size=m.TEXT_SIZE,
                ),
            )
            page.dialog.open = True
            page.update()
            time.sleep(1.5)
            fechar_alert(page)
    
    
    username_field = ft.TextField(
        hint_text='Nome de utilizador...',
        bgcolor='bluegrey300',
    )
    
    password_field = ft.TextField(
        hint_text='Password...',
        bgcolor='bluegrey300',
        password=True,
    )
    
    #COLUNA PRINCIPAL DA PAGINA DE SIGNUP
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        'Signup', 
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
                        text='Signup',
                        on_click=efetuar_registo,
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
