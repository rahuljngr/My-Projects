from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("user.json") as file:
            users = json.load(file)

        users[uname] = {'username': uname,'password':pword,
            'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print(users)

        with open ("user.json",'w') as file:
            json.dump(users,file)
        self.manager.current = "sign_up_screen_success"
class SignUpScreenSuccess(Screen):
    def go_to_login(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()