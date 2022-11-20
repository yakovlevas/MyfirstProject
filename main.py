from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
image = '''
Image:
    source: "2.png"

'''

class MainApp(MDApp):
    def build(self):
        images = Builder.load_string(image)
        return images
#        return MDLabel(text="Hello, World", halign="center")


MainApp().run()



#import kivy
#kivy.require('2.1.0') # replace with your current kivy version !
#from kivy.app import App
#from kivy.uix.label import Label
#class MyApp(App):

#    def build(self):
#        return Label(text='Hello world')


#if __name__ == '__main__':
#    MyApp().run()