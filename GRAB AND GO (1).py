from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (360, 640)


# ------------------ HOME SCREEN ------------------
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        title = Label(text="GrabNGo", font_size=32, bold=True)

        btn_login = Button(text="Login", size_hint=(1, 0.2))
        btn_register = Button(text="Register", size_hint=(1, 0.2))
        btn_products = Button(text="View Products", size_hint=(1, 0.2))

        btn_login.bind(on_press=lambda x: self.manager.current = "login")
        btn_register.bind(on_press=lambda x: self.manager.current = "register")
        btn_products.bind(on_press=lambda x: self.manager.current = "products")

        layout.add_widget(title)
        layout.add_widget(btn_login)
        layout.add_widget(btn_register)
        layout.add_widget(btn_products)

        self.add_widget(layout)


# ------------------ LOGIN SCREEN ------------------
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        layout.add_widget(Label(text="Login", font_size=26))

        self.email = TextInput(hint_text="Email", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)

        login_btn = Button(text="Login")
        back_btn = Button(text="Back")

        back_btn.bind(on_press=lambda x: self.go_home())

        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_home(self):
        self.manager.current = "home"


# ------------------ REGISTER SCREEN ------------------
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="Register", font_size=26))

        self.name = TextInput(hint_text="Full Name", multiline=False)
        self.email = TextInput(hint_text="Email", multiline=False)
        self.location = TextInput(hint_text="Location", multiline=False)
        self.phone = TextInput(hint_text="Phone", multiline=False)
        self.password = TextInput(hint_text="Password", password=True)

        back_btn = Button(text="Back")
        back_btn.bind(on_press=lambda x: self.go_home())

        layout.add_widget(self.name)
        layout.add_widget(self.email)
        layout.add_widget(self.location)
        layout.add_widget(self.phone)
        layout.add_widget(self.password)
        layout.add_widget(Button(text="Register"))
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_home(self):
        self.manager.current = "home"


# ------------------ PRODUCTS SCREEN ------------------
class ProductsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        products = [
            ("Stylish Bag", "15,000 CFA"),
            ("Sport Shoes", "25,000 CFA"),
            ("Summer Dress", "20,000 CFA"),
            ("Fresh Meat", "8,000 CFA"),
            ("Tomatoes", "2,500 CFA"),
            ("Onions", "1,500 CFA"),
            ("Eggs (Dozen)", "3,000 CFA"),
            ("Milk (1L)", "1,200 CFA"),
            ("Bread", "800 CFA"),
            ("Rice (1kg)", "1,500 CFA"),
        ]

        layout.add_widget(Label(text="Products", font_size=26))

        for name, price in products:
            box = BoxLayout(size_hint_y=None, height=40)
            box.add_widget(Label(text=name))
            box.add_widget(Label(text=price))
            layout.add_widget(box)

        back_btn = Button(text="Back")
        back_btn.bind(on_press=lambda x: self.go_home())
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_home(self):
        self.manager.current = "home"


# ------------------ APP ------------------
class GrabNGoApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(ProductsScreen(name="products"))

        return sm


if __name__ == "__main__":
    GrabNGoApp().run()