import flet as ft
import main as m
import datetime as dt
import calendar

obj = calendar.Calendar()


def abrir_calendario(page: ft.Page):

    def voltar(e):
        page.clean()
        m.main(page)

    ano_atual = int(dt.date.today().strftime('%Y'))
    mes_atual = int(dt.date.today().strftime('%m'))
    dia_atual = int(dt.date.today().strftime('%d'))

    meses = [
        'Janeiro', 
        'Fevereiro', 
        'Março', 
        'Abril', 
        'Maio', 
        'Junho',
        'Julho', 
        'Agosto', 
        'Setembro', 
        'Outubro', 
        'Novembro', 
        'Dezembro',
    ]

    dia_semana = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']

    # Linha de dias da semana
    _row_dia_semana = ft.Row(
        spacing=12,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    for dia in dia_semana:
        _row_dia_semana.controls.append(
            ft.Container(
                width=25,
                height=25,
                border_radius=5,
                alignment=ft.alignment.center,
                content=ft.Text(
                    dia,
                    size=15,
                    color='white',
                )
            )
        )

    # Função para atualizar o calendário
    def atualizar_calendario():
        calendario_container.controls.clear()  # Limpa os controles existentes
        carregar_calendario()  # Recarrega o calendário
        page.update()  # Atualiza a interface

    # Função para navegar para o mês anterior
    def mes_anterior(e):
        nonlocal mes_atual, ano_atual
        if mes_atual == 1:
            mes_atual = 12
            ano_atual -= 1
        else:
            mes_atual -= 1
        atualizar_calendario()

    # Função para navegar para o próximo mês
    def mes_seguinte(e):
        nonlocal mes_atual, ano_atual
        if mes_atual == 12:
            mes_atual = 1
            ano_atual += 1
        else:
            mes_atual += 1
        atualizar_calendario()

    # Função para carregar o calendário
    def carregar_calendario():
        coluna_mes = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=2,
        )
        # Cabeçalho com navegação de meses
        _row_ano = ft.Row(
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK_IOS,
                    icon_size=10,
                    on_click=mes_anterior,
                ),
                ft.Text(
                    f'{meses[mes_atual - 1]} {ano_atual}',
                    size=15,
                ),
                ft.IconButton(
                    icon=ft.icons.ARROW_FORWARD_IOS,
                    icon_size=10,
                    on_click=mes_seguinte,
                ),
            ]
        )
        coluna_mes.controls.append(_row_ano)
        coluna_mes.controls.append(_row_dia_semana)

        # Adiciona os dias do mês
        for dias in obj.monthdayscalendar(ano_atual, mes_atual):
            _row = ft.Row(
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
            )
            coluna_mes.controls.append(_row)
            for dia in dias:
                if dia != 0:
                    __ = ft.Container(
                        width=35,
                        height=35,
                        bgcolor='bluegrey900',
                        border_radius=5,
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            f'{dia}',
                            size=15,
                            color='white70',
                        ),
                    )
                    # Destaca o dia atual
                    if mes_atual == int(dt.date.today().strftime('%m')) and dia == dia_atual and ano_atual == int(dt.date.today().strftime('%Y')):
                        __.bgcolor = 'blue800'
                    _row.controls.append(__)
                else:
                    _row.controls.append(
                        ft.Container(
                            width=35,
                            height=35,
                            border_radius=5,
                        )
                    )
        calendario_container.controls.append(coluna_mes)
        calendario_container.controls.append(
            ft.Container(
                margin=ft.margin.only(bottom=60),
            ),
        )
        
    calendario_container = ft.Column()
    
    # Coluna principal
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        'Calendário',
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
                margin=ft.margin.only(bottom=50),
            ),
            ft.Image(
                src='assets/calendar.svg',
                width=80,
                height=80,
                fit=ft.ImageFit.COVER,
                color='green500',
            ),
            ft.Container(
                margin=ft.margin.only(bottom=30),
            ),
            calendario_container,
        ]
    )

    carregar_calendario()  # Inicializa o calendário

    # Adicionar o conteúdo à página
    page.add(
        ft.Container(
            height=m.WINDOW_HEIGHT - 80,
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
                                content=ft.Column(
                                    controls=[_main_column_],
                                )
                            )
                        ],
                    )
                ]
            )
        ),
    )