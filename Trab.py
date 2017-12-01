from gi.repository import Gtk, Gdk
import os
import webbrowser
import socket
confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
new = 2 # open in a new tab, if possible


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Janela")

        # inicializando
        self.set_border_width(10)
        self.set_default_size(500,300)

        # header
        header = Gtk.HeaderBar(title="Protótipo")
        header.set_subtitle("Ajuda no pc!")
        header.props.show_close_button = True
        self.set_titlebar(header)

        # adiciona scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        #Flowbox
        botoes = Gtk.FlowBox()
        botoes.set_valign(Gtk.Align.START)
        botoes.set_max_children_per_line(5)
        botoes.set_selection_mode(Gtk.SelectionMode.NONE)
        self.create_flowbox(botoes)
        scrolled.add(botoes)
        self.add(scrolled)
        self.show_all()

        print(self.check_host() and "Conexão Ativa" or "Conexão Inativa")

    def check_host(self):
        global confiaveis
        for host in confiaveis:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b = a.connect_ex((host, 80))
                if b == 0:  # ok, conectado
                    return True
            except:
                print("off")
                pass
            a.close()
        return False

    def create_button(self, str_name):
        button = Gtk.Button(label=str_name)
        button.set_property("height-request", 100)
        button.set_property("width-request", 500)
        button.tam = 0
        if str_name == 'PLUS':
            button.connect('clicked', self.cliked_plus_or_minus)
        elif str_name == 'Dimunui Letra -':
            button.connect('clicked', self.cliked_plus_or_minus)
        else:
            button.connect('clicked', self.you_clicked)
        return button

    def create_flowbox(self, flowbox):
        self.google = self.create_button('PESQUISAR NA INTERNET')
        flowbox.add(self.google)

        self.youtube = self.create_button('YOUTUBE - VIDEOS')
        flowbox.add(self.youtube)

        self.facebook = self.create_button('FACEBOOK')
        flowbox.add(self.facebook)

        self.netflix = self.create_button('NETFLIX')
        flowbox.add(self.netflix)

        self.gmail = self.create_button('E-MAIL')
        flowbox.add(self.gmail)

        self.gedit = self.create_button('Bloco de Notas')
        flowbox.add(self.gedit)

        self.calc = self.create_button('CALCULADORA')
        flowbox.add(self.calc)

        self.office = self.create_button('Libre Office')
        flowbox.add(self.office)

        self.plus = self.create_button('PLUS')
        flowbox.add(self.plus)
        self.plus_label = self.plus.get_child()
        self.plus_label.set_markup('<big><big>Aumenta Letra +</big></big>')


        self.minus = self.create_button('Dimunui Letra -')
        flowbox.add(self.minus)
        self.minus_label = self.minus.get_child()
        self.minus_label.set_markup('<small>A -</small>')

    def you_clicked(self, widget):
        print('entra cliked '*2)
        print(widget.get_properties('label'))
        label = widget.get_properties('label')

        # page1
        google = Gtk.Label()
        google.set_label('PESQUISAR NA INTERNET')
        youtube = Gtk.Label()
        youtube.set_label('YOUTUBE - VIDEOS')
        face = Gtk.Label()
        face.set_label('FACEBOOK')
        netflix = Gtk.Label()
        netflix.set_label('NETFLIX')
        gmail = Gtk.Label()
        gmail.set_label('E-MAIL')
        gedit = Gtk.Label()
        gedit.set_label('Bloco de Notas')
        calc = Gtk.Label()
        calc.set_label('CALCULADORA')
        office = Gtk.Label()
        office.set_label('Libre Office')

        # if button pesquisar cliked
        if label == google.get_properties('label'):
            url = "https://www.google.com.br"
            if self.check_host():
                webbrowser.open(url, new=new)
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "Calma, Está sem Internet. Não é nada demais.")
                dialog.format_secondary_text(
                    "Verifique os cabos e chame seu neto.")
                dialog.run()
                print("ERROR dialog closed")
                dialog.destroy()
                print("sem internet")
            print(self.google.get_properties('label'))

        # if button youtube cliked
        if label == youtube.get_properties('label'):
            url = "http://youtube.com.br"
            if self.check_host():
                webbrowser.open(url, new=new)
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "Calma, Está sem Internet. Não é nada demais.")
                dialog.format_secondary_text(
                    "Verifique os cabos e chame seu neto.")
                dialog.run()
                print("ERROR dialog closed")
                dialog.destroy()
                print("sem internet")
            print('1 --- google  deu certo')
        # if button facebook cliked
        if label == face.get_properties('label'):
            url = "https://www.facebook.com/"
            if self.check_host():
                webbrowser.open(url, new=new)
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "Calma, Está sem Internet. Não é nada demais.")
                dialog.format_secondary_text(
                    "Verifique os cabos e chame seu neto.")
                dialog.run()
                print("ERROR dialog closed")
                dialog.destroy()
                print("sem internet")
            print('2 --- facebook  deu certo')
        # if button netflix cliked
        if label == netflix.get_properties('label'):
            url = "http://netflix.com.br"
            if self.check_host():
                webbrowser.open(url, new=new)
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "Calma, Está sem Internet. Não é nada demais.")
                dialog.format_secondary_text(
                    "Verifique os cabos e chame seu neto.")
                dialog.run()
                print("ERROR dialog closed")
                dialog.destroy()
                print("sem internet")
            print('1 --- netflix  deu certo')
        # if button Gmail cliked
        if label == gmail.get_properties('label'):
            url = "http://gmail.com.br"
            if self.check_host():
                webbrowser.open(url, new=new)
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "Calma, Está sem Internet. Não é nada demais.")
                dialog.format_secondary_text(
                    "Verifique os cabos e chame seu neto.")
                dialog.run()
                print("ERROR dialog closed")
                dialog.destroy()
                print("sem internet")
            print('1 --- gmail  deu certo')
        # if button gedit cliked
        if label == gedit.get_properties('label'):
            os.system('/usr/bin/gedit')
            print('3 --- gedit')
        # if button calc cliked
        if label == calc.get_properties('label'):
            os.system('/usr/bin/gnome-calculator')
            print('3 --- calculadora')
        # if button Libre Office cliked
        if label == office.get_properties('label'):
            os.system('/usr/bin/soffice')
            print('3 --- Libre Office')

    def cliked_plus_or_minus(self, widget):

        print('entra cliked '*2)
        label = widget.get_properties('label')
        print(label[0])

        #cria as variáveis para mudar a label dos botões, if só para ficar identado
        if True:
            print('if com zero funciona')
            plus = Gtk.Label()
            plus.set_label('PLUS')
            self.plus_label = self.plus.get_child()

            minus = Gtk.Label()
            minus.set_label('Dimunui Letra -')
            self.minus_label = self.minus.get_child()

            google = Gtk.Label()
            google.set_label('PESQUISAR NA INTERNET')
            self.google_label = self.google.get_child()

            youtube = Gtk.Label()
            youtube.set_label('YOUTUBE')
            self.youtube_label = self.youtube.get_child()

            facebook = Gtk.Label()
            facebook.set_label('FACEBOOK')
            self.facebook_label = self.facebook.get_child()

            netflix = Gtk.Label()
            netflix.set_label('NETFLIX')
            self.netflix_label = self.netflix.get_child()

            gmail = Gtk.Label()
            gmail.set_label('E-MAIL')
            self.gmail_label = self.gmail.get_child()

            gedit = Gtk.Label()
            gedit.set_label('Bloco de Notas')
            self.gedit_label = self.gedit.get_child()

            calc = Gtk.Label()
            calc.set_label('CALCULADORA')
            self.calc_label = self.calc.get_child()

            office = Gtk.Label()
            office.set_label('Libre Office')
            self.office_label = self.office.get_child()

        print("plus tam inicio")
        print(self.plus.tam)
        if label == plus.get_properties('label'):
            if self.plus.tam == 0:
                self.plus_label.set_markup('<big>Aumenta Letra +</big>')
                self.minus_label.set_markup('<big>Dimunui Letra -</big>')
                self.google_label.set_markup('<big>PESQUISAR NA INTERNET</big>')
                self.youtube_label.set_markup('<big>YOUTUBE</big>')
                self.facebook_label.set_markup('<big>FACEBOOK</big>')
                self.netflix_label.set_markup('<big>NETFLIX</big>')
                self.gmail_label.set_markup('<big>E-MAIL</big>')
                self.gedit_label.set_markup('<big>Bloco de Notas</big>')
                self.calc_label.set_markup('<big>CALCULADORA</big>')

                self.office_label.set_markup('<big>Libre Office</big>')

            elif self.plus.tam == 1:
                self.plus_label.set_markup('<big><big>Aumenta Letra +</big></big>')
                self.minus_label.set_markup('<big><big>Dimunui Letra -</big></big>')
                self.google_label.set_markup('<big><big>PESQUISAR NA INTERNET</big></big>')
                self.youtube_label.set_markup('<big><big>YOUTUBE</big></big>')
                self.facebook_label.set_markup('<big><big>FACEBOOK</big></big>')
                self.netflix_label.set_markup('<big><big>NETFLIX</big></big>')
                self.gmail_label.set_markup('<big><big>E-MAIL</big></big>')
                self.gedit_label.set_markup('<big><big>Bloco de Notas</big></big>')
                self.calc_label.set_markup('<big><big>CALCULADORA</big></big>')
                self.office_label.set_markup('<big><big>Libre Office</big></big>')

            elif self.plus.tam == 2:
                self.plus_label.set_markup('<big><big><big>Aumenta Letra +</big></big></big>')
                self.minus_label.set_markup('<big><big><big>Dimunui Letra -</big></big></big>')
                self.google_label.set_markup('<big><big><big>PESQUISAR NA INTERNET</big></big></big>')
                self.youtube_label.set_markup('<big><big><big>YOUTUBE</big></big></big>')
                self.facebook_label.set_markup('<big><big><big>FACEBOOK</big></big></big>')
                self.netflix_label.set_markup('<big><big><big>NETFLIX</big></big></big>')
                self.gmail_label.set_markup('<big><big><big>E-MAIL</big></big></big>')
                self.gedit_label.set_markup('<big><big><big>Bloco de Notas</big></big></big>')
                self.calc_label.set_markup('<big><big><big>CALCULADORA</big></big></big>')
                self.office_label.set_markup('<big><big><big>Libre Office</big></big></big>')

            elif self.plus.tam == 3:
                self.plus_label.set_markup('<big><big><big><big>Aumenta Letra +</big></big></big></big>')
                self.minus_label.set_markup('<big><big><big><big>Dimunui Letra -</big></big></big></big>')
                self.google_label.set_markup('<big><big><big><big>PESQUISAR NA INTERNET</big></big></big></big>')
                self.youtube_label.set_markup('<big><big><big><big>YOUTUBE</big></big></big></big>')
                self.facebook_label.set_markup('<big><big><big><big>FACEBOOK</big></big></big></big>')
                self.netflix_label.set_markup('<big><big><big><big>NETFLIX</big></big></big></big>')
                self.gmail_label.set_markup('<big><big><big><big>E-MAIL</big></big></big></big>')
                self.gedit_label.set_markup('<big><big><big><big>Bloco de Notas</big></big></big></big>')
                self.calc_label.set_markup('<big><big><big><big>CALCULADORA</big></big></big></big>')
                self.office_label.set_markup('<big><big><big><big>Libre Office</big></big></big></big>')

            elif self.plus.tam == 4:
                self.plus_label.set_markup('<big><big><big><big><big>Aumenta Letra +</big></big></big></big></big>')
                self.minus_label.set_markup('<big><big><big><big><big>Dimunui Letra -</big></big></big></big></big>')
                self.google_label.set_markup('<big><big><big><big><big>PESQUISAR NA INTERNET</big></big></big></big></big>')
                self.youtube_label.set_markup('<big><big><big><big><big>YOUTUBE</big></big></big></big></big>')
                self.facebook_label.set_markup('<big><big><big><big><big>FACEBOOK</big></big></big></big></big>')
                self.netflix_label.set_markup('<big><big><big><big><big>NETFLIX</big></big></big></big></big>')
                self.gmail_label.set_markup('<big><big><big><big><big>E-MAIL</big></big></big></big></big>')
                self.gedit_label.set_markup('<big><big><big><big><big>Bloco de Notas</big></big></big></big></big>')
                self.calc_label.set_markup('<big><big><big><big><big>CALCULADORA</big></big></big></big></big>')
                self.office_label.set_markup('<big><big><big><big><big>Libre Office</big></big></big></big></big>')

            else :
                self.plus_label.set_markup('<big><big><big><big><big><big>Aumenta Letra +</big></big></big></big></big></big>')
                self.minus_label.set_markup('<big><big><big><big><big><big>Dimunui Letra -</big></big></big></big></big></big>')
                self.google_label.set_markup('<big><big><big><big><big><big>PESQUISAR NA INTERNET</big></big></big></big></big></big>')
                self.youtube_label.set_markup('<big><big><big><big><big><big>YOUTUBE</big></big></big></big></big></big>')
                self.facebook_label.set_markup('<big><big><big><big><big><big>FACEBOOK</big></big></big></big></big></big>')
                self.netflix_label.set_markup('<big><big><big><big><big><big>NETFLIX</big></big></big></big></big></big>')
                self.gmail_label.set_markup('<big><big><big><big><big><big>E-MAIL</big></big></big></big></big></big>')
                self.gedit_label.set_markup('<big><big><big><big><big><big>Bloco de Notas</big></big></big></big></big></big>')
                self.calc_label.set_markup('<big><big><big><big><big><big>CALCULADORA</big></big></big></big></big></big>')
                self.office_label.set_markup('<big><big><big><big><big><big>Libre Office</big></big></big></big></big></big>')


                self.plus.tam = 5
            self.plus.tam += 1

        #if minus button cliked
        if label == minus.get_properties('label'):
            if self.plus.tam == 1:
                self.plus_label.set_markup('Aumenta Letra +')
                self.minus_label.set_markup('Dimunui Letra -')
                self.google_label.set_markup('PESQUISAR NA INTERNET')
                self.youtube_label.set_markup('YOUTUBE')
                self.facebook_label.set_markup('FACEBOOK')
                self.netflix_label.set_markup('NETFLIX')
                self.gmail_label.set_markup('E-MAIL')
                self.gedit_label.set_markup('Bloco de Notas')
                self.calc_label.set_markup('CALCULADORA')
                self.office_label.set_markup('Libre Office')


            elif self.plus.tam == 2:
                self.plus_label.set_markup('<big>Aumenta Letra +</big>')
                self.minus_label.set_markup('<big>Dimunui Letra -</big>')
                self.google_label.set_markup('<big>PESQUISAR NA INTERNET</big>')
                self.youtube_label.set_markup('<big>YOUTUBE</big>')
                self.facebook_label.set_markup('<big>FACEBOOK</big>')
                self.netflix_label.set_markup('<big>NETFLIX</big>')
                self.gmail_label.set_markup('<big>E-MAIL</big>')
                self.gedit_label.set_markup('<big>Bloco de Notas</big>')
                self.calc_label.set_markup('<big>CALCULADORA</big>')
                self.office_label.set_markup('<big>Libre Office</big>')


            elif self.plus.tam == 3:
                self.plus_label.set_markup('<big><big>Aumenta Letra +</big></big>')
                self.minus_label.set_markup('<big><big>Dimunui Letra -</big></big>')
                self.google_label.set_markup('<big><big>PESQUISAR NA INTERNET</big></big>')
                self.youtube_label.set_markup('<big><big>YOUTUBE</big></big>')
                self.facebook_label.set_markup('<big><big>FACEBOOK</big></big>')
                self.netflix_label.set_markup('<big><big>NETFLIX</big></big>')
                self.gmail_label.set_markup('<big><big>E-MAIL</big></big>')
                self.gedit_label.set_markup('<big><big>Bloco de Notas</big></big>')
                self.calc_label.set_markup('<big><big>CALCULADORA</big></big>')
                self.office_label.set_markup('<big><big>Libre Office</big></big>')


            elif self.plus.tam == 4:
                self.plus_label.set_markup('<big><big><big>Aumenta Letra +</big></big></big>')
                self.minus_label.set_markup('<big><big><big>Dimunui Letra -</big></big></big>')
                self.google_label.set_markup('<big><big><big>PESQUISAR NA INTERNET</big></big></big>')
                self.youtube_label.set_markup('<big><big><big>YOUTUBE</big></big></big>')
                self.facebook_label.set_markup('<big><big><big>FACEBOOK</big></big></big>')
                self.netflix_label.set_markup('<big><big><big>NETFLIX</big></big></big>')
                self.gmail_label.set_markup('<big><big><big>E-MAIL</big></big></big>')
                self.gedit_label.set_markup('<big><big><big>Bloco de Notas</big></big></big>')
                self.calc_label.set_markup('<big><big><big>CALCULADORA</big></big></big>')
                self.office_label.set_markup('<big><big><big>Libre Office</big></big></big>')


            elif self.plus.tam == 5:
                self.plus_label.set_markup('<big><big><big><big>Aumenta Letra +</big></big></big></big>')
                self.minus_label.set_markup('<big><big><big><big>Dimunui Letra -</big></big></big></big>')
                self.google_label.set_markup('<big><big><big><big>PESQUISAR NA INTERNET</big></big></big></big>')
                self.youtube_label.set_markup('<big><big><big><big>YOUTUBE</big></big></big></big>')
                self.facebook_label.set_markup('<big><big><big><big>FACEBOOK</big></big></big></big>')
                self.netflix_label.set_markup('<big><big><big><big>NETFLIX</big></big></big></big>')
                self.gmail_label.set_markup('<big><big><big><big>E-MAIL</big></big></big></big>')
                self.gedit_label.set_markup('<big><big><big><big>Bloco de Notas</big></big></big></big>')
                self.calc_label.set_markup('<big><big><big><big>CALCULADORA</big></big></big></big>')
                self.office_label.set_markup('<big><big><big><big>Libre Office</big></big></big></big>')


            elif self.plus.tam == 6:
                self.plus_label.set_markup('<big><big><big><big><big>Aumenta Letra +</big></big></big></big></big>')
                self.minus_label.set_markup('<big><big><big><big><big>Dimunui Letra -</big></big></big></big></big>')
                self.google_label.set_markup('<big><big><big><big><big>PESQUISAR NA INTERNET</big></big></big></big></big>')
                self.youtube_label.set_markup('<big><big><big><big><big>YOUTUBE</big></big></big></big></big>')
                self.facebook_label.set_markup('<big><big><big><big><big>FACEBOOK</big></big></big></big></big>')
                self.netflix_label.set_markup('<big><big><big><big><big>NETFLIX</big></big></big></big></big>')
                self.gmail_label.set_markup('<big><big><big><big><big>E-MAIL</big></big></big></big></big>')
                self.gedit_label.set_markup('<big><big><big><big><big>Bloco de Notas</big></big></big></big></big>')
                self.calc_label.set_markup('<big><big><big><big><big>CALCULADORA</big></big></big></big></big>')
                self.office_label.set_markup('<big><big><big><big><big>Libre Office</big></big></big></big></big>')


            else:
                self.plus.tam = 1
            self.plus.tam -= 1

        print("fim")
        print(self.plus.tam)


window = MainWindow()
window.fullscreen()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
