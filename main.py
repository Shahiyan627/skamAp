from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

Window.clearcolor = (0.1, 0.1, 0.1, 1)

Builder.load_string("""
<GameCard>:
    orientation: 'vertical'
    size_hint_y: None
    height: 250
    padding: 10
    spacing: 5
    canvas.before:
        Color:
            rgb: 0.2, 0.2, 0.2
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5,]

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: 0
                spacing: 0

                # Header Section
                BoxLayout:
                    id: header
                    size_hint_y: None
                    height: 60
                    padding: [20, 0]
                    canvas.before:
                        Color:
                            rgb: 0.2, 0.2, 0.2
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    Label:
                        text: "SKAMALEXA"
                        font_size: '24sp'
                        color: 0.8, 0.2, 0.2, 1
                        bold: True
                        halign: 'left'
                        valign: 'middle'
                        text_size: self.size
                    BoxLayout:
                        size_hint_x: None
                        width: 400
                        padding: [10, 0]
                        spacing: 20
                        Button:
                            text: "Главная"
                            font_size: '16sp'
                            color: 1, 1, 1, 1
                            background_color: 0.1, 0.1, 0.1, 0
                            background_normal: ''
                            on_release: root.manager.current = 'main'
                        Button:
                            text: "Каталог"
                            font_size: '16sp'
                            color: 1, 1, 1, 1
                            background_color: 0.1, 0.1, 0.1, 0
                            background_normal: ''
                            on_release: root.manager.current = 'catalog'
                        Button:
                            text: "О нас"
                            font_size: '16sp'
                            color: 1, 1, 1, 1
                            background_color: 0.1, 0.1, 0.1, 0
                            background_normal: ''
                            on_release: root.manager.current = 'about'
                        Button:
                            text: "Контакты"
                            font_size: '16sp'
                            color: 1, 1, 1, 1
                            background_color: 0.1, 0.1, 0.1, 0
                            background_normal: ''
                            on_release: root.manager.current = 'contacts'

                # Hero Section
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: 350
                    spacing: 15
                    padding: [50, 50, 50, 50]
                    Label:
                        text: "Вселенные лучших игр в одном паке"
                        font_size: '36sp'
                        bold: True
                        color: 1, 1, 1, 1
                        halign: 'center'
                        valign: 'middle'
                    Label:
                        text: "Получите полные коллекции легендарных серий по выгодной цене."
                        font_size: '18sp'
                        color: 0.8, 0.8, 0.8, 1
                        halign: 'center'
                        valign: 'middle'

                # Наши наборы Section
                BoxLayout:
                    orientation: 'vertical'
                    padding: [50, 20]
                    spacing: 20
                    size_hint_y: None
                    height: self.minimum_height
                    Label:
                        text: "Наши наборы"
                        font_size: '28sp'
                        bold: True
                        color: 1, 1, 1, 1
                        halign: 'left'
                        valign: 'middle'
                        size_hint_y: None
                        height: 40
                    GridLayout:
                        id: games_container
                        cols: 3
                        spacing: 15
                        padding: 0
                        size_hint_y: None
                        height: self.minimum_height

                # Footer Section
                BoxLayout:
                    id: footer
                    size_hint_y: None
                    height: 100
                    padding: [20, 10]
                    orientation: 'vertical'
                    canvas.before:
                        Color:
                            rgb: 0.2, 0.2, 0.2
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    Label:
                        text: "© 2025 Skamalexa. Все права защищены."
                        font_size: '14sp'
                        color: 0.7, 0.7, 0.7, 1
                        halign: 'center'
                        valign: 'bottom'
                    Label:
                        text: "Внимание: Вы должны обладать правами на распространение данных игр."
                        font_size: '10sp'
                        color: 0.6, 0.6, 0.6, 1
                        halign: 'center'
                        valign: 'top'

<CatalogScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 20
        # Header Section
        BoxLayout:
            id: header
            size_hint_y: None
            height: 60
            padding: [20, 0]
            canvas.before:
                Color:
                    rgb: 0.2, 0.2, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "SKAMALEXA"
                font_size: '24sp'
                color: 0.8, 0.2, 0.2, 1
                bold: True
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            BoxLayout:
                size_hint_x: None
                width: 400
                padding: [10, 0]
                spacing: 20
                Button:
                    text: "Главная"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'main'
                Button:
                    text: "Каталог"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'catalog'
                Button:
                    text: "О нас"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'about'
                Button:
                    text: "Контакты"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'contacts'

        Label:
            text: "КАТАЛОГ ИГР"
            font_size: '36sp'
            bold: True
            color: 0.9, 0.9, 0.9, 1
            size_hint_y: None
            height: 60
        ScrollView:
            GridLayout:
                id: catalog_games_container
                cols: 2
                spacing: 15
                padding: 10
                size_hint_y: None
                height: self.minimum_height

<PaymentScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [0, 50]
        spacing: 30

        # Header Section
        BoxLayout:
            id: header
            size_hint_y: None
            height: 60
            padding: [20, 0]
            canvas.before:
                Color:
                    rgb: 0.2, 0.2, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "SKAMALEXA"
                font_size: '24sp'
                color: 0.8, 0.2, 0.2, 1
                bold: True
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            BoxLayout:
                size_hint_x: None
                width: 400
                padding: [10, 0]
                spacing: 20
                Button:
                    text: "Главная"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'main'
                Button:
                    text: "Каталог"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'catalog'
                Button:
                    text: "О нас"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'about'
                Button:
                    text: "Контакты"
                    font_size: '16sp'
                    color: 1, 1, 1, 1
                    background_color: 0.1, 0.1, 0.1, 0
                    background_normal: ''
                    on_release: root.manager.current = 'contacts'

        # Payment Form
        BoxLayout:
            orientation: 'vertical'
            size_hint: (0.7, 0.9)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: 20
            spacing: 20
            canvas.before:
                Color:
                    rgb: 0.2, 0.2, 0.2
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [5,]

            Label:
                text: "Оформление заказа"
                font_size: '28sp'
                bold: True
                color: 0.8, 0.2, 0.2, 1
                size_hint_y: None
                height: 40

            # Product Info Section
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: 120
                padding: 15
                spacing: 10
                canvas.before:
                    Color:
                        rgb: 0.2, 0.2, 0.2
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [5,]
                Label:
                    text: "Ваш товар:"
                    font_size: '16sp'
                    color: 0.7, 0.7, 0.7, 1
                    halign: 'center'
                    size_hint_y: None
                    height: 30
                Label:
                    id: payment_info
                    text: ""
                    font_size: '20sp'
                    bold: True
                    color: 1, 1, 1, 1
                    halign: 'center'
                    size_hint_y: None
                    height: 30

            Label:
                text: "Ваш E-mail (для получения ключа)"
                font_size: '14sp'
                halign: 'left'
                text_size: self.size
                size_hint_y: None
                height: 20

            TextInput:
                id: email_input
                hint_text: "user@example.com"
                size_hint: (1, None)
                height: 40
                multiline: False
                background_color: 0.3, 0.3, 0.3, 1
                foreground_color: 1, 1, 1, 1
                font_size: '16sp'

            Label:
                text: "Номер банковской карты"
                font_size: '14sp'
                halign: 'left'
                text_size: self.size
                size_hint_y: None
                height: 20

            TextInput:
                id: card_number
                hint_text: "0000 0000 0000 0000"
                input_type: 'number'
                size_hint: (1, None)
                height: 40
                multiline: False
                background_color: 0.3, 0.3, 0.3, 1
                foreground_color: 1, 1, 1, 1
                font_size: '16sp'

            BoxLayout:
                size_hint: (1, None)
                height: 40
                spacing: 10
                Label:
                    text: "Срок действия"
                    font_size: '14sp'
                    halign: 'left'
                    text_size: self.size
                Label:
                    text: "CVC-код"
                    font_size: '14sp'
                    halign: 'left'
                    text_size: self.size

            BoxLayout:
                size_hint: (1, None)
                height: 40
                spacing: 10
                TextInput:
                    id: expiry_date
                    hint_text: "MM / YY"
                    input_type: 'text'
                    size_hint_x: 0.7
                    multiline: False
                    background_color: 0.3, 0.3, 0.3, 1
                    foreground_color: 1, 1, 1, 1
                    font_size: '16sp'
                TextInput:
                    id: cvv
                    hint_text: "123"
                    input_type: 'number'
                    size_hint_x: 0.3
                    multiline: False
                    background_color: 0.3, 0.3, 0.3, 1
                    foreground_color: 1, 1, 1, 1
                    font_size: '16sp'

            Button:
                id: pay_button
                text: "ОПЛАТИТЬ"
                size_hint: (1, None)
                height: 50
                background_color: 0.8, 0.2, 0.2, 1
                background_normal: ''
                color: (1, 1, 1, 1)
                font_size: '18sp'
                on_release: app.process_payment()
""")


