from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image

from models.id_model import get_ids


class ViewIDsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Scroll view
        self.scroll = ScrollView()

        self.ids_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=20
        )

        self.ids_layout.bind(minimum_height=self.ids_layout.setter('height'))

        self.scroll.add_widget(self.ids_layout)

        # Buttons
        load_btn = Button(text="Load Saved IDs", size_hint=(1, 0.15))
        load_btn.bind(on_press=self.load_ids)

        back_btn = Button(text="Back to Home", size_hint=(1, 0.15))
        back_btn.bind(on_press=self.go_home)

        main_layout.add_widget(load_btn)
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def load_ids(self, instance):

        self.ids_layout.clear_widgets()

        ids = get_ids()

        for data in ids:

            name = data[1]
            id_number = data[2]
            image_path = data[3]

            # Card layout
            card = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=150,
                padding=10,
                spacing=10
            )

            # Image
            try:
                img = Image(source=image_path, size_hint=(0.4, 1))
            except:
                img = Label(text="No Image")

            # Text area
            info = BoxLayout(orientation='vertical')

            name_label = Label(text=f"Name: {name}")
            id_label = Label(text=f"ID Number: {id_number}")

            info.add_widget(name_label)
            info.add_widget(id_label)

            card.add_widget(img)
            card.add_widget(info)

            self.ids_layout.add_widget(card)

    def go_home(self, instance):
        self.manager.current = "home"