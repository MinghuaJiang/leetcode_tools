import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2
from gi.repository import Gdk
from leetcode_client import LeetcodeClient


class WebView:
    def __init__(self):
        self.window = Gtk.Window()
        self.view = WebKit2.WebView()
        self.client = LeetcodeClient()
        self.window.connect('delete-event', Gtk.main_quit)
        self.window.connect('key_press_event', self.on_key_press_event)
        self.view.load_uri(self.client.get_random_problem())
        self.window.add(self.view)
        self.window.fullscreen()
        self.window.show_all()

    def update_view(self):
        self.view.load_uri(self.client.get_random_problem())

    def on_key_press_event(self, widget, event):
        # see if we recognise a keypress
        if event.keyval == Gdk.KEY_F5:
            self.update_view()
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

if __name__ == "__main__":
    view = WebView()
    Gtk.main()

