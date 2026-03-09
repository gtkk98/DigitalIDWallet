from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class LockScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.correct_pin = "1234"

        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=20
        )

        layout.add_widget(Label(text="Enter Wallet PIN"))

        self.pin_input = TextInput(
            password=True,
            multiline=False,
            hint_text="Enter PIN"
        )

        layout.add_widget(self.pin_input)

        unlock_btn = Button(text="Unlock")
        unlock_btn.bind(on_press=self.check_pin)

        layout.add_widget(unlock_btn)

        self.message = Label(text="")
        layout.add_widget(self.message)

        self.add_widget(layout)

    def check_pin(self, instance):

        if self.pin_input.text == self.correct_pin:
            self.manager.current = "home"
        else:
            self.message.text = "Wrong PIN"