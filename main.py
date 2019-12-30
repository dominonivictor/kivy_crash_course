from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ScatterTextWidget(BoxLayout):
    pass


class HelloApp(App):
    def build(self):
        boxL = BoxLayout(orientation='vertical')
        textI = TextInput(font_size=150, 
                          size_hint_y=None,
                          height=200,
                          text='default'
                        )
        floatL = FloatLayout()
        scatter = Scatter()
        label = Label(text="default",
                  font_size=150
                )

        textI.bind(text=label.setter('text'))

        floatL.add_widget(scatter)
        scatter.add_widget(label)
        
        boxL.add_widget(floatL)
        boxL.add_widget(textI)
        return boxL

if __name__ == '__main__':
    HelloApp().run()