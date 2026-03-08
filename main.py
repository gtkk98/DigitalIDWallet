from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import HomeScreen
from screens.add_id_screen import AddIDScreen
from screens.view_ids_screen import ViewIDsScreen


class DigitalIDApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(AddIDScreen(name="add_id"))
        sm.add_widget(ViewIDsScreen(name="view_ids"))

        return sm


if __name__ == "__main__":
    DigitalIDApp().run()