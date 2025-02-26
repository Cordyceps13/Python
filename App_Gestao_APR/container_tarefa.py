import flet as ft
import main as m

# Classe para mostrar as tarefas introduzidas


class Tarefa(ft.UserControl):
    def __init__(self, task_id: int, task: str, date: str, func1, func2):
        self.task_id = task_id
        self.task = task
        self.date = date
        self.checked = False
        # Criar dois argumentos para chamar as funções de eliminar e editar
        self.func1 = func1
        self.func2 = func2
        super().__init__()

    # Função para marcar as tarefas como concluídas
    def rasurar_texto(self, e):
        self.checked = e.control.value  # Atualiza o estado da checkbox
        text_decoration = ft.TextDecoration.LINE_THROUGH if self.checked else ft.TextDecoration.NONE
        self.task_text.style = ft.TextStyle(decoration=text_decoration)
        self.date_text.style = ft.TextStyle(decoration=text_decoration)
        self.update()

    # Função para construir o container de cada tarefa
    def build(self):

        # Textos da tarefa e data
        self.task_text = ft.Text(
            value=self.task,
            size=10,
            selectable=True,
            text_align=ft.TextAlign.LEFT,
            color="white54",
            max_lines=None,
            overflow=ft.TextOverflow.VISIBLE,
            style=ft.TextStyle(decoration=ft.TextDecoration.NONE),  # Inicialmente sem decoração
        )

        self.date_text = ft.Text(
            value=self.date,
            size=8,
            color="white54",
            max_lines=None,
            overflow=ft.TextOverflow.VISIBLE,
            style=ft.TextStyle(decoration=ft.TextDecoration.NONE),  # Inicialmente sem decoração
        )

        return ft.Container(
            width=m.WINDOW_WIDTH,
            height=50,
            border=ft.border.all(0.6, 'white'),
            border_radius=6,
            padding=5,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Checkbox(
                                value=self.checked,
                                on_change=self.rasurar_texto,
                                scale=0.7,
                            ),
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                width=160,
                                scroll=ft.ScrollMode.HIDDEN,
                                controls=[
                                    self.task_text,
                                    self.date_text,
                                ],
                            ),
                        ]
                    ),
                    # icons de editar e apagar
                    ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            # passar aqui os argumentos para as funções de eliminar e editar
                            self.ApagarEditarTarefa(
                                ft.icons.DELETE_ROUNDED,
                                'red500',
                                self.func1),
                            self.ApagarEditarTarefa(
                                ft.icons.EDIT_ROUNDED,
                                'blue500',
                                self.func2),
                        ]
                    )
                ],
            ),
        )

    # Função para apagar e editar as tarefas
    def ApagarEditarTarefa(self, name, color, func):
        return ft.IconButton(
            icon=name,
            width=30,
            icon_size=15,
            icon_color=color,
            padding=ft.padding.only(bottom=1),
            on_click=lambda e: func(self.task_id, self.task) if name == ft.icons.DELETE_ROUNDED else func(self.task_id)
        )
