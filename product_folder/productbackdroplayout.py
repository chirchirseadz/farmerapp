from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import kivy.utils
from kivy.uix.scrollview import ScrollView
 
# Your layouts.
KV = (
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
 
<MyBackdropBackLayer@ScrollView>
 
<MyBackdropFrontLayer@Screen>
 
 
<BusStopBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Press for Market Products"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Available Products:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: container
 
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                id: frontlayer
                 
'''
)
 
class BusStopBackdrop(Screen):
    pass
 
class ProductBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return BusStopBackdrop()