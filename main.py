from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import TwoLineListItem
from kivy.uix.image import Image
from kivymd.uix.list import MDList
import base64
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton,MDTextButton,MDFlatButton,MDRaisedButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.menu import MDDropdownMenu
import MysqlConnection
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.stencilview import StencilView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivymd.uix.progressbar import MDProgressBar
from io import BytesIO
import random
import math
from MainAlg import Classify_Algorithm
from kivy.metrics import dp
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
import numpy as np
from kivy.graphics import Color,Line
import cv2
# To change the kivy default settings
# we use this module config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
#Config.set('graphics', 'resizable', True)
from image_spliter import reduce_clarity
from kivy.graphics import (Translate, Fbo, ClearColor,
                           ClearBuffers, Scale)
#from Model import Read_Letter,build_model
from PIL import Image as Img
import MainAlg
homescreen=MDScreen()

Letters=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","J","j","K","k","L","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
# Group 1 (a to g)
group1_beginner = ['dog', 'cat', 'hat', 'egg', 'fun', 'game', 'jump', 'kite', 'luck', 'ball', 'doll', 'fish', 'gift', 'hand', 'kite', 'jump', 'lake', 'moon', 'nose', 'park']
group1_intermediate = ['acid', 'dock', 'edge', 'flag', 'gold', 'item', 'jolt', 'king', 'lime', 'mold', 'noise', 'plate', 'quick', 'road', 'sound', 'table', 'uncle', 'virus', 'wagon', 'zebra']
group1_advanced = ['apple', 'badge', 'cedar', 'dodge', 'eager', 'flame', 'gavel', 'habit', 'jumbo', 'kayak', 'label', 'magic', 'noble', 'ozone', 'paddle', 'quirk', 'radar', 'salad', 'tango', 'velvet']

# Group 2 (h to m)
group2_beginner = ['hat', 'ham', 'ice', 'jam', 'key', 'lamp', 'milk', 'nest', 'owl', 'pen', 'quiz', 'rain', 'sock', 'toy', 'van', 'wig', 'yell', 'bank', 'camp', 'desk']
group2_intermediate = ['hedge', 'igloo', 'jolt', 'king', 'lime', 'medal', 'nylon', 'onion', 'pillow', 'quill', 'radar', 'salad', 'tempo', 'uncle', 'violin', 'wagon', 'xenon', 'yodel', 'zealous', 'aroma']
group2_advanced = ['helium', 'insect', 'jigsaw', 'kitten', 'lemon', 'melody', 'nucleus', 'onion', 'piano', 'quartz', 'radar', 'salad', 'tempo', 'unique', 'velvet', 'whiskey', 'xenon', 'yacht', 'zealous', 'aroma']

# Group 3 (n to s)
group3_beginner = ['net', 'oak', 'pen', 'queen', 'rain', 'sun', 'tiger', 'up', 'vest', 'wet', 'bank', 'camp', 'desk', 'elf', 'flag', 'gold', 'home', 'ink', 'joke', 'kiss']
group3_intermediate = ['nylon', 'ocean', 'pillow', 'quill', 'radar', 'salad', 'tempo', 'unique', 'vine', 'whale', 'xenon', 'yodel', 'apple', 'badge', 'cedar', 'dodge', 'eager', 'flame', 'gavel', 'habit']
group3_advanced = ['nephew', 'object', 'paddle', 'quirk', 'radar', 'salad', 'tempo', 'unique', 'vine', 'whale', 'xenon', 'yodel', 'apple', 'badge', 'cedar', 'dodge', 'eager', 'flame', 'gavel', 'habit']

# Group 4 (t to z)
group4_beginner = ['tiger', 'umbrella', 'vase', 'whale', 'xylophone', 'yarn']
group4_intermediate = ['tackle', 'unicorn', 'vivid', 'wander', 'x-ray', 'yacht']
group4_advanced = ['twinkle', 'unique', 'valiant', 'wanderer', 'xylophone', 'yearning']
group = [
    [group1_beginner, group1_intermediate, group1_advanced],
    [group2_beginner, group2_intermediate, group2_advanced],
    [group3_beginner, group3_intermediate, group3_advanced],
    [group4_beginner, group4_intermediate, group4_advanced]
]



tips = [
    "Hold the device with a relaxed and comfortable grip, ensuring a natural and neutral position.",
    "Position the device at a slight angle to allow for smoother movement and better control.",
    "Place your fingers on the device in a tripod grip: thumb, index finger, and middle finger forming a stable tripod shape.",
    "Maintain a light grip on the device to avoid excessive pressure and fatigue.",
    "Keep your wrist relaxed and avoid excessive bending or twisting.",
    "Use your arm and shoulder to move the device rather than relying solely on your fingers.",
    "Practice proper finger placement and spacing for typing on a virtual keyboard, ensuring each finger has a designated area.",
    "When writing big letters, focus on deliberate and controlled movements to maintain consistency and proportion.",
    "Take breaks and stretch your fingers and wrists periodically to prevent fatigue and stiffness.",
    "Adjust the touch sensitivity settings of the device to match your writing style and pressure.",
    "Increase the font size or zoom level on the device to make letters appear larger and easier to read.",
    "Focus on maintaining consistent spacing between each letter to enhance legibility and readability.",
    "Utilize writing aids or apps that provide guidelines or grids to help with letter size and spacing.",
    "Practice handwriting exercises specific to writing on a device to improve dexterity, coordination, and muscle memory."
]








KV_Levels = '''
<Level>
    MDTextField:
        id: lvls
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: "150dp"
        hint_text: "Select Level"
        on_focus: if self.focus: root.dropdown()
'''
KV_Languages =  '''
<Language>:
    MDTextField:
        id: lang
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_x: None
        width: "150dp"
        hint_text: "Select Language"
        on_focus: if self.focus: root.dropdown()
'''
KV_Progress = '''
<Progress>
    MDTextField:
        id: prog
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: "150dp"
        hint_text: "Progress name"
        on_focus: if self.focus: root.dropdown()
'''

KV_Home = '''
#:import SliverToolbar __main__.SliverToolbar


<CardItem>
    size_hint_y: None
    height: "86dp"
    padding: "4dp"
    radius: 12

    FitImage:
        source: root.image_source
        radius: root.radius
        size_hint_x: None
        width: root.height

    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: "6dp"
        padding: "12dp", 0, 0, 0
        pos_hint: {"center_y": .5}

        MDLabel:
            text: root.title_text
            font_style: "H5"
            bold: True
            adaptive_height: True

        MDLabel:
            text: root.subtitle_text
            theme_text_color: "Hint"
            adaptive_height: True


MDScreen:

    MDSliverAppbar:
        id : bar
        background_color: "2e138e"
        toolbar_cls: SliverToolbar()

        MDSliverAppbarHeader:

            MDRelativeLayout:

                FitImage:
                    source: "background.jpg"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True
'''


        
        

class User():
    name=''
    password=''
    id=-1
    def __init__(self):
        pass

    def Set(self, user, pas,id):
        self.name = user
        self.password = pas
        self.id=id

connected= User()
class Prog():
    def __init__(self):
        pass
    def __init__(self,id,name,language,level,LW):
        self.id=id
        self.name=name
        self.language=language
        self.level=level
        self.LorW=LW
        self.group_num=0


current_progress=Prog('','','','','')
class MyPopUp(Popup):
    pass



flag=MysqlConnection.get_Theme()


def fbo_to_ndarray(fbo):
    # Ensure that the FBO is already rendered
    fbo.ask_update()

    # Get the texture from the FBO
    texture = fbo.texture

    # Read the pixels from the texture as a byte string
    pixels = texture.pixels

    # Create a NumPy ndarray from the byte string
    image_array = np.frombuffer(pixels, dtype=np.uint8)

    # Reshape the ndarray to match the dimensions of the texture
    width, height = texture.size
    image_array = image_array.reshape((height, width, 4))

    return image_array

