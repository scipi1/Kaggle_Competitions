from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.image import Image 
from kivy.uix.popup import Popup
import numpy as np


#-------------------------------------------------------------------------------------------------------------------------------------------------
r = 1
min_dist = 0.1

class Avatar:
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.surname = kwargs['surname']
        self.nickname = kwargs['nickname']
        self.img = kwargs['img']
        self.dist = kwargs['dist']
        self.xy = kwargs['xy']

def calculate_coordinates(r,avatars):
    n = len(avatars)
    alpha = round(2*np.pi/n)
    for i,avatar in enumerate(avatars):
        angle = i*alpha
        r_hat = r*avatar.dist
        x = r_hat*np.cos(angle).item()
        y = r_hat*np.sin(angle).item()
        avatar.xy = (x,y)
    return None

#define dummy database
friends = set()
friends.add(Avatar(name = "Gesù", surname = "Di Nazaret", nickname = "Jesoo", img = "./img/jesus.png", dist = min_dist, xy = None))
friends.add(Avatar(name = "Teresa", surname = "Raft", nickname = "Teresa", img = "./img/teresa.png", dist = min_dist, xy = None))
friends.add(Avatar(name = "Katrina", surname = "Klösel", nickname = "Kati", img = "./img/koala.png", dist = min_dist, xy = None))

calculate_coordinates(r,friends)
#-------------------------------------------------------------------------------------------------------------------------------------------------

class PopGridLayout(GridLayout):
    pass

class AvatarPopup(Popup):
    def __init__(self, avatar, **kwargs):
        super(AvatarPopup, self).__init__(**kwargs)
        self.avatar = avatar
    
        show = PopGridLayout()
        pop = Popup(content = show)
        content = self.avatar.img
    
class ImageButton(ButtonBehavior, Image):
    def __init__(self, avatar, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.avatar = avatar
        
    def on_press(self):
        #print("Bau")
        pops = AvatarPopup(self.avatar)
        pops.open()
        pops.title = self.avatar.nickname
        
        
    

class FloatLayoutCircle(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for j,friend in enumerate(friends):
                    size = 40
                    b = ImageButton(source = friend.img,  pos_hint={'x':0.5+friend.xy[0], 'y':0.5+friend.xy[1]}, size_hint = (None,None),size = (dp(size),dp(size)),avatar = friend)
                    self.add_widget(b)
        

#class MainWidget(Widget):
#   pass

class CircleApp(App):
    pass

CircleApp().run()
