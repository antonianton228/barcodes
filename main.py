from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import time
from pyzbar import pyzbar
from glob import glob
import cv2




def decode_1(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print(f"Обнаружен штрих-код:\n{obj}")
        # print barcode type & data
        print("Тип:", obj.type)
        print("Данные:", obj.data)
        print()
    return image


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
        do_rotation: False
        rotation: 90
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.button()
    Label:
        font_size: "30sp"
        text: root.data_label
        
''')


class CameraClick(BoxLayout):
    data_label = StringProperty()
    def __init__(self, **kwargs):
        super(CameraClick, self).__init__(**kwargs)
        self.data_label = 'unpress'
        self.flag = True

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_" + timestr)
        print("Captured")

    def button(self):
        if self.flag:
            self.data_label = 'press'
        else:
            self.data_label = 'unpress'
        self.flag = not self.flag



class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
# decode_1(cv2.imread('2.jpg'))