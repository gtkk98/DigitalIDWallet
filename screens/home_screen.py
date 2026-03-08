from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        add_btn = Button(text="Add ID", size_hint=(1, 0.3))
        view_btn = Button(text="View IDs", size_hint=(1, 0.3))

        add_btn.bind(on_press=self.go_add)
        view_btn.bind(on_press=self.go_view)

        layout.add_widget(add_btn)
        layout.add_widget(view_btn)

        self.add_widget(layout)

    def go_add(self, instance):
        self.manager.current = "add_id"

    def go_view(self, instance):
        self.manager.current = "view_ids"