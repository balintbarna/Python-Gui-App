from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


video_path = ""


class MainNode(Widget):
    video = ObjectProperty(None)

    def start(self):
        self.video.source = video_path


    def update(self, dt):
        pass


class VideoApp(App):
    def build(self):
        main = MainNode()
        main.start()
        Clock.schedule_interval(main.update, 1.0/60.0)
        return main


def toggle_fullscreen():
    if Window.fullscreen is False:
        Window.fullscreen = 'auto'
    else:
        Window.fullscreen = False


if __name__ == '__main__':
    toggle_fullscreen()
    VideoApp().run()
