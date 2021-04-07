import random
import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner


class MyBackground(Widget):
    def __init__(self, **kwargs):
        super(MyBackground, self).__init__(**kwargs)
        with self.canvas:
            self.bg = Rectangle(source='Woodlawn_HS_4.jpg', pos=self.pos, size=self.size)

        self.bind(pos=self.update_bg)
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class ScrollViewApp(App):

    def build(self):

        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, padding=0, spacing=0,
                size_hint=(None, None),
                row_default_height = '50dp',
                width = 500,
                row_force_default = True)

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(13):
            spn = Spinner(text = "Games",
                values = ("pong", "cards", "chess", "ps5"),
                background_color = (0.784, 0.443, 0.216, 1))
            spn.size_hint = (0.3, 0.2)
            layout.add_widget(spn)

            spn = Spinner(text = "Mediation",
                values = ("pong", "cards", "chess", "ps5"),
                background_color = (0.784, 0.443, 0.216, 1))
            spn.size_hint = (0.3, 0.2)
            layout.add_widget(spn)

            spn = Spinner(text = "Asmr",
                values = ("pong", "cards", "chess", "ps5"),
                background_color = (0.784, 0.443, 0.216, 1))
            spn.size_hint = (0.3, 0.2)
            layout.add_widget(spn)

            spn = Spinner(text = "Homework",
                values = ("pong", "cards", "chess", "ps5"),
                background_color = (0.784, 0.443, 0.216, 1))
            spn.size_hint = (0.3, 0.2)
            layout.add_widget(spn)

            spn = Spinner(text = "Nap",
                values = ("pong", "cards", "chess", "ps5"),
                background_color = (0.784, 0.443, 0.216, 1))
            spn.size_hint = (0.3, 0.2)
            layout.add_widget(spn)

        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        root.add_widget(layout)

        return root

    def click(self, event):
        print("Hello Tujuana")
        print("Congratulations !!!!!!!")


if __name__ == '__main__':

    ScrollViewApp().run()