class WritingArea(StencilView):
   
    def __init__(self, **kwargs):
        super(WritingArea, self).__init__(**kwargs)
        global flag

        # Add widgets to the GridLayout
        

        # Add horizontal lines
        with self.canvas.before:
            Color(0, 0, 0)  # Set line color (red in this example)
            self.lines = []
            pattern = [2, 4] 
            for i in range(4):
                if flag==False:
                    Color(0.2, 0.2, 0.2, 1)
                else:
                    Color(0.8, 0.8, 0.8, 1)
                line = Line(points=(0, 0, 0, 0),dash_offset=60, dash_length=20, width=1)  # Set line properties
                self.lines.append(line)
            
            self.border = Line(points=(0, 0, 0, 0), width=2)

        self.bind(pos=self.update_lines, size=self.update_lines)
        self.bind(pos=self.update_border, size=self.update_border)

    def update_lines(self, *args):
        # Update the lines' positions whenever the GridLayout's position or size changes
        line_height1 = self.height / 2
        self.lines[0].points = (self.x, self.y +  self.height / 5, self.x + self.width, self.y +  self.height / 5)
        self.lines[1].points = (self.x, self.y +2* self.height / 5, self.x + self.width, self.y +  2*self.height / 5)
        self.lines[2].points = (self.x, self.y + 3* self.height / 5, self.x + self.width, self.y +3* self.height / 5)
        self.lines[3].points = (self.x, self.y + 4 * self.height / 5, self.x + self.width, self.y + 4 * self.height / 5)
    
    def update_border(self, *args):
        self.border.points = (self.x, self.y, self.x + self.width, self.y, self.x + self.width, self.y + self.height,
                              self.x, self.y + self.height, self.x, self.y)
    

    def on_touch_down(self,touch):
         with self.canvas:
             global flag
             
             if flag==False:
                 Color(0,0,0)
             else:
                 Color(1,1,1)   
             touch.ud['line']=Line(points=(touch.x,touch.y),width=self.size[1]/30)
             if not self.collide_point(*touch.pos):
                 return

    def on_touch_move(self,touch):
        touch.ud['line'].points+=[touch.x,touch.y]
        if not self.collide_point(*touch.pos):
                 return
    def export_scaled_png(self, filename, image_scale=1):
        re_size = (self.width * image_scale, 
                self.height * image_scale)

        if self.parent is not None:
            canvas_parent_index = self.parent.canvas.indexof(self.canvas)
            if canvas_parent_index > -1:
                self.parent.canvas.remove(self.canvas)

        fbo = Fbo(size=re_size, with_stencilbuffer=True)

        with fbo:
            
            global flag
            if flag==False :
                ClearColor(1, 1, 1, 0)
            else:
                ClearColor(0, 0, 0, 0)

            ClearBuffers()
            Scale(image_scale, -image_scale, image_scale)
            Translate(-self.x, -self.y - self.height, 0)

        fbo.add(self.canvas)
        fbo.draw()
        #fbo.texture.save(filename, flipped=False)
        fbo.remove(self.canvas)
        

        if self.parent is not None and canvas_parent_index > -1:
            self.parent.canvas.insert(canvas_parent_index, self.canvas)
        return fbo




class Navigation(MDBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.nav= MDBottomNavigation(
                    MDBottomNavigationItem(
                        app.Home_Page,
                        name='Home',
                        text='Home',
                        icon='home',
                    ),
                    MDBottomNavigationItem(
                        app.New_Page,
                        name='New',
                        text='New',
                        icon='plus',
                    ),
                    MDBottomNavigationItem(
                        app.Board_Page,
                        name='Board',
                        text='Continue',
                        icon='play',
                    ),
                    MDBottomNavigationItem(
                        app.Progress_Page,
                        name='Progress',
                        text='Progress',
                        icon='chart-line',

                    ),
                    
                )
        self.nav.text_color_active=(0, 0, 1, 1)
                    
                    
                    
                
        self.Settings=MDBottomNavigationItem(
                        app.Settings_Page,
                        name='Settings',
                        text='Settings',
                        icon='cog',

                    )
        
        self.nav.add_widget(self.Settings)
        self.add_widget(self.nav)
            




class Create_Screen(MDFloatLayout):
    def __init__(self):
        super().__init__()
        self.login_label = MDLabel(
            text=" Create account ",
            pos_hint={'center_x': 0.65, 'center_y': 0.9},
            theme_text_color="Primary",
            font_style="H4"

        )
        self.add_widget(self.login_label)
        # Username input
        self.username_input = MDTextField(
            hint_text="Username",
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            size_hint=(0.7, 0.1)
        )
        self.add_widget(self.username_input)

        # Password input
        self.password_input = MDTextField(
            hint_text="Password",
            pos_hint={'center_x': 0.5, 'center_y': 0.675},
            size_hint=(0.7, 0.1),
            password=True
        )
        self.add_widget(self.password_input)

        self.password_input1 = MDTextField(
            hint_text="Rewrite password ",
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.7, 0.1),
            password=True
        )
        self.add_widget(self.password_input1)

         # Username input
        self.mail = MDTextField(
            hint_text="Mail",
            pos_hint={'center_x': 0.5, 'center_y': 0.425},
            size_hint=(0.7, 0.1)
        )
        self.add_widget(self.mail)

        # create account button
        create_account_button = MDRectangleFlatButton(
            text="create account",
            pos_hint={'center_x': 0.7, 'center_y': 0.3},
            size_hint=(0.4, 0.1)
        )
        create_account_button.bind(on_press=self.create_account)
        self.add_widget(create_account_button)
        back = MDRectangleFlatButton(
            text="back",
            pos_hint={'center_x': 0.3, 'center_y': 0.3},
            size_hint=(0.2, 0.1)
        )
        back.bind(on_press=self.backpage)
        self.add_widget(back)
        self.error_lbel=MDLabel(text="", halign="center",
            theme_text_color="Error",pos_hint={'center_x': 0.5, 'center_y': 0.15})
        self.add_widget(self.error_lbel)
    
    def backpage(self,instance):
        app.ScreenManager.current="Login"

    def create_account(self,instance):
        if self.username_input.text=="" or self.password_input.text=="" or self.mail.text=="":
            self.error_lbel.text="One or more of the inputs are missing "
        elif self.password_input.text!=self.password_input1.text:
             self.error_lbel.text="Passwords do not match, please check again "   
        else:
            str=MysqlConnection.create_account(self.username_input.text,self.password_input.text,self.mail.text)
            if str=="ok":
                list=MysqlConnection.Log_in_DB(self.username_input.text,self.password_input.text)
                global connected
                connected.Set(list[0][1],list[0][2],list[0][0])
                app.Refresh()
                app.Nav.nav.switch_tab("Home")
                app.ScreenManager.current = "NavigationScreen"
            else:
                self.error_lbel.text=str


