from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from models.id_model import save_id


class AddIDScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        # Name input
        layout.add_widget(Label(text="Name"))
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        # ID Number input
        layout.add_widget(Label(text="ID Number"))
        self.id_input = TextInput(multiline=False)
        layout.add_widget(self.id_input)

        # Image path input
        layout.add_widget(Label(text="Image Path"))
        self.image_input = TextInput(multiline=False)
        layout.add_widget(self.image_input)

        # Save button
        save_btn = Button(text="Save ID")
        save_btn.bind(on_press=self.save_id_data)

        # Back button
        back_btn = Button(text="Back to Home")
        back_btn.bind(on_press=self.go_home)

        layout.add_widget(save_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def save_id_data(self, instance):

        name = self.name_input.text
        id_number = self.id_input.text
        image_path = self.image_input.text

        save_id(name, id_number, image_path)

        # clear fields after saving
        self.name_input.text = ""
        self.id_input.text = ""
        self.image_input.text = ""

        print("ID Saved")

    def go_home(self, instance):
        self.manager.current = "home"