class GameCard(BoxLayout):
    pass


class MainScreen(Screen):
    def on_enter(self, *args):
        self.build_ui()

    def build_ui(self):
        games_container = self.ids.games_container
        games_container.clear_widgets()

        games = [
            {"name": "Коллекция Hitman", "image": "img/Hitman_2015.jpg", "price": "5₽"},
            {"name": "Cara Assassin's Creed", "image": "img/assasins.jpeg", "price": "5₽"},
            {"name": "Антология Far Cry", "image": "img/farcry.jpg", "price": "5₽"},
        ]

        for game in games:
            game_card = GameCard()

            try:
                game_image = Image(source=game['image'], size_hint_y=None, height=120, allow_stretch=True,
                                   keep_ratio=True)
            except Exception:
                game_image = Label(text="Нет\nизображения", halign="center", valign="middle", size_hint_y=None,
                                   height=120, color=(0.8, 0.8, 0.8, 1))

            game_title = Label(
                text=f"[b]{game['name']}[/b]",
                font_size='18sp',
                halign='center',
                valign='middle',
                color=(1, 1, 1, 1),
                markup=True,
                size_hint_y=None,
                height=30
            )

            price_label = Label(
                text=f"[b]{game['price']}[/b]",
                font_size='24sp',
                halign='center',
                valign='middle',
                color=(1, 1, 1, 1),
                markup=True,
                size_hint_y=None, height=40
            )

            buy_button = Button(
                text="Купить",
                size_hint=(1, None),
                height=40,
                background_color=(0.8, 0.2, 0.2, 1),
                background_normal='',
                color=(1, 1, 1, 1),
                font_size='18sp'
            )
            buy_button.bind(
                on_release=lambda btn, game_name=game['name'], price=game['price']: App.get_running_app().show_payment(
                    game_name, price))

            game_card.add_widget(game_image)
            game_card.add_widget(game_title)
            game_card.add_widget(price_label)
            game_card.add_widget(buy_button)

            games_container.add_widget(game_card)


