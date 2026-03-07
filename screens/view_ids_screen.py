from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from models.id_model import get_user_ids


class ViewIDsScreen(Screen):

    def on_pre_enter(self):
        self.load_ids()

    def load_ids(self):
        container = self.ids.id_list
        container.clear_widgets()

        ids = get_user_ids(1)

        for id_data in ids:
            card = BoxLayout(
                orientation="vertical",
                padding=10,
                spacing=5,
                size_hint_y=None,
                height=150
            )

            card.add_widget(Label(text=f"ID Type: {id_data[2]}"))
            card.add_widget(Label(text=f"ID Number: {id_data[3]}"))
            card.add_widget(Label(text=f"Expiry Date: {id_data[4]}"))

            container.add_widget(card)