from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class _BoxLayout(BoxLayout):
	def __init__(self, **kwargs):
		super(_BoxLayout, self).__init__(**kwargs)
		with self.canvas.before:
		    Color(0.878, 0.941, 0.784)
		    self.rect = Rectangle(size=self.size, pos=self.pos)
		self.bind(size=self._update_rect, pos=self._update_rect)

	def _update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size

class KaliteUI(object):
	def __init__(self, kaliteApp):
		self.root_layout = GridLayout(cols=1)
		logo_houlder = _BoxLayout(orientation='horizontal')
		log_img = Image(source='horizontal-logo.png')
		#log_img.pos_hint={'center_x': 0.1, 'center_y': .5}
		logo_houlder.padding = [20,10,Window.width-250,0]
		logo_houlder.add_widget(log_img)

		self.root_layout.add_widget(logo_houlder)

		#create BubbleButtons
		btn1= Button(text='OpenBrowser', font_size=30
		    , color=(0.14, 0.23, 0.25, 1), bold=True)
		btn1.background_normal='green_button_up.png'
		#btn1.background_down='button_down.png'
		btn1.bind(on_press=kaliteApp.start_webview_bubblebutton)

		btn2= Button(text='Exit', font_size=30
		    , color=(0.14, 0.23, 0.25, 1), bold=True)
		btn2.background_normal='green_button_up.png'
		#btn2.background_down='button_down.png'
		btn2.bind(on_press=kaliteApp.quit_app)

		btn3= Button(text='thread', font_size=30
		    , color=(0.14, 0.23, 0.25, 1), bold=True)
		btn3.background_normal='green_button_up.png'
		#btn3.background_down='button_down.png'
		btn3.bind(on_press=kaliteApp.set_thread_num)

		btn4= Button(text='StopServer', font_size=30
		    , color=(0.14, 0.23, 0.25, 1), bold=True)
		btn4.background_normal='green_button_up.png'
		btn4.bind(on_press=kaliteApp.stop_server)

		btn5= Button(text='StartServer', font_size=30
		    , color=(0.14, 0.23, 0.25, 1), bold=True)
		btn5.background_normal='green_button_up.png'
		btn5.bind(on_press=kaliteApp.start_server)

		#Add items to bubble
		buttons_holder = _BoxLayout(orientation='horizontal')
		buttons_holder.padding = [10,0,10,0]
		buttons_holder.add_widget(btn1)
		buttons_holder.add_widget(btn2)
		buttons_holder.add_widget(btn3)
		buttons_holder.add_widget(btn4)
		buttons_holder.add_widget(btn5)

		self.root_layout.add_widget(buttons_holder)

		#image stuff
		self.img_holder = BoxLayout(orientation='vertical', size=(200,200), size_hint=(1, None))
		self.img_holder.padding = [0,80,0,10]
		self.root_layout.add_widget(self.img_holder)

		#thread input box
		text_input_holder = BoxLayout(orientation='horizontal')
		text_input_holder.padding = [200,10,200,10]

		self.text_input = TextInput(multiline=False, 
		    hint_text="Enter number of threads here:")
		self.text_input.padding = [10,10,10,10]
		text_input_holder.add_widget(self.text_input)

		self.progress_bar = ProgressBar()

		self.server_box = BoxLayout(orientation='horizontal')
		self.messages = BoxLayout(orientation='vertical')

		self.root_layout.add_widget(self.messages)
		self.root_layout.add_widget(self.server_box)
		self.root_layout.add_widget(text_input_holder)
		self.root_layout.add_widget(self.progress_bar)

	def get_root_Layout(self):
		return self.root_layout

	def add_messages(self, message):
		self.messages.add_widget(message)

	def remove_messages(self, message):
		self.messages.remove_widget(message)

	def add_loading_gif(self):
		self.gif_img = Image(source='loading.zip',  anim_delay = 0.15)
		#self.gif_img = Image(source='horizontal-logo.png')
		self.img_holder.add_widget(self.gif_img)

	def remove_loading_gif(self):
		self.img_holder.remove_widget(self.gif_img)

	def get_thread_num(self):
		return 'threads=' + self.text_input.text

	def start_progress_bar(self, anim_value):
		self.anim = Animation(value = anim_value, duration = 1)
		self.anim.start(self.progress_bar)

	def animation_bind(self, bindFunction):
		self.anim.bind(on_complete = bindFunction)


