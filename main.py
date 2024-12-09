from math import *

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color, RoundedRectangle, Ellipse
from kivy.core.window import Window
from kivy.uix.label import Label

from kivy.clock import Clock
from kivy.uix.widget import Widget

from data import *



popup_widget = None
parent_layout = None
Window.minimum_width, Window.minimum_height = 700, 500
def update_widget(parent, widget):
    parent.remove_widget(widget)
    parent.add_widget(widget)

class ParentLayout(BoxLayout):
    def __init__(self, **kwargs):
        global parent_layout
        super().__init__(**kwargs)
        self.child = TableOfElements()
        self.add_widget(self.child)
        parent_layout = self

    def on_size(self, *args):
        self.child.resize()


class TableOfElements(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min_dim = 0

        self.element_size = 0
        self.rows = 9
        for i in range(self.rows * 18):
            button = Element(i)
            self.add_widget(button)

    def resize(self, *args):
        self.size = min(Window.height, Window.width) * 0.8 * 1.4, min(Window.height, Window.width) * 0.8
        self.pos = Window.width / 2 - self.width / 2, 0


class Element(Button):
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        for i in range(len(families)):
            if list(families[i].keys()).count(self.id+1) > 0:
                self.background_color = colors[i]
                self.group = i
                self.element_class = families[i][self.id+1]
                self.halign = "center"
                self.markup = True
                name_size  = min(self.width/12, self.height * 0.2)
                number_size = min(self.width/12, self.height * 0.2)
                if len(self.element_class.symbol) != 0:
                    try:
                        symbol_size = self.width/self.element_class.max_word_length
                    except AttributeError:
                        symbol_size = self.width/ceil(len(self.element_class.symbol)/2)/4
                else:
                    symbol_size = 0
                self.text = "[size=" + str(int(number_size)) + "]" + str(self.element_class.number) + "[/size]\n[size=" + str(int(symbol_size)) + "]" + self.element_class.symbol + "[/size]\n[size=" + str(int(name_size)) + "px]" + self.element_class.name.capitalize() + "[/size]"

                break

        else:
            self.background_color = (0, 0, 0, 0)
            self.element_class = None


    def on_press(self):
        if self.element_class is not None:
            popup_widget.call(self.element_class, self.group)

# class ElementSymbol(Label):
#
#     def __init__(self, text, element_class, **kwargs):
#         super().__init__(**kwargs)
#         self.text = text
#         self.color = "#000000"
#         self.halign = "center"
#         self.valign = "center"
#         self.bold = True
#         self.element_class = element_class
#
#     def resize(self, parent_dim, parent_center):
#         self.size = parent_dim[0] * 0.5, parent_dim[1] * 0.5
#         self.center = parent_center
#         self.font_size = 10
#
# class ElementName(Label):
#
#     def __init__(self, text, **kwargs):
#         super().__init__(**kwargs)
#         self.text = text.capitalize()
#         self.color = "#000000"
#         self.halign = "center"
#         self.valign = "center"
#         self.bold = True
#
#     def resize(self, parent_pos, parent_dim, parent_center):
#         self.size = parent_dim[0], parent_dim[1] * 0.2
#         self.center_x = parent_center[0]
#         self.pos = parent_pos[0], parent_pos[1]
#         self.font_size = min(parent_dim[0]/7, parent_dim[1] * 0.2)
#
#
# class ElementNumber(Label):
#
#     def __init__(self, text, **kwargs):
#         super().__init__(**kwargs)
#         self.text = text.capitalize()
#         self.color = "#000000"
#         self.halign = "center"
#         self.valign = "center"
#         self.bold = True
#
#     def resize(self, parent_pos, parent_dim, parent_center):
#         self.size = parent_dim[0] * 0.1, parent_dim[1] * 0.1
#         self.pos = self.pos[0], parent_pos[1] + parent_dim[1] - self.height*3
#         self.center_x = parent_center[0]
#         self.font_size = min(parent_dim[0], parent_dim[1] * 0.2)
#
#
# class ElementText(Label):
#     def __init__(self, element_class, **kwargs):
#         super().__init__(**kwargs)
#         self.color = "#000000"
#         self.halign = "center"
#         self.valign = "center"
#         self.element_class = element_class
#         self.text = str(element_class.number) + "\n" + str(element_class.symbol)
#
#     def resize(self, parent_dim, parent_center):
#         self.size = parent_dim[0] * 0.5, parent_dim[1] * 0.5
#         self.center = parent_center
#         try:
#             self.font_size = min(self.height, self.width/ceil(self.element_class.max_word_length/3))
#         except AttributeError:
#             self.font_size = min(self.height, self.width / (ceil(len(self.text) / 2)))

class PopupWidget(BoxLayout):

    def __init__(self, **kwargs):
        global popup_widget
        super().__init__(**kwargs)
        self.called = False

        self.size_hint = 0.8, 0.8
        self.size = Window.width * 0.8, Window.height * 0.8
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.orientation = "vertical"
        popup_widget = self
        self.exit_button = Button(size_hint=(1, 0.1),
                                  text="Exit",
                                  on_press=self.delete,
                                  background_color="#ff0000")


    def on_size(self, *args):
        if self.called:
            self.canvas.clear()
            self.model.resize(parent_dim=self.size, parent_center=self.center)
            with self.canvas:
                Color(rgba=(0, 0, 0, 0.95))
                RoundedRectangle(size=self.size, pos=self.pos, radius=(7, 7, 7, 7))

            update_widget(self, self.exit_button)
            update_widget(self, self.header)
            update_widget(self, self.model)
            update_widget(self, self.data)

    def call(self, element_class, group):
        if type(element_class.number) == type(int()):
            if not self.called:
                self.called = True
                with self.canvas:
                    Color(rgba=(0, 0, 0, 0.95))
                    RoundedRectangle(size=self.size, pos=self.pos, radius=(7, 7, 7, 7))
                # self.exit_button = Button(size_hint=(1, 0.1))
                self.add_widget(self.exit_button)
                self.header = Label(size_hint=(1, 0.5),
                                    text=element_class.name.capitalize() + " - " + element_class.symbol,
                                    font_size=min(self.width, self.height/2)/5)
                self.model = BohrModel(element=element_class,
                                       parent_center=self.center,
                                       parent_dim=self.size)
                self.data = Label(size_hint=(1, 0.2),
                                  text="Protons: [color=#ff0000][b]" + str(element_class.number) + "[/b][/color]   Neutrons: [b]" + str(int(element_class.mass)-element_class.number) + "[/b]  Electrons: [color=#0000ff][b]" + str(element_class.number) + "[/b][/color]\n"
                                  + "Family:[b][color=" + colors[group] + "] " + group_names[group] + "[/color][/b]    Mass: [b]" + str(element_class.mass) + "[/b]",
                                  font_size=min(self.width, self.height/2)/15,
                                  markup=True,
                                  halign="center")
                self.add_widget(self.header)
                self.add_widget(self.model)
                self.add_widget(self.data)

    def delete(self, *args):
        for i in range(len(self.children)):
            self.remove_widget(self.children[0])
        self.called = False
        self.canvas.clear()


class BohrModel(Widget):

    def __init__(self, element, parent_dim, parent_center, **kwargs):
        super().__init__(**kwargs)
        self.size = min(parent_dim[0], parent_dim[1] * 0.5), min(parent_dim[0], parent_dim[1] * 0.5)
        self.center = parent_center[0], parent_center[1] - parent_dim[1] * 0.1
        self.element = element
        self.shells_data = shells[self.element.number]
        self.shells_num = len(self.shells_data)

        self.draw_bohr()

        self.name = Label(center=(self.center[0] + 5, self.center[1] + 5),
                          text="[b]"+ self.element.symbol + "[/b]"+"[b]\nP: [/b][color=#ff0000]"+str(self.element.number)+"[/color][b]\nN: [/b]"+str(int(self.element.mass)-self.element.number),
                          markup=True,
                          halign="center")
        self.add_widget(self.name)

    def resize(self, parent_dim, parent_center):
        self.size = min(parent_dim[0], parent_dim[1] * 0.5), min(parent_dim[0], parent_dim[1] * 0.5)
        self.center = parent_center
        self.canvas.clear()
        self.draw_bohr()
        self.name = Label(center=(self.center[0] + 5, self.center[1] + 5),
                          text="[b]" + self.element.symbol + "[/b]" + "[b]\nP: [/b]" + str(
                              self.element.number) + "[b]\nN: [/b]" + str(int(self.element.mass) - self.element.number),
                          markup=True,
                          halign="center")
        update_widget(self, self.name)

    def draw_bohr(self):
        with self.canvas:
            for i in range(1, self.shells_num+1):
                size = self.size[0]/(self.shells_num+1) * (self.shells_num+1-i)+50
                Color(rgb=(1, 1, 1))
                Ellipse(pos=(self.center[0] - size/2 + 5, self.center[1] - size/2 + 5), size=(size, size))
                Color(rgb=(0, 0, 0))
                Ellipse(pos=(self.center[0] - (size-4)/2 + 5, self.center[1] - (size-4)/2 + 5), size=(size-4, size-4))

                shell_data = self.shells_data[::-1][i - 1]
                shell_deg_incr = 360/shell_data
                for k in range(shell_data):
                    deg = shell_deg_incr * k
                    point = (self.center[0] + size/2 * cos(radians(deg+90)),
                             self.center[1] + size/2 * sin(radians(deg+90)))
                    Color(rgb=(0, 0, 1))
                    Ellipse(pos=point, size=(10, 10))


class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0.1)

    def post_init(self, *args):
        Clock.schedule_once(parent_layout.on_size, 0.1)



MainApp().run()