class Login_Screen(MDFloatLayout):
    def __init__(self):
        super().__init__()
        self.login_label = MDLabel(
            text=" Log-in ",
            pos_hint={'center_x': 0.8, 'center_y': 0.9},
            theme_text_color= "Custom",
            text_color=(55/256, 76/256, 172/256, 1),
            font_style="H4"

        )
        self.add_widget(self.login_label)
        # Username input
        self.username_input = MDTextField(
            hint_text="Username",
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            size_hint=(0.7, 0.1)
        )
        self.add_widget(self.username_input)

        # Password input
        self.password_input = MDTextField(
            hint_text="Password",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.7, 0.1),
            password=True
        )
        self.add_widget(self.password_input)
        
        button = MDTextButton(
            text="Forget Password",
            theme_text_color= "Custom",
            text_color =(0, 0, 1, 1),
            pos_hint={"center_x": 0.5, 'center_y':0.4},
            on_release=self.on_forgot_password,
            underline=True
        )
        self.add_widget(button)
        # Login button
        login_button = MDRectangleFlatButton(
            text="Log In",
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            size_hint=(0.4, 0.1)
        )
        login_button.bind(on_press=self.login)
        self.add_widget(login_button)
        

        

    
        # Forgot password button
        forgot_password_button = MDRectangleFlatButton(
            text="Create account",
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            size_hint=(0.4, 0.1)
        )
        forgot_password_button.bind(on_press=self.forgot_pass)
        self.add_widget(forgot_password_button)

        self.error_lbel=MDLabel(text="", halign="center",
            theme_text_color="Error",pos_hint={'center_x': 0.5, 'center_y': 0.05})
        self.add_widget(self.error_lbel)
        
    def on_forgot_password(self, instance):
        # Handle the "Forgot Password?" action here
        MysqlConnection.forgot_Pass(self.username_input.text) 

    def forgot_pass(self,instance):
        app.ScreenManager.current="Create"   

    def login(self, instance):
        if self.username_input.text=="" or self.password_input.text=="":
            self.error_lbel.text="one or more of the inputs are missing "
        else:
            username = self.username_input.text
            password = self.password_input.text
            
        
            if self.authenticate(username, password):
                app.ScreenManager.current = "NavigationScreen"
            else:
                self.username_input.text = ""
                self.password_input.text = ""
                self.username_input.error = True
                self.password_input.error = True

    def authenticate(self, username, password):
        list=MysqlConnection.Log_in_DB(username,password)
        if len(list)==0:
            self.error_lbel.text="invalid username or password"
        elif(list[0][1]==username and list[0][2]==password):
            global connected
            connected.Set(username,password,list[0][0])  
            app.Refresh()
            app.Nav.nav.switch_tab("Home")
            return True
        else :
            return False
      

class CardItem(MDCard):
    image_source = StringProperty()  # Image source for the card
    title_text = StringProperty() # Title text for the card
    subtitle_text = StringProperty()  # Subtitle text for the card

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elevation = 3


class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Home"


