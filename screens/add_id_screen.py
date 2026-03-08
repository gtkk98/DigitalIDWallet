from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class AddIDScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        layout.add_widget(Label(text="Add ID Screen"))

        back_btn = Button(text="Back to Home")
        back_btn.bind(on_press=self.go_home)

        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_home(self, instance):
        self.manager.current = "home"