from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from homemapview import HomeMapView
from kivy.core.window import Window
from searchpopupmenu import SearchPopupMenu
from homegpshelper import HomeGpsHelper
from apikey_ import lta_account_key
from kivy.properties import ObjectProperty
from market_folder.marketmapview import MarketMapView
from product_folder.productbackdroplayout import ProductBackDropLayout
from product_folder.productsearchpopupmenu import ProductSearchPopupMenu
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import os



#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
url = 'http://datamall2.mytransport.sg/' #Resource URL
 
Window.size = (380, 650)
Window.title = "app"
class HomeScreen(Screen):
    pass
class MarketScreen(Screen):
    pass

class ProductScreen(Screen):
    pass

class MainApp(MDApp):

    busstopsearch_menu = None

    marketmapview = ObjectProperty(None)

    search_menu = None

    current_lat = -0.53112
    current_lon = 30.45061

    if os.path.isfile("profile_source.txt"):
        with open("profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "empty.jpg"
    else:
        img_source_path = "empty.jpg"

  
    def on_start(self):

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

        # Initialize GPS
        HomeGpsHelper().run()

        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "900"
        self.theme_cls.theme_style = "Light"
        # Instantiate the bus stop back drop
        self.product_backdroplayout = ProductBackDropLayout().run()
        # Add bus stop back drop to the bus stop screen
        self.root.ids.bus_stop_screen.ids.productbackdrop.add_widget(self.product_backdroplayout)
        # Instantiate BusStopSearchPopupMenu
        self.search_menu = ProductSearchPopupMenu()
 
    def change_screen(self, screen_name, direction='forward', mode = ""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
 
        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return
 
        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name
 
        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Market Finder"
        if screen_name == "market_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Nearby markets"
            marketscreen_mapview = self.root.ids.market_screen.ids.marketmapview

            self.marketmapview = MarketMapView()
            marketscreen_mapview.add_widget(self.marketmapview)
 
            self.marketmapview.center_on(self.current_lat, self.current_lon)
            from market_folder.marketgpshelper import TaxiGpsHelper
            TaxiGpsHelper().run() 
            if screen_name == "bus_stop_screen":
                print("Screen name is ", screen_name)
                self.root.ids.titlename.title = "Bus Stops"
                self.root.ids.bus_stop_screen.ids.busstoptoolbar.ids.label_title.font_size = '13sp'
                bus_stop_backdropfrontlayer = self.busstop_backdroplayout.ids.frontlayer
            try:
                # Remove taximapview widget
                for w in taxiscreen_mapview.walk():
                    if w.__class__ == TaxiMapView:
                        print("remove busroutemapview widget")
                        taxiscreen_mapview.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
MainApp().run()