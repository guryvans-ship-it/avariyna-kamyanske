from kivy.app import App
from kivy.uix.label import Label

class AvariynaApp(App):
    def build(self):
        return Label(text="Аварійна служба міста Кам’янське")

if __name__ == "__main__":
    AvariynaApp().run()