class CatalogScreen(Screen):
    def on_enter(self, *args):
        self.build_ui()

    def build_ui(self):
        games_container = self.ids.catalog_games_container
        games_container.clear_widgets()

        games = [
            {"name": "Hitman", "image": "img/Hitman_2015.jpg", "price": "5₽"},
            {"name": "Assassin's Creed", "image": "img/assasins.jpeg", "price": "5₽"},
            {"name": "Far Cry", "image": "img/farcry.jpg", "price": "5₽"},
            {"name": "Mafia", "image": "img/Mafia_Definitive_Edition.jpg", "price": "30₽"},
            {"name": "Spider-Man", "image": "img/spider-man.jpeg", "price": "70₽"},
        ]

        for game in games:
            game_card = GameCard()

            try:
                game_image = Image(source=game['image'], size_hint_y=None, height=120, allow_stretch=True,
                                   keep_ratio=True)
            except Exception:
                game_image = Label(text="Нет\nизображения", halign="center", valign="middle", size_hint_y=None,
                                   height=120, color=(0.8, 0.8, 0.8, 1))

            game_title = Label(
                text=f"[b]{game['name']}[/b]",
                font_size='18sp',
                halign='center',
                valign='middle',
                color=(1, 1, 1, 1),
                markup=True,
                size_hint_y=None,
                height=30
            )

            price_label = Label(
                text=f"[b]{game['price']}[/b]",
                font_size='24sp',
                halign='center',
                valign='middle',
                color=(1, 1, 1, 1),
                markup=True,
                size_hint_y=None, height=40
            )

            buy_button = Button(
                text="Купить",
                size_hint=(1, None),
                height=40,
                background_color=(0.8, 0.2, 0.2, 1),
                background_normal='',
                color=(1, 1, 1, 1),
                font_size='18sp'
            )
            buy_button.bind(
                on_release=lambda btn, game_name=game['name'], price=game['price']: App.get_running_app().show_payment(
                    game_name, price))

            game_card.add_widget(game_image)
            game_card.add_widget(game_title)
            game_card.add_widget(price_label)
            game_card.add_widget(buy_button)

            games_container.add_widget(game_card)


class PaymentScreen(Screen):
    pass


class GameStoreApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CatalogScreen(name='catalog'))
        sm.add_widget(PaymentScreen(name='payment'))
        return sm

    def show_payment(self, game_name, price):
        payment_screen = self.root.get_screen('payment')
        payment_screen.ids.payment_info.text = f"{game_name}\nЦена: {price}"
        self.root.current = 'payment'

    def process_payment(self):
        payment_screen = self.root.get_screen('payment')
        email = payment_screen.ids.email_input.text
        card_number = payment_screen.ids.card_number.text
        expiry_date = payment_screen.ids.expiry_date.text
        cvv = payment_screen.ids.cvv.text

        print(
            f"Обработка платежа...\nE-mail: {email}\nНомер карты: {card_number}\nСрок действия: {expiry_date}\nCVV: {cvv}")

        payment_screen.ids.email_input.text = ""
        payment_screen.ids.card_number.text = ""
        payment_screen.ids.expiry_date.text = ""
        payment_screen.ids.cvv.text = ""

        self.root.current = 'catalog'


if __name__ == '__main__':
    GameStoreApp().run()