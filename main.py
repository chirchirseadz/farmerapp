from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3 # He were importing the sqlite3 database

# This is the main class that the app runs
class MainApp(MDApp):
    connection  = None
    cursor = None
    def on_start(self):

    # initialize local database connection
        self.connection = sqlite3.connect("kenya.db")
        self.cursor = self.connection.cursor()
    # initialize GPS connection

    
    # Instantiatin local SearchPopupMenu
   
        


MainApp().run()