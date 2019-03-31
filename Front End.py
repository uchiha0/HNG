# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:51:46 2019

@author: Jude O
"""
import json
import kivy

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import (ListProperty,
                             NumericProperty,
                             ReferenceListProperty,
                             ObjectProperty,
                             BooleanProperty)
from kivy.uix.listview import ListView
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.vector import Vector
from kivy.network.urlrequest import UrlRequest
from kivy.graphics import Color, Ellipse, Line

#Set config first before doing the window thing or any other thing

#Window.fullscreen = 'auto'

Builder.load_string('''

<AddLocationForm>:
    orientation: 'vertical'
    search_input: search_box
    search_results: search_results_list
    BoxLayout:
        size_hint_y: None
        height: 40
        TextInput:
            id: search_box
            size_hint_x: .5
        Button:
            text: 'Search'
            size_hint_x: .25
            on_press: root.search_location()
        Button:
            text: 'Current Location'
            size_hint_x: .25
    ListView:
        id: search_results_list
        item_strings: []

''')



class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/weather?q={}"
        search_url      = search_template.format(self.search_input.text)
        request         = UrlRequest(search_url, self.found_location)
        print(request)

    def found_location(self, request, data):
        data    = json.loads(data.decode()) if isinstance(data,dict) else data
        cities  = [f"{d['name']} ({d['sys']['country']})" for d in data['list']]
        self.search_results.item_strings = cities


class MainApp(App):
    def build(self):
        return AddLocationForm()

if __name__ == '__main__':
    MainApp().run()






