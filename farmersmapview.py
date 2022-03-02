
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
class FarmersMapView(MapView):
    getting_market_timer = None
    def start_getting_markets_in_fov(self):
        # after 1s get the markets in the field of view
        try:
            self.getting_market_timer.cancel()
        except:
            pass
        self.getting_market_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        print(self.get_bbox())
        min_lat, max_lat, min_lon, max_lon = self.get_bbox()
        # Get refrence to the Main app and the database cursor
        app = App.get_running_app()
        sql_statement = 'SELECT * FROM markets WHERE lat > %s AND lat < %s AND lon > %s AND lon < %s'%(min_lat, max_lat, min_lon, max_lon)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(sql_statement)