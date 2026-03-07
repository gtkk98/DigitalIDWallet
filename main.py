from docutils.nodes import title
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from models.user_model import register_user, login_user
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from screens.add_id_screen import AddIDScreen
from models.id_model import add_id
from screens.view_ids_screen import ViewIDsScreen

Builder.load_file("ui/design.kv")

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class DigitalIDApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))
        self.sm.add_widget(AddIDScreen(name="add_id"))
        self.sm.add_widget(ViewIDsScreen(name="view_ids"))
        return self.sm

    def login(self, email, password):
        user = login_user(email, password)
        if user:
            self.sm.current = "dashboard"
        else:
            popup = Popup(title="Error",
                          content=Label(text="Invalid Email or Password"),
                          size_hint=(0.6, 0.4))
            popup.open()

    def register(self, name, email, password):
        success = register_user(name, email, password)
        if success:
            popup = Popup(title="Success",
                          content=Label(text="Registered Successfully!"),
                          size_hint=(0.6, 0.4))
            popup.open()
            self.sm.current = "login"
        else:
            popup = Popup(title="Error",
                          content=Label(text="Email already exists!"),
                          size_hint=(0.6, 0.4))
            popup.open()

    def save_id(self, id_type, id_number, expiry_date, image_path):
        user_id = 1 #temporary until login session added

        add_id(user_id, id_type, id_number, expiry_date, image_path)

        popup = Popup(
            title="Success",
            content=Label(text="ID Saved Successfully"),
            size_hint=(0.6, 0.4)
        )
        popup.open()


if __name__ == "__main__":
    DigitalIDApp().run()