class Home_Page(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global counter
        global homescreen


class Language(MDFloatLayout):
    def dropdown(self):
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "English",
                "height":dp(56),
                "on_release": lambda x="English": self.set_language(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Arabic",
                "height":dp(56),
                "on_release": lambda x="Arabic": self.set_language(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Hebrew",
                "height":dp(56),
                "on_release": lambda x="Hebrew": self.set_language(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.lang,
            items=self.menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    Builder.load_string(KV_Languages)

    def set_language(self, text_item):
        self.ids.lang.text = text_item
        self.menu.dismiss()

class Level(MDFloatLayout):
    def __init__(self,page):
        super().__init__()
        self.page=page


    def dropdown(self):
       
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Beginner",
                "height": dp(56),
                "on_release": lambda x="Beginner": self.set_level(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Intermediate",
                "height": dp(56),
                "on_release": lambda x="Intermediate": self.set_level(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Advanced",
                "height": dp(56),
                "on_release": lambda x="Advanced": self.set_level(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.lvls,
            items=self.menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    Builder.load_string(KV_Levels)

    def set_level(self, text_item):
        self.ids.lvls.text = text_item
        self.page.radio_button1.disabled=False
        self.page.radio_button1.active=False
        self.page.radio_button2.disabled=False
        self.page.radio_button2.active=False

        if text_item=="Beginner":
            self.page.radio_button1.active=True
            self.page.radio_button2.disabled=True
        elif text_item=="Advanced":
            self.page.radio_button2.active=True
            self.page.radio_button1.disabled=True
        self.menu.dismiss()

class New_Page(MDFloatLayout):
    def __init__(self):
        super().__init__()
        x=Window.size[1]-(Window.size[0]/5)+14
        self.letters=False
        self.words=False
        parent_layout=MDGridLayout(cols=1)
        name_row=MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        self.progressname_input = MDTextField(
            hint_text="Progress name"
            
        )
        
        name_row.add_widget(MDLabel(text="Enter your progress name",halign="center",theme_text_color="Primary"))
        name_row.add_widget(self.progressname_input)
        
        
        first_row = MDLabel(
            text="New Lesson",
            halign="center",
            theme_text_color="Primary",
            font_style="H4",size_hint_y=None,height=x*0.2
        )
        parent_layout.add_widget(first_row)#############################################################
        parent_layout.add_widget(name_row)
        seconed_row=MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        seconed_row.add_widget(MDLabel(text="Select a language:",halign="center"))
        
        self.spinner1=Language()
        seconed_row.add_widget(self.spinner1)

        parent_layout.add_widget(MDLabel(text="",size_hint_y=None,height=x*0.05))
        parent_layout.add_widget(seconed_row)
        parent_layout.add_widget(MDLabel(text="",size_hint_y=None,height=x*0.05))
        third_row=MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        third_row.add_widget(MDLabel(text="Select a level:",halign="center"))
        self.spinner2 = Level(self)
        third_row.add_widget(self.spinner2)
        parent_layout.add_widget(third_row)
        
        t3grid=MDGridLayout(cols=3,size_hint_y=None,height=x*0.1)
        t3grid.add_widget(MDLabel(text=""))
        box_layout = MDBoxLayout(orientation='horizontal', adaptive_size=True, padding='20dp',size_hint_y=None,height=x*0.1)
        
       
        label1 = MDLabel(text='Letters',halign="center", size_hint=(None, 1), width='80dp')
        self.radio_button1 = MDCheckbox(
             size_hint=(None, None),
            size=(48, 48),
            on_release=self.on_radio_button1
         )
        
        box_layout.add_widget(label1)
        box_layout.add_widget(self.radio_button1)
        
        
        label2 = MDLabel(text="Words",halign="center", size_hint=(None, 1), width='80dp')
        self.radio_button2 = MDCheckbox(
             size_hint=(None, None),
            size=(48, 48),
            on_release=self.on_radio_button2
        )
        
        box_layout.add_widget(label2)
        box_layout.add_widget(self.radio_button2)
        t3grid.add_widget(box_layout)
        t3grid.add_widget(MDLabel(text=""))
        # box_layout.add_widget(layout1)
        # box_layout.add_widget(layout2)
        parent_layout.add_widget(t3grid)
        button_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.07)
        button_row.add_widget(MDLabel(text=""))
        create=MDRectangleFlatButton(text="Create",halign="center")
        button_row.add_widget(create)
        create.bind(on_press=self.create_progress)
        button_row.add_widget(MDLabel(text=""))
        parent_layout.add_widget(MDLabel(size_hint_y=None,height=x*0.1))
        parent_layout.add_widget(button_row)
        self.error_label=MDLabel(text="", halign="center",
            theme_text_color="Error",size_hint_y=None,height=x*0.1)
        parent_layout.add_widget(self.error_label)
        self.add_widget(parent_layout)
        # Add the bottom bar to the page



    def create_progress(self,*args):
        name=self.progressname_input.text
        language=self.spinner1.ids.lang.text
        level=self.spinner2.ids.lvls.text

        global connected, current_progress
        
        
        
        if name=="" or language=="languages" or level=="levels" or (self.letters==False and self.words==False):
            self.error_label.text="one or more of the data is missing"
        elif language!="English":
            self.error_label.text="This language is not available right now"    
        elif self.letters==True and self.words==False:
            
            res=MysqlConnection.create_progress(connected.id,name,language,level,"Letters")
            print("letters")
            if res==None:
                prog=MysqlConnection.get_progress_by_name(connected.id,name)
                current_progress=Prog(prog[0],prog[1],prog[2],prog[3],prog[4])
                app.Refresh()
                app.Nav.nav.switch_tab("Board")
            else:
                self.error_label.text=res

        elif  self.letters==False and self.words==True:
            
            res=MysqlConnection.create_progress(connected.id,name,language,level,"Words")
            print("words")
            if res==None:
                prog=MysqlConnection.get_progress_by_name(connected.id,name)
                current_progress=Prog(prog[0],prog[1],prog[2],prog[3],prog[4])
                app.Refresh()
                app.Nav.nav.switch_tab("Board")
            else:
                self.error_label.text=res
        else:
            self.error_label.text="One or more of the data is missing"

    def on_radio_button1(self, *args):
        self.radio_button2.active = False
        if self.radio_button1.active:
            self.letters=True
            self.words=False
            
    def on_radio_button2(self, *args):
        self.radio_button1.active = False
        if self.radio_button2.active:
            self.words=True 
            self.letters=False
              

        
   



    



class Board_Page(MDFloatLayout):
    def __init__(self):
        super().__init__()
        self.parent_layout=MDGridLayout(cols=1)
        
        self.dod=False
        x=Window.size[1]-(Window.size[0]/5)+14
        self.quizes=MDGridLayout(cols=1,size_hint_y=None,height=x*0.5)
        self.t3grid=MDGridLayout(cols=3,size_hint_y=None,height=x*0.1)
        progresslist=MysqlConnection.get_progresses(connected.id,"ALL")
        print(f"your progress list is {progresslist} \n with the length of {len(progresslist)}")
        if len(progresslist)==0:
            self.parent_layout.add_widget(MDLabel(text="you have no progresses yet, please consider creating a progress before accessing this page .\n you can create a progress at new page ",
                                         theme_text_color="Error",
                                         halign="center",
                                         valign="middle",
                                         font_style="H6",
                                         size_hint_y=None,
            height=x*0.5))
            self.add_widget(self.parent_layout)
        else:
            print("else")
            # First row: Title label
            self.parent_layout.add_widget(MDLabel(text="Continue",
                                            theme_text_color="Primary",
                                            halign="center",
                                            valign="top",
                                            font_style="H4",
                                            size_hint_y=None,
                height=x*0.15))

            # Second row: Progress name label and select box
            second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
            second_row.row_force_default = True
            second_row.row_default_height = x*0.1
            second_row.add_widget(MDLabel(text="Progress name:",theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
            self.spinner =Progress(self,"ALL")
            self.spinner.bind(on_press=self.show_full_page)
            second_row.add_widget(self.spinner)
            self.parent_layout.add_widget(second_row)
            self.add_widget(self.parent_layout)

        


    def Display_Word(self):
        if(current_progress.LorW=="Letters"):
            self.cnt=MysqlConnection.get_counter(current_progress.id)
            self.cntmod=self.cnt%52
            if self.cntmod<len(Letters):
                self.WordLabel.text=f"your {current_progress.LorW[:-1]} is: "+Letters[self.cntmod]
                self.word=Letters[self.cntmod]
        else:
            if current_progress.level=="Beginner":
                wordslist=self.add_lists_of_words(0)
            elif current_progress.level=="Intermediate":
                wordslist=self.add_lists_of_words(1)
            else:
                wordslist=self.add_lists_of_words(2)   
            word=random.sample(wordslist[0],1)
            print(word)
            self.WordLabel.text=f"your {current_progress.LorW[:-1]} is: "+word[0]
            self.word=word[0]       

    def show_full_page(self,text):
        global current_progress
        print("show full page")
        
        x=Window.size[1]-(Window.size[0]/5)+14
        current_progress=Prog(self.spinner.dictionary[text][0],text,self.spinner.dictionary[text][1],self.spinner.dictionary[text][2],self.spinner.dictionary[text][3])
       
        
        self.cnt=MysqlConnection.get_counter(current_progress.id)
        if(self.cnt>=14 and self.cnt <26):
            cra=1
        elif (self.cnt>=26 and self.cnt<38):
            cra=2
        elif self.cnt>=38 and self.cnt<=51:
            cra=3
        elif self.cnt<14:
            cra=0
        else:
            cra=4    
        if self.dod:
            self.parent_layout.remove_widget(self.quizes)
            self.parent_layout.remove_widget(self.t3grid)
        self.quizes.clear_widgets()
        self.t3grid.clear_widgets()
        letters1=["A-G","H-M","N-S","T-Y"]
        gobutton=MDFlatButton(text="start quiz")
        gobutton.bind(on_press=self.start_quiz)   
        for i in range(cra):
            row_layout = MDFloatLayout(height=self.x*0.1)
            
            row_layout.add_widget(MDLabel(text=f" Retake a quiz in group {i+1} (letters:{letters1[i]})",halign="center",pos_hint={'center_x': 0.25, 'center_y': 0.5},size_hint=(0.5, 0.9)))
            
            gobutton=MDRectangleFlatButton(text="Start quiz",halign="center",size_hint_x=0.5,pos_hint={'center_x': 0.8, 'center_y': 0.5})
            
            gobutton.bind(on_press=self.start_quiz) 
            row_layout.add_widget(gobutton)
            
            self.quizes.add_widget(row_layout)
        self.parent_layout.add_widget(self.quizes)
        self.dod=True
        
        self.t3grid.add_widget(MDLabel(text=""))
        continuebutton=MDRectangleFlatButton(text="Continue learning")
        continuebutton.bind(on_press=self.get_progress)
        self.t3grid.add_widget(continuebutton)
        self.t3grid.add_widget(MDLabel(text="")) 
        self.parent_layout.add_widget(self.t3grid)                    
        # wseacv self.add_widget(self.parent_layout)
    
    def start_quiz(self,instance):
        self.cnt=MysqlConnection.get_counter(current_progress.id)
        self.cntmod=self.cnt%52
        current_progress.group_num=int((self.cntmod-3)/10) -1
        if current_progress.group_num==0 or current_progress.group_num==1 or current_progress.group_num==2 or current_progress.group_num==3:
            quizid=MysqlConnection.create_quiz(current_progress.id,current_progress.level,current_progress.group_num)
            Quiz_Page1=Quiz_Page(quizid)
            app.Quizscreen.clear_widgets()
            app.Quizscreen.add_widget(Quiz_Page1)
            app.ScreenManager.current="Quiz"
        else :
            print (f"Error wrong number of group {current_progress.group_num}")
    
    def get_progress(self,instance):

        print(f"get progress with progress {current_progress.name}")
        self.clear_widgets()
        back_button=MDIconButton(icon="keyboard-backspace",pos_hint={'center_x': 0.03, 'center_y': 0.9})
        back_button.bind(on_press=self.back)
        self.add_widget(back_button)
        Continue_label = MDLabel(
            text=" Continue ",
            halign="center",
            theme_text_color="Primary",
            font_style="H4",
        )
        
        parent_layout=MDGridLayout(cols=1)
        parent_layout.add_widget(Continue_label)
        child_layout=MDGridLayout(cols=3)
        self.word=""
        child_layout.add_widget(MDLabel(text=""))
        
        check_button = MDRectangleFlatButton(
            text="Check",
            size_hint_y=None,
            height=70,
            size_hint_x=None,
            width=120
        )
        self.cnt=0
        check_button.bind(on_press=self.Check_function)
        child_layout.add_widget(check_button)
        child_layout.add_widget(MDLabel(text=""))
        
        self.WordLabel=MDLabel(text="",
                                         theme_text_color="Secondary",
                                         halign="center",
                                         font_style="Body1",
                                         size_hint_y=None,
            height=70
            )
        parent_layout.add_widget(self.WordLabel)
        self.continue_page = WritingArea(size=[Window.size[0],Window.size[1]/2])
        parent_layout.add_widget(self.continue_page)
        # Forgot password button
       
        parent_layout.add_widget(child_layout)
        
        self.result_label=MDLabel(
            text="",
            halign="center",
            theme_text_color="Secondary",
            font_style="Body1")
        parent_layout.add_widget(self.result_label)
        parent_layout.add_widget(Builder.load_string(KV_learning_tip))
        self.Display_Word()
        self.add_widget(parent_layout)   


    def back(self,instance):
        self.clear_widgets()
        self.parent_layout=MDGridLayout(cols=1)
        
        self.dod=False
        x=Window.size[1]-(Window.size[0]/5)+14
        self.quizes=MDGridLayout(cols=1,size_hint_y=None,height=x*0.5)
        self.t3grid=MDGridLayout(cols=3,size_hint_y=None,height=x*0.1)
        progresslist=MysqlConnection.get_progresses(connected.id,"ALL")
        parent_layout=MDGridLayout(cols=1)
        self.parent_layout.add_widget(MDLabel(text="Continue",
                                            theme_text_color="Primary",
                                            halign="center",
                                            valign="top",
                                            font_style="H4",
                                            size_hint_y=None,
                height=x*0.15))

            # Second row: Progress name label and select box
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        second_row.row_force_default = True
        second_row.row_default_height = x*0.1
        second_row.add_widget(MDLabel(text="Progress name:",theme_text_color="Secondary",
                                        halign="center",
                                        font_style="Body1"))
        self.spinner =Progress(self,"ALL")
        self.spinner.bind(on_press=self.show_full_page)
        second_row.add_widget(self.spinner)
        self.parent_layout.add_widget(second_row)
        self.add_widget(self.parent_layout)
    

    def Check_function(self,instance):
        global flag
        global current_progress
        image=fbo_to_ndarray(self.continue_page.export_scaled_png("image.png"))
        print(flag)  
        MysqlConnection.write_image_to_blob(image,"image")

        image=MysqlConnection.read_blob_and_convert_to_image()
        
        image= 255-image if flag else image
        image1=255-image
        MysqlConnection.write_image_to_blob(255-image,"image1")
        image=reduce_clarity(255-image,25)
        MysqlConnection.write_image_to_blob(image,"image")


        response= Classify_Algorithm(image,self.word,current_progress.level)
         
        self.result_label.text=response[0]
        
        blob=BytesIO()
        image1=Img.fromarray(image1)
        image1.save(blob, format='PNG')
        blob_value = blob.getvalue()

        MysqlConnection.add_action_to_progress(current_progress.id,self.word,blob_value,response[0],current_progress.name)
        if response[0] =="Good job! No letter mistakes found.":
            MysqlConnection.Counter_INC(current_progress.id)
        blob.close() 
        #MysqlConnection.delete_all_letters()           
        self.continue_page.canvas.clear()
        self.cntmod=MysqlConnection.get_counter(current_progress.id)%52
        if (self.cntmod==14 or self.cntmod==26 or self.cntmod==38 or (self.cntmod==50 and self.cnt!=0)) and response[0] =="Good job! No letter mistakes found." :
           self.dialog=None
           if not self.dialog:
            self.dialog = MDDialog(
                text="its time for a quiz, do you want to test your handwriting?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Primary",
                        on_release=self.cancel_action
                    ),
                    MDFlatButton(
                        text="TEST",
                        theme_text_color="Primary",
                        on_release=self.proceed_action
                    ),
                ],
                radius=[20, 7, 20, 7],
                
            )
            self.dialog.open()
        else:
            self.Display_Word()    
   
    def cancel_action(self, instance):
        self.dialog.dismiss()  # Close the dialog    
        self.Display_Word()

    def proceed_action(self, instance):
        self.cnt=MysqlConnection.get_counter(current_progress.id)
        self.cntmod=self.cnt%52
        self.dialog.dismiss()
        current_progress.group_num=int((self.cntmod-3)/10) -1
        if current_progress.group_num==0 or current_progress.group_num==1 or current_progress.group_num==2 or current_progress.group_num==3:
            quizid=MysqlConnection.create_quiz(current_progress.id,current_progress.level,current_progress.group_num)
            Quiz_Page1=Quiz_Page(quizid)
            app.Quizscreen.clear_widgets()
            app.Quizscreen.add_widget(Quiz_Page1)
            app.ScreenManager.current="Quiz"
            self.Display_Word()
        else :
            print (f"error wrong number of group {current_progress.group_num}")    

    def add_lists_of_words(self,i):
        result_list = []
        for k in range(4):
            result_list.append(group[k][i])
              
        return result_list 
    def show_tip(self):
        tip_text = random.choice(tips)

        dialog = MDDialog(
            text=tip_text,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open() 
KV_learning_tip = '''
BoxLayout:
    orientation: "vertical"

    MDIconButton:
        icon: "information"
        pos_hint: {"left": 1}
        on_release: app.Board_Page.show_tip()

'''   



class Quiz_Page(MDFloatLayout):
    def __init__(self,qid):
        super().__init__()
        self.qid=qid
        self.count=1
        self.rightletters=0
        self.all=0
        self.number=current_progress.group_num
        if current_progress.level=="Beginner":
            self.f5words=self.get_random_words(self.add_lists_of_words(self.number,0))
        elif current_progress.level=="Intermediate":
            self.f5words=self.get_random_words(self.add_lists_of_words(self.number,1))
        else:
            self.f5words=self.get_random_words(self.add_lists_of_words(self.number,2))
        back_button=MDIconButton(icon="keyboard-backspace",pos_hint={'center_x': 0.03, 'center_y': 0.9})
        back_button.bind(on_press=self.back)
        self.add_widget(back_button)    
        parent_layout=MDGridLayout(cols=1)
        x=Window.size[1]-(Window.size[0]/5)+14
        # First row: Title label
        parent_layout.add_widget(MDLabel(text="Quiz",
                                         theme_text_color="Primary",
                                         halign="center",
                                         valign="top",
                                         font_style="H4",
                                         size_hint_y=None,
            height=x*0.15))
        self.progbar=MDProgressBar(value=1,color=(0,0,1,1),size_hint_y=None,height=x*0.009)
        # Second row: Progress name label and select box
        second_row = MDLabel(text=f"Level:{current_progress.level}",font_style="Body1",size_hint_y=None,height=x*0.09)
        self.word=self.f5words[0]
        third_row=MDLabel(text=f"Language:{current_progress.language}",font_style="Body1",size_hint_y=None,height=x*0.09)
        self.forth_row=MDLabel(text=f"your word is :{self.f5words[0]}",font_style="Body1",size_hint_y=None,height=x*0.12)
        self.continue_page=WritingArea(size=[Window.size[0],Window.size[1]/2])
        sixsth_row=MDGridLayout(cols=3)
        sixsth_row.add_widget(MDLabel())
        self.check_button = MDRectangleFlatButton(
            text="Next",
            size_hint_y=None,
            height=70,
            size_hint_x=None,
            width=120
        )
        self.check_button.bind(on_press=self.Check_function)
        sixsth_row.add_widget(self.check_button)
        sixsth_row.add_widget(MDLabel())
        parent_layout.add_widget(self.progbar)
        parent_layout.add_widget(second_row)
        parent_layout.add_widget(third_row)
        parent_layout.add_widget(self.forth_row)
        parent_layout.add_widget(self.continue_page)
        parent_layout.add_widget(sixsth_row)
       
        self.add_widget(parent_layout)

    def back(self,instance):
        self.dialog1=None
        if not self.dialog1:
            self.dialog1 = MDDialog(
            text="Are you sure you want to quit your quiz??",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Primary",
                    on_release=self.cancel_action
                ),
                MDFlatButton(
                    text="Quit",
                    theme_text_color="Primary",
                    on_release=self.proceed_action
                ),
            ],
            radius=[20, 7, 20, 7],
            
        )
        self.dialog1.open()
    def  cancel_action(self,instnce):
        self.dialog1.dismiss()
    def  proceed_action(self,instance):
        self.dialog1.dismiss()
        app.Nav.nav.switch_tab("Board")
        MysqlConnection.delete_incomplete_quizes(self.qid)
        MysqlConnection.delete_all_letters()
        app.ScreenManager.current = "NavigationScreen"

    def add_lists_of_words(self,i,j):
        result_list = []
        for k in range(i+1):
            result_list.append(group[k][j])
            print(f"group {k} {j} is : {group[k][j]}")  # Add the word_list to the result_list
        return result_list


    def Display_Word(self):
        self.continue_page.canvas.clear()
        self.progbar.value=self.count*20
        self.forth_row.text=f"Your word is :{self.f5words[self.count]}"
        print(self.forth_row.text)
        self.word=self.f5words[self.count]
        self.count=self.count+1     
        if self.count==4:
            self.check_button.text="Submit"

        
            

    def get_random_words(self,word_list):
        try:
            print(f"the world list is : {word_list}")
            random_words = random.sample(word_list[0], 5)
            return random_words 
        except ValueError as ve:
            print(ve) 
            return["error"]
             


    

    def Check_function(self,instance):
        global flag
        global current_progress
        image=fbo_to_ndarray(self.continue_page.export_scaled_png("image.png"))
        print(flag)  
        MysqlConnection.write_image_to_blob(image,"image")

        image=MysqlConnection.read_blob_and_convert_to_image()
        image= 255-image if flag else image
        image1=255-image
        MysqlConnection.write_image_to_blob(255-image,"image1")
        image=reduce_clarity(255-image,25)
        MysqlConnection.write_image_to_blob(image,"image")

        
        response= Classify_Algorithm(image,self.word,current_progress.level)
        self.all=self.all+len(self.word)
        allresponse=""
        for respon in response:
            allresponse=f"{allresponse} {respon}"
            if respon=="Good job! No letter mistakes found.":
                self.rightletters=self.rightletters+1
                print(self.rightletters)
                
           
        blob=BytesIO()
        image1=Img.fromarray(image1)
        image1.save(blob, format='PNG')
        blob_value = blob.getvalue()
                                                                #progressid, quizid, LorW, image, feedback
        MysqlConnection.add_action_to_quiz(current_progress.id,self.qid,self.word,blob_value,allresponse)
        blob.close()            
        MysqlConnection.delete_all_letters()
        if self.count<5:
            self.Display_Word()
        else:
            self.grade=math.ceil((self.rightletters/self.all)*100)
            self.dialog=None
            if not self.dialog:
                self.dialog = MDDialog(
                    text=f"Congratulations, you have completed the quiz you got {self.rightletters} letters right out of {self.all} your grade is : {self.grade}",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Primary",
                            on_release=self.save_quiz
                        ),
                        
                    ],
                    radius=[20, 7, 20, 7],
                    
                )
                self.dialog.open()
            
    
    
    def save_quiz(self,instance):
        MysqlConnection.save_quiz_grade(self.qid,self.grade)
        self.dialog.dismiss()
        app.Nav.nav.switch_tab("Board")
        app.ScreenManager.current = "NavigationScreen"
        

        


class Progress(MDFloatLayout):

    def __init__(self,page,LW):
        super().__init__()
        self.page=page
        self.LW=LW
        if connected.id != -1:
            progresslist=MysqlConnection.get_progresses(connected.id,self.LW)
            self.dictionary = {row[1]: (row[0],row[2],row[3],row[4]) for row in progresslist}# Progress dictionary {name:(id,language,level,LW)}
            self.list = [str(row[1]) for row in progresslist]
            self.progress_list = self.list




    def dropdown(self):
        if connected.id != -1:
            progresslist=MysqlConnection.get_progresses(connected.id,self.LW)
            self.dictionary = {row[1]: (row[0],row[2],row[3],row[4]) for row in progresslist}# Progress dictionary {name:(id,language,level,LW)}
            self.list = [str(row[1]) for row in progresslist]
            self.progress_list = self.list
        
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": progress_item,
                "height": dp(56),
                "on_release": lambda x=progress_item: self.set_progress(x),
            } for progress_item in self.progress_list
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.prog,
            items=self.menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()
    

    
    

    Builder.load_string(KV_Progress)
    

 
        

    def set_progress(self, text_item):
        self.ids.prog.text = text_item
        
        self.menu.dismiss()
        if isinstance(self.page, Progress_Page) :
            if self.LW!="Graph":
                self.page.show_selected_value(text_item)
                #current_progress=Prog(self.page.spinner.dictionary[text_item][0],text_item,self.page.spinner.dictionary[text_item][1],self.page.spinner.dictionary[text_item][2],self.page.spinner.dictionary[text_item][3])
        if isinstance(self.page, Board_Page):
            self.page.show_full_page(text_item)    



class CustomSwiperItem(MDSwiperItem):
    def __init__(self, image_path, Page,label):
        super().__init__()
        self.size=(600,600)
        self.label=label
        self.Page=Page
        self.img=image_path
        self.parent_layout=MDGridLayout(cols=1)
        x=Window.size[1]-(Window.size[0]/5)+14
        self.third_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.5)
        self.add_widget(Image(source=image_path))
        self.add_widget(MDLabel(text=self.label))
        
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
           print(self.Page.spinner.ids.prog.text)
           if self.Page.spinner.ids.prog.text not in self.Page.spinner.dictionary.keys():
               self.Page.error_lbel.text="Please select a Progress"
               return 
           if self.label=="Learning Progress":
                self.Page.Go_to_Progress()

           elif self.label=="Quizzes Actions":
                self.Page.Go_to_Quizes()
           else:
                self.Page.Go_to_Graph()





KV_progress_tip = '''
BoxLayout:
    orientation: "vertical"

    MDIconButton:
        icon: "information"
        pos_hint: {"left": 1}
        on_release: app.Progress_Page.show_tip()

'''              
      



class Progress_Page(MDFloatLayout):
    def __init__(self):
        super().__init__()
        
        
        self.parent_layout=MDGridLayout(cols=1)

        x=Window.size[1]-(Window.size[0]/5)+14

        self.third_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.5)
        # First row: Title label
        self.parent_layout.add_widget(MDLabel(text="Progress",
                                        theme_text_color="Primary",
                                        halign="center",
                                        valign="top",
                                        font_style="H4",
                                        size_hint_y=None,
            height=x*0.15))
        # Second row: Progress name label and select box
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        second_row.row_force_default = True
        second_row.row_default_height = x*0.1

        self.lbl=MDLabel(text="Progress name:",theme_text_color="Secondary",
                                        halign="center",
                                        font_style="Body1")
        self.img = MysqlConnection.read_blob_and_convert_to_graph()
        second_row.add_widget(self.lbl)
        self.spinner =Progress(self,"ALL")
        self.spinner.bind(on_press=self.show_selected_value)
        second_row.add_widget(self.spinner)
        self.parent_layout.add_widget(second_row)
        
        #toolbar =  Builder.load_string(KV_sliver_App_bar)
        swiper = MDSwiper()
        self.Graph=CustomSwiperItem("Graph.jpg",self,"Quiz Graph")
        self.Quizes=CustomSwiperItem("Quiz.png",self,"Quizzes Actions")
        self.Letters=CustomSwiperItem("letter.jpg",self,"Learning Progress")
        swiper.add_widget(self.Graph)
        swiper.add_widget(self.Quizes)
        swiper.add_widget(self.Letters)
        
        self.parent_layout.add_widget(swiper)
        self.error_lbel=MDLabel(text="", halign="center",
            theme_text_color="Error",pos_hint={'center_x': 0.5, 'center_y': 0.15})
        

        self.parent_layout.add_widget(self.error_lbel)
        self.parent_layout.add_widget(Builder.load_string(KV_progress_tip))
        self.add_widget(self.parent_layout)

  
        #self.add_widget(toolbar)

      

    def show_tip(self):
        tip_text = 'Quiz Graph: Visualize progress for a graphical representation of learning.\nQuizzes Actions: Track actions and progress made in quizzes.\nProgress: Monitor learning actions and progress.'

        dialog = MDDialog(
            text=tip_text,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_selected_value(self, text):
        global current_progress
        current_progress=Prog(self.spinner.dictionary[text][0],text,self.spinner.dictionary[text][1],self.spinner.dictionary[text][2],self.spinner.dictionary[text][3])
       
       

    def on_item_release(self, item):
        parent = item.parent

        row_number = len(parent.children)-parent.children.index(item)-1
        action_ids=list(self.ImageDictionary.keys())
        row_data=(item.text,item.secondary_text)
        print(row_number)
        self.open_popup(action_ids[row_number],row_data,"progress")
    
    
    def on_item_release_quiz(self, item):
        parent = item.parent
        row_number = len(parent.children)-parent.children.index(item)-1
        quiz_ids=list(self.QuizDictionary.keys())
        row_data=(item.text,item.secondary_text)
        print(row_number)
        self.open_popup(quiz_ids[row_number],row_data,"quiz")

   
    def Go_to_Progress(self):
        self.clear_widgets()
        self.parent_layout.clear_widgets()
        self.third_row.clear_widgets()
        self.parent_layout=MDGridLayout(cols=1)
        x=Window.size[1]-(Window.size[0]/5)+14
        # First row: Title label
        
        self.parent_layout.add_widget(MDLabel(text="Learning Progress",
                                        theme_text_color="Primary",
                                        halign="center",
                                        valign="top",
                                        font_style="H4",
                                        size_hint_y=None,
            height=x*0.15))

        # Second row: Progress name label and select box
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        Action_list=MysqlConnection.get_Actions_by_id(int(self.spinner.dictionary[current_progress.name][0])) 
        if not Action_list:
            second_row.add_widget(MDLabel(text="The Progress "+current_progress.name+" is still empty",theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
            self.parent_layout.add_widget(second_row)
            button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        
        
            button.bind(on_press=self.back_ro_main_progress)
            self.parent_layout.add_widget(button)
            self.add_widget(self.parent_layout)
            return
        second_row.add_widget(MDLabel(text="Progress Name : "+current_progress.name,theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
        self.parent_layout.add_widget(second_row)
        
        self.third_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.5)
        self.third_row.add_widget(MDLabel(size_hint_x=None,width=Window.size[0]*0.1,size_hint_y=None,
            height=x*0.8))
        self.list=MDList(
                    id="container"
                )
        self.scroll=MDScrollView(self.list)

         

        self.ImageDictionary = {row[3]: row[0] for row in Action_list}
        self.Row_data=[(row[1], row[2]) for row in Action_list]
        self.list.clear_widgets()
        for row in self.Row_data:
            self.list.add_widget(
            TwoLineListItem(text=row[0],
                            secondary_text= row[1],
                            on_release=self.on_item_release
                            ))
        self.third_row.add_widget(self.scroll)
        self.third_row.add_widget(MDLabel(size_hint_x=None,width=Window.size[0]*0.1,size_hint_y=None,
            height=x*0.5))
        

        # Fourth row: Empty label
        button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        button.bind(on_press=self.back_ro_main_progress)
        self.parent_layout.add_widget(button)
        self.parent_layout.add_widget(self.third_row)
        
    
        self.add_widget(self.parent_layout)




    def Go_to_Graph(self):
        lbl=self.lbl.text
        self.clear_widgets()
        self.parent_layout.clear_widgets()

        self.third_row.clear_widgets()
        self.parent_layout=MDGridLayout(cols=1)
        x=Window.size[1]-(Window.size[0]/5)+14
        # First row: Title label
        
        self.parent_layout.add_widget(MDLabel(text="Graph",
                                        theme_text_color="Primary",
                                        halign="center",
                                        valign="top",
                                        font_style="H4",
                                        size_hint_y=None,
            height=x*0.15))
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        second_row.row_force_default = True
        second_row.row_default_height = x*0.1
        if not MainAlg.Make_Charts(current_progress.id,current_progress.name):
            second_row.add_widget(MDLabel(text="The Progress "+current_progress.name+" is still empty",theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
            self.parent_layout.add_widget(second_row)
            button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        
        
            button.bind(on_press=self.back_ro_main_progress)
            self.parent_layout.add_widget(button)
            self.add_widget(self.parent_layout)
            return
        # Second row: Progress name label and select box
        
        second_row.add_widget(MDLabel(text="Progress Name: "+current_progress.name,theme_text_color="Secondary",
                                        halign="center",
                                        font_style="Body1"))
        self.parent_layout.add_widget(second_row)
        print(current_progress.id,current_progress.name)
        
        self.img=MysqlConnection.read_blob_and_convert_to_graph()
        

        #img.allow_stretch = True

        self.third_row.add_widget(MDBoxLayout(self.img))
        
        # Fourth row: Empty label
        button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        self.parent_layout.add_widget(button)

        button.bind(on_press=self.back_ro_main_progress)
        self.parent_layout.add_widget(self.third_row)
        self.add_widget(self.parent_layout)


    
    def Go_to_Quizes(self):
        self.clear_widgets()
        self.parent_layout.clear_widgets()
        self.third_row.clear_widgets()
        self.parent_layout=MDGridLayout(cols=1)
        x=Window.size[1]-(Window.size[0]/5)+14
        # First row: Title label
        
        self.parent_layout.add_widget(MDLabel(text="Quizzes Actions",
                                        theme_text_color="Primary",
                                        halign="center",
                                        valign="top",
                                        font_style="H4",
                                        size_hint_y=None,
            height=x*0.15))

        # Second row: Progress name label and select box
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        second_row.row_force_default = True
        second_row.row_default_height = x*0.1
        Quiz_list=MysqlConnection.get_Quiz_Actions(current_progress.id)  
        if not Quiz_list:
            second_row.add_widget(MDLabel(text="The Progress "+current_progress.name+" is still empty",theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
            self.parent_layout.add_widget(second_row)
            button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        
        
            button.bind(on_press=self.back_ro_main_progress)
            self.parent_layout.add_widget(button)
            self.add_widget(self.parent_layout)
            return
        second_row.add_widget(MDLabel(text="Progress Name : "+current_progress.name,theme_text_color="Secondary",
                                            halign="center",
                                            font_style="Body1"))
        self.parent_layout.add_widget(second_row)

        
        
        self.third_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.5)
        self.third_row.add_widget(MDLabel(size_hint_x=None,width=Window.size[0]*0.1,size_hint_y=None,
            height=x*0.8))
        self.list=MDList(
                    id="container"
                )
        self.scroll=MDScrollView(self.list)

        
        self.QuizDictionary = {row[0]: (row[2],row[3],row[4]) for row in Quiz_list}
        Quiz_Image_list=MysqlConnection.get_Quiz_Actions_imgs(current_progress.id)
        self.Quiz_Image_list = list(map(lambda x: x[0], Quiz_Image_list))
        self.QuizImages={row[0]: value[0] for row, value in zip(Quiz_list, Quiz_Image_list)}
        self.Row_data=[(row[3], row[4]) for row in Quiz_list]
        self.list.clear_widgets()
        for row in self.Row_data:          
            self.list.add_widget(
            TwoLineListItem(text=str(row[0]),
                            secondary_text= str(row[1]),
                            on_release=self.on_item_release_quiz
                            ))
        self.third_row.add_widget(self.scroll)
        self.third_row.add_widget(MDLabel(size_hint_x=None,width=Window.size[0]*0.1,size_hint_y=None,
            height=x*0.5))
        button=MDIconButton(icon='keyboard-backspace', size_hint_x=None, icon_size=100)
        
        
        button.bind(on_press=self.back_ro_main_progress)
        self.parent_layout.add_widget(button)
        self.parent_layout.add_widget(self.third_row)
        # Fourth row: Empty label
        
    
        self.add_widget(self.parent_layout)
           
    def back_ro_main_progress(self,instance):
        self.clear_widgets()
        self.img = Image(source = 'chart.jpg')
        self.parent_layout=MDGridLayout(cols=1)

        x=Window.size[1]-(Window.size[0]/5)+14

        self.third_row=MDGridLayout(cols=3,size_hint_y=None,height=x*0.5)
        # First row: Title label
        self.parent_layout.add_widget(MDLabel(text="Progress",
                                        theme_text_color="Primary",
                                        halign="center",
                                        valign="top",
                                        font_style="H4",
                                        size_hint_y=None,
            height=x*0.15))
        # Second row: Progress name label and select box
        second_row = MDGridLayout(cols=2,size_hint_y=None,height=x*0.1)
        second_row.row_force_default = True
        second_row.row_default_height = x*0.1

        self.lbl=MDLabel(text="Progress name:",theme_text_color="Secondary",
                                        halign="center",
                                        font_style="Body1")
        
        second_row.add_widget(self.lbl)
        self.spinner =Progress(self,"ALL")
        self.spinner.bind(on_press=self.show_selected_value)
        second_row.add_widget(self.spinner)
        self.parent_layout.add_widget(second_row)
        
        #toolbar =  Builder.load_string(KV_sliver_App_bar)
        swiper = MDSwiper()
        self.Graph=CustomSwiperItem("Graph.jpg",self,"Quiz Graph")
        self.Quizes=CustomSwiperItem("Quiz.png",self,"Quizzes Actions")
        self.Letters=CustomSwiperItem("letter.jpg",self,"Learning Progress")
        swiper.add_widget(self.Graph)
        swiper.add_widget(self.Quizes)
        swiper.add_widget(self.Letters)
        
        self.parent_layout.add_widget(swiper)
        self.spinner.ids.prog.text=current_progress.name
        self.error_lbel.text=""
        self.parent_layout.add_widget(self.error_lbel)
        self.parent_layout.add_widget(Builder.load_string(KV_progress_tip))

        self.add_widget(self.parent_layout)


    def open_popup(self,Id,lw,type):
        # Create an instance of the custom pop-up class
        self.popup = MyPopUp(title=f'{lw[0]} : {lw[1]}')
        
        layout = MDBoxLayout(orientation='vertical')
        if type=="progress":
            stream = self.ImageDictionary[Id]
        else:
            
            stream = self.QuizImages[Id]    

        data = BytesIO(stream)
        img = CoreImage(data, ext="png").texture

        widget = Image(source = 'a.jpg')
        widget.texture = img
        widget.allow_stretch = True
        widget.size_hint = (1, 1)
        
        button=MDIconButton(icon='arrow-left-bold', size_hint_x=None, icon_size=100)
        button.bind(on_press=self.back)
        

        
        layout.add_widget(widget)
        layout.add_widget(button)
        # Set the Image widget as the content of the pop-up
        self.popup.content = layout

        # Open the pop-up
        self.popup.open()

    def back(self,instance):
        self.popup.dismiss()




class Settings_Page(MDFloatLayout):
    def __init__(self):
        self.dialog=None
        super().__init__()
        global flag
        
        x=900
        layout = MDGridLayout(cols=1)
        
        # Create labels
        
       


        layout.add_widget(MDLabel(text="Settings",
                                         theme_text_color="Primary",
                                         halign="center",
                                         valign="top",
                                         font_style="H4",
                                         size_hint_y=None,
            height=x*0.15))
       
        
        label3 = MDLabel(text="Enjoy your learning")
        ################
        box_layout = MDBoxLayout(orientation='horizontal', adaptive_size=True, padding='20dp')
        
        label = MDLabel(text='Dark theme', size_hint=(None, 1), width='100dp')
        switch = MDSwitch(active=flag,size_hint=(None, 1), width='48dp',thumb_color_inactive=(0.7,0.7,0.7,1))
        
        switch.bind(active=self.on_switch_active)
        box_layout.add_widget(label)
        box_layout.add_widget(switch)
        #################
        layout.add_widget(box_layout)
        
        self.logout=MDRectangleFlatButton(text="Log out",size_hint_y=None,height=x*0.1)
        self.logout.bind(on_press=self.show_alert_dialog)
        five=MDGridLayout(cols=5)
        for i in range(5):
            if i==2:
                five.add_widget(self.logout)
            else:
                five.add_widget(MDLabel(text=""))
        three=MDGridLayout(cols=3)
        for i in range(5):
            if i==1:
                three.add_widget(label3)
            else:
                three.add_widget(MDLabel(text=""))
        layout.add_widget(three)
        layout.add_widget(five)
        layout.add_widget(MDLabel())
        self.add_widget(layout)
        
       
    def show_alert_dialog(self,instance):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Are you sure you want to log out?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Primary",
                        on_release=self.cancel_action
                    ),
                    MDFlatButton(
                        text="LOGOUT",
                        theme_text_color="Primary",
                        on_release=self.proceed_action
                    ),
                ],
                radius=[20, 7, 20, 7],
                
            )
        self.dialog.open()
   
    def cancel_action(self, instance):
        self.dialog.dismiss()  # Close the dialog    
        
    def proceed_action(self, instance):
        self.dialog.dismiss()
        app.ScreenManager.current="Login"

    def on_switch_active(self, instance, value):
        self.toggle_theme_value()
        if value:
            app.set_dark_theme()
            app.Nav.nav.switch_tab("Settings")

        else:
            app.set_light_theme()
            app.Nav.nav.switch_tab("Settings")


    def toggle_theme_value(self):
        global flag
        flag=not flag 
        MysqlConnection.set_Theme(flag)
        
    


    




class LoginApp(MDApp):
    def build(self):
        global homescreen
        self.ScreenManager=ScreenManager()
        self.theme_cls.primary_palette = "Indigo"
        self.Login_Page=Login_Screen()
        self.Home_Page=Home_Page()
        self.New_Page=New_Page()
        self.Board_Page=Board_Page()
        self.Progress_Page=Progress_Page()
        self.Settings_Page=Settings_Page()
        self.Create_Page=Create_Screen()
        screen=MDScreen(name='Create')
        screen.add_widget(self.Create_Page)
        self.ScreenManager.add_widget(screen)
        homescreen=Builder.load_string(KV_Home)
        self.Home_Page.add_widget(homescreen)
        self.Quizscreen=MDScreen(name='Quiz')
        
        self.ScreenManager.add_widget(self.Quizscreen)
        screen=MDScreen(name='Login')
        screen.add_widget(self.Login_Page)
        self.ScreenManager.add_widget(screen)
        self.ScreenManager.current="Login"
        NavigationScreen=MDScreen(name="NavigationScreen")
        self.Nav=Navigation()
        NavigationScreen.add_widget(self.Nav)
        self.ScreenManager.add_widget(NavigationScreen)


        return self.ScreenManager


    def Refresh(self):
        self.ScreenManager.clear_widgets()
        self.Login_Page=Login_Screen()
        self.Home_Page.clear_widgets()
        self.Home_Page=Home_Page()
        self.Home_Page.add_widget(homescreen)
        self.New_Page=New_Page()
        self.Board_Page=Board_Page()
        self.Progress_Page=Progress_Page()
        self.Settings_Page=Settings_Page()
        screen=MDScreen(name='Login')
        screen.add_widget(self.Login_Page)
        self.ScreenManager.add_widget(screen)
        self.Create_Page=Create_Screen()
        screen=MDScreen(name='Create')
        screen.add_widget(self.Create_Page)
        self.ScreenManager.add_widget(screen)
        self.Quizscreen=MDScreen(name='Quiz')
        self.ScreenManager.add_widget(self.Quizscreen)

        NavigationScreen=MDScreen(name="NavigationScreen")
        self.Nav=Navigation()
        NavigationScreen.add_widget(self.Nav)
        self.ScreenManager.add_widget(NavigationScreen)
        self.ScreenManager.current="NavigationScreen"


    def set_light_theme(self):
        # Set app theme to light mode
        global flag
        self.theme_cls.theme_style = "Light" # White background color
        self.Refresh()
        # self.Refresh(self.Screen_Manager.current)
        


    def set_dark_theme(self):
        # Set app theme to dark mode
        global flag
        self.theme_cls.theme_style = "Dark" 
        self.Refresh()
        #self.Refresh(self.Screen_Manager.current)
        

    

    def on_start(self):
         self.ScreenManager.current="Login"
         
         
         global flag
         if flag==True:
             self.theme_cls.theme_style = "Dark" 

             

         else:
             self.theme_cls.theme_style = "Light"
         card_data =[
            
            {'image_source': 'plus.png','title_text':'New', 'subtitle_text': 'In this page, you can create a new progress with your own options.'},
            {'image_source': 'play.jpg', 'title_text':'Continue','subtitle_text': 'In this page, you can continue with a progress you already created.'},
            {'image_source': 'chart-line.png', 'title_text':'Progress','subtitle_text': 'In this page, you can view your progresses, results, and info.'},
            {'image_source': 'cog.png','title_text':'Settings', 'subtitle_text': 'In this page, you can adjust your own settings for the app.'}
        ]
         for data in card_data:
            card = CardItem()
            card.image_source = data["image_source"]
            card.title_text = data["title_text"]
            card.subtitle_text = data["subtitle_text"]
            homescreen.ids.content.add_widget(card)
             
             
                     
        


if __name__ == "__main__":
    Window.size=(330,650)
    app=LoginApp()
    app.run()


