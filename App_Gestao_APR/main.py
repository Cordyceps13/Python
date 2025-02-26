import flet as ft
import to_do as td
import login as lg
import signup as su
import database as db
import calculator as cal
import calendario as ca
import time
import sys

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700
TITLE_SIZE = 20
TEXT_SIZE = 16
DIALOG_BG = 'bluegrey500'
BTN_COLOR = 'bluegrey700'


def main(page: ft.Page):
    page.title = 'Cordyceps®'
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.resizable = False
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    # Função para fechar a aplicação
    def fechar_app(e):
        page.window.close()
        sys.exit()

    # Função para abrir o módulo to_do.py
    def abrir_to_do(e):
        page.clean()
        td.abrir_lista_tarefas(page)

    # Função para abrir o módulo login.py
    def abrir_login(e):
        page.clean()
        lg.abrir_login(page)

    # Função para abrir o módulo signup.py
    def abrir_signup(e):
        page.clean()
        su.abrir_signup(page)

    def abrir_calculadora(e):
        page.clean()
        cal.abrir_calculadora(page)
    
    def abrir_calendario(e):
        page.clean()
        ca.abrir_calendario(page)

    # Função para fechar o alertDialog
    def fechar_alert(page):
        page.dialog.open = False
        page.update()

    # Função para efetuar o logout
    def logout(e):
        db.destruir_sessao()

        if db.verificar_sessao():
            page.dialog = ft.AlertDialog(
                bgcolor=DIALOG_BG,
                title=ft.Text(
                    "Erro!",
                    text_align="center",
                    size=TITLE_SIZE,
                ),
                content=ft.Text(
                    "Não foi possível fazer logout.",
                    text_align="center",
                    size=TEXT_SIZE,
                ),
                actions=[
                    ft.TextButton(
                        "OK",
                        on_click=lambda e: fechar_alert(page),
                        style=ft.ButtonStyle(
                            color='white',
                            bgcolor=BTN_COLOR,
                            shape=ft.RoundedRectangleBorder(radius=6),
                        )
                    )
                ]
            )
            page.dialog.open = True
            page.update()
            time.sleep(1.5)
            fechar_alert(page)
            return
        else:
            page.dialog = ft.AlertDialog(
                bgcolor=DIALOG_BG,
                title=ft.Text(
                    "Sessão terminada!",
                    text_align="center",
                    size=TITLE_SIZE,
                ),
                content=ft.Text(
                    "Até à próxima!",
                    text_align="center",
                    size=TEXT_SIZE,
                )
            )
            page.dialog.open = True
            page.update()
            page.clean()
            main(page)
            page.update()
            time.sleep(1.5)
            fechar_alert(page)

    botoes = []  # Controls para adicionar os botões à pagina principal

    # Adicionar botões à pagina principal consoante existência de sessão iniciada ou não
    imagem_fundo = ft.Image(
        src= 'assets/mushroom.png',
        fit=ft.ImageFit.FILL,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
    )
    if db.verificar_sessao():
        # Botão para abrir a aplicação to_do.py
        to_do_button = ft.TextButton(
            text="Lista de Tarefas",
            on_click=abrir_to_do,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor=BTN_COLOR,
            ),
        )

        calculator_btn = ft.TextButton(
            text="Calculadora",
            on_click=abrir_calculadora,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor=BTN_COLOR,
            ),
        )
        
        calendario_btn = ft.TextButton(
            text="Calendário",
            on_click=abrir_calendario,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor=BTN_COLOR,
            ),
        )

        logout_btn = ft.IconButton(
            icon=ft.icons.LOGOUT,
            on_click=logout,
            rotate=3.14159,
            icon_size=20,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )

        botoes.extend([
            ft.Container(
                content=logout_btn,
                alignment=ft.alignment.top_right,
                margin=ft.margin.only(bottom=200),
            ),
            ft.Container(
                content=to_do_button,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=calculator_btn,
                alignment=ft.alignment.center,
                # margin=ft.margin.only(bottom=300),
            ),
            ft.Container(
                content=calendario_btn,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=300),
            )
        ])

    else:
        log_btn = ft.TextButton(
            text="Login",
            on_click=abrir_login,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor=BTN_COLOR,
            ),
        )
        sign_btn = ft.TextButton(
            text="Signup",
            on_click=abrir_signup,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor=BTN_COLOR,
            ),
        )
        botoes.extend([
            ft.Container(
                content=ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color='red',
                    on_click=fechar_app,
                ),
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=20),
            ),
            ft.Image(
               src='assets/alien.svg',
               fit=ft.ImageFit.COVER,
               width=300,
               height=300,
               border_radius=10,
            ),
            ft.Container(
                content=sign_btn,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=30, bottom=10),
            ),
            ft.Container(
                content=log_btn,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=50),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(
                    "Developed by Cordyceps®",
                    size=10,
                    color='white',
                    text_align="center",
                )
            )
        ])

    # Adicionar o conteúdo à página
    page.add(
        ft.Container(
            height=WINDOW_HEIGHT - 80,
            bgcolor='bluegrey900',
            border_radius=20,
            alignment=ft.alignment.center,
            content=ft.Stack(
                controls=[
                    ft.Row(
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
                                    top=20, 
                                    left=25, 
                                    right=25, 
                                    bottom=20
                                ),
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=ft.Stack(
                                    expand = True,
                                    controls=[
                                        # imagem_fundo,
                                        *(
                                            [imagem_fundo] if db.verificar_sessao() else []
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            expand=True,
                                            controls=botoes,
                                        ),
                                    ],
                                )
                            )
                        ],
                    )
                ]
            )
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
