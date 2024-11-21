import flet as ft
import datetime as dt
import database as db
import main as m
import container_tarefa as ct

conexao = db.criar_conexao()
utilizador = db.verificar_sessao()


def abrir_lista_tarefas(page: ft.Page):
    
    # Função para voltar à página inicial
    def voltar(e):
        page.clean()
        m.main(page)

    # Função para adicionar/editar tarefas
    def Criar_Tarefa(e):
        tarefa = ft.Ref[ft.TextField]()
        data = dt.datetime.now().strftime('%b %d, %Y %H:%M')
        
        def confirm(e):
            tarefa_texto = tarefa.current.value
            db.InserirTarefa(conexao, tarefa_texto, data, db.sessao_ID)
            Listar_Tarefas()  # Atualizar a lista de tarefas após eliminar
            page.dialog.open = False
            page.update()

        def cancel(e):
            page.dialog.open = False
            page.update()

        page.dialog = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor='bluegrey500',
            title=ft.Text(
                "Criar Tarefa",
                text_align=ft.TextAlign.CENTER,
            ),
            content=ft.TextField(
                bgcolor='bluegrey300',
                multiline=True,
                max_lines=5,
                max_length=100,
                ref=tarefa,
                text_size=13,
                filled=True,
                border_color='transparent',
                hint_text='Introduza uma tarefa...',
                hint_style=ft.TextStyle(
                    color='black', 
                    size=11, 
                    weight=ft.FontWeight.NORMAL
                ),
            ),
            actions=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content = ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.TextButton(
                                "Adicionar", 
                                on_click=confirm,
                                style=ft.ButtonStyle(
                                    color={ft.MaterialState.DEFAULT: 'white'}, 
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                    bgcolor= m.BTN_COLOR,
                                ),
                            ),
                            ft.TextButton(
                                "Cancelar", 
                                on_click=cancel,
                                style=ft.ButtonStyle(
                                    color={ft.MaterialState.DEFAULT: 'white'}, 
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                    bgcolor= m.BTN_COLOR,
                                ),
                            ),
                        ]
                    ),
                ),
            ],
        )
        page.dialog.open = True
        page.update()

        Listar_Tarefas()  # Atualiza a lista de tarefas após a salvar

    # Função para atualizar  a lista de tarefas completamente
    def Listar_Tarefas():
        # Armazenar o respetivo container das tarefas
        lista_tarefas = _main_column_.controls[2]
        # Limpa todas as tarefas do container para evitar duplicações
        lista_tarefas.controls.clear()

        # Carrega todas as tarefas da base de dados e adiciona à coluna principal
        for tarefa in db.VerTarefas(conexao, db.sessao_ID)[::-1]:
            lista_tarefas.controls.append(
                ct.Tarefa(
                    tarefa[0],  # ID da tarefa
                    tarefa[1],  # Nome da tarefa
                    tarefa[2],  # Data da tarefa
                    Eliminar_Tarefa,
                    Editar_Tarefa,
                )
            )
        lista_tarefas.update()  # Atualiza a lista de tarefas
        page.update()  # Atualiza a página (necessário sempre que existam alterações visíveis)

    # função para eliminar tarefas
    def Eliminar_Tarefa(tarefa_id, nome_tarefa):
        def confirm_delete(e):
            db.EliminarTarefa(conexao, (tarefa_id,))
            Listar_Tarefas()  # Atualizar a lista de tarefas após eliminar
            page.dialog.open = False
            page.update()

        def cancel_delete(e):
            page.dialog.open = False
            page.update()

        page.dialog = ft.AlertDialog(
            bgcolor= m.DIALOG_BG,
            shape=ft.RoundedRectangleBorder(radius=10),
            title=ft.Text("Confirmar Eliminação"),
            content=ft.Text(
                f"Você realmente deseja eliminar a tarefa '{nome_tarefa}'?",
                width=3    
            ),
                
            actions=[
                ft.TextButton(
                    "Sim", 
                    on_click=confirm_delete,
                    style=ft.ButtonStyle(
                        color='white',
                        shape=ft.RoundedRectangleBorder(radius=6),
                        bgcolor= m.BTN_COLOR,
                    ),
                ),
                ft.TextButton(
                    "Não", 
                    on_click=cancel_delete,
                    style=ft.ButtonStyle(
                        color='white',
                        shape=ft.RoundedRectangleBorder(radius=6),
                        bgcolor= m.BTN_COLOR,
                    ),
                    
                ),
            ],
        )
        page.dialog.open = True
        page.update()

    # função para editar tarefas
    def Editar_Tarefa(tarefa_id):
        tarefa = ft.Ref[ft.TextField]()
        data = dt.datetime.now().strftime('%b %d, %Y %H:%M')

        def confirm_edit(e):
            tarefa_txt = tarefa.current.value
            db.EditarTarefa(conexao, tarefa_txt, data, tarefa_id)
            Listar_Tarefas()  # Atualizar a lista de tarefas após eliminar
            page.dialog.open = False
            page.update()

        def cancel_edit(e):
            page.dialog.open = False
            page.update()

        page.dialog = ft.AlertDialog(
            bgcolor= m.DIALOG_BG,
            shape=ft.RoundedRectangleBorder(radius=10),
            title=ft.Text(
                "Editar Tarefa",
                text_align=ft.TextAlign.CENTER,
                size=m.TITLE_SIZE,
            ),
            content=ft.TextField(
                bgcolor='bluegrey300',
                multiline=True,
                max_lines=5,
                max_length=100,
                ref=tarefa,
                text_size=13,
                filled=True,
                border_color='transparent',
                hint_text='Introduza uma tarefa...',
                hint_style=ft.TextStyle(
                    color='black', 
                    size=11, 
                    weight=ft.FontWeight.NORMAL
                ),
            ),
            actions=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.TextButton(
                            "Confirmar", 
                            on_click=confirm_edit,
                            style=ft.ButtonStyle(
                                color='white',
                                shape=ft.RoundedRectangleBorder(radius=6),
                                bgcolor= m.BTN_COLOR,
                            ),
                        ),
                        ft.TextButton(
                            "Cancelar", 
                            on_click=cancel_edit,
                            style=ft.ButtonStyle(
                                color='white',
                                shape=ft.RoundedRectangleBorder(radius=6),
                                bgcolor= m.BTN_COLOR,
                            ),
                        ),
                    ],
                ),
            ]
        )
        page.dialog.open = True
        page.update()


    # Coluna principal para listar tarefas
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        'Lista de tarefas', 
                        size=m.TEXT_SIZE, 
                        weight='bold'
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK_IOS_NEW,
                        icon_size = 15,
                        on_click=voltar,
                    ),
                ]
            ),
            ft.Divider(
                height=2, 
                color='white24'
            ),
            ft.ListView(
                height=m.WINDOW_HEIGHT -180,
                width=m.WINDOW_WIDTH - 100,
                spacing=10,
                controls=[],
                expand=True,
            ),
            ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(
                            ft.icons.ADD_CIRCLE_ROUNDED,
                            icon_size=20,
                            icon_color='white',
                            on_click=Criar_Tarefa,
                        ),
                    ]
                )
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
                        padding=ft.padding.only(top=20, left=25, right=25, bottom=20),
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

    # Carregar as tarefas existentes inicialmente
    Listar_Tarefas()

