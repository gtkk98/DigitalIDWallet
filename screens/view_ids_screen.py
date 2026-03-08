from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class ViewIDsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        # Scroll area for IDs
        self.scroll = ScrollView
        self.ids_layout =   BoxLayout(orientation= 'vertical', size_hint_y=None)
        self.ids_layout.bind(minimum_height=self.ids_layout.setter('height'))

        self.scroll.add_widget(self.ids_layout)

        # Load Button
        load_btn = Button(text="Load Saved IDs", size_hint=(1, 0.2))
        load_btn.bind(on_press=self.load_ids)

        # Back Button
        back_btn = Button(text="Back to Home", size_hint=(1, 0.2))
        back_btn.bind(on_press=self.go_home)

        main_layout.add_widget(load_btn)
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)
