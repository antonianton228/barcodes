from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard as Cb
import threading
import socket

KV = '''
MyBl:
        Label:
                font_size: "30sp"
                text: root.data_label
'''

class MyBl(BoxLayout):
    data_label = StringProperty('!!!')

class MyApp(App):
    running = True
    def build(self):
        return Builder.load_string(KV)
    def on_stop(self):
        running = False
MyApp().run()