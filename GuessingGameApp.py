from kivy import *
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


class WannaPlay(Screen):
    pass


class Guesses(Screen):
    def SetText(self):
        text = 'Guesses Left: 3'
        self.manager.get_screen('time_to_guess').label_text = text


class TimeToGuess(Screen):
    LabelText = StringProperty('')


class Winner(Screen):
    def SetText(self):
        text = 'Guesses Left: 3'
        self.manager.get_screen('time_to_guess').label_text = text


class Loser(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


kv = Builder.load_file('guessinggame.kv')


class GuessingGameApp(App):
    def build(self):
        return kv

    computer_num = random.randint(1, 10)
    random_num = str(computer_num)
    print(random_num)
    guesses_left = 3
    guess_text = 'Guesses Left: 3'
    user_guess = ''


if __name__ == '__main__':
    GuessingGameApp().run()
