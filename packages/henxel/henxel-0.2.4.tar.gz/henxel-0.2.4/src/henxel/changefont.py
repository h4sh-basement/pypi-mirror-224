import tkinter.font
import tkinter


class FontChooser:
		
	def __init__(self, master, fontlist, tracefunc=None):
		'''	master		tkinter.Toplevel
			fontlist	list of tkinter.font.Font instances
			tracefunc	callable, used in change_font. It arranges variable
						observer for change on any item in fontlist.
						This is practically same as if there would be virtual
						event <<FontChanged>> and tracefunc binded to it.
		'''
		
		self.top = master
		self.fonts = fontlist
		
		if tracefunc:
			self.tracefunc = tracefunc
		else:
			self.tracefunc = None
		
		self.badfonts = frozenset([
					'Standard Symbols PS',
					'OpenSymbol',
					'Noto Color Emoji',
					'FontAwesome',
					'Dingbats',
					'Droid Sans Fallback',
					'D050000L'
					])
					
		self.fontnames = [f for f in tkinter.font.families() if f not in self.badfonts]
		
		# Remove duplicates then sort
		s = set(self.fontnames)
		self.fontnames = [f for f in s]
		self.fontnames.sort()
		self.max = 42
		self.min = 8
		
		self.option_menu_list = list()

		for font in self.fonts:
			self.option_menu_list.append(font.name)
		
		self.var = tkinter.StringVar()
		self.var.set(self.option_menu_list[0])
		self.font = tkinter.font.nametofont(self.var.get())
		
		self.optionmenu = tkinter.OptionMenu(self.top, self.var, *self.option_menu_list, command=self.optionmenu_command)
		
		# Set font of dropdown button:
		self.optionmenu.config(font=('TkDefaultFont',10))
		
		# Set font of dropdown items:
		menu = self.top.nametowidget(self.optionmenu.menuname)
		menu.config(font=('TkDefaultFont',10))
		
		# Optionmenu contains font-instances to be configured:
		self.optionmenu.pack(side=tkinter.LEFT)
		self.button = tkinter.Button(self.top, text='BIG', command=self.button_command)
		self.button.pack()
		self.scrollbar = tkinter.Scrollbar(self.top)
		
		# Listbox contains font-choises to select from:
		self.lb = tkinter.Listbox(self.top, font=('TkDefaultFont', 10), selectmode=tkinter.SINGLE, width=40, yscrollcommand=self.scrollbar.set)
		self.lb.pack(pady=10, side='left')
		self.scrollbar.pack(side='left', fill='y')
		self.scrollbar.config(width=30, elementborderwidth=4, command=self.lb.yview)
		
		# With spinbox we set font size:
		self.sb = tkinter.Spinbox(self.top, font=('TkDefaultFont', 10), from_=self.min, to=self.max, increment=2, width=3, command=self.change_font)
		self.sb.pack(pady=10)
		
		# Make four checkboxes for other font configurations
		self.bold = tkinter.StringVar()
		self.cb1 = tkinter.Checkbutton(self.top, font=('TkDefaultFont', 10), offvalue='normal', onvalue='bold', text='Bold', variable=self.bold)
		self.cb1.pack(pady=10, anchor='w')
		self.cb1.config(command=lambda args=[self.bold, 'weight']: self.checkbutton_command(args))
		
		self.italic = tkinter.StringVar()
		self.cb2 = tkinter.Checkbutton(self.top, font=('TkDefaultFont', 10), offvalue='roman', onvalue='italic', text='Italic', variable=self.italic)
		self.cb2.pack(pady=10, anchor='w')
		self.cb2.config(command=lambda args=[self.italic, 'slant']: self.checkbutton_command(args))
		
		self.underline = tkinter.StringVar()
		self.cb3 = tkinter.Checkbutton(self.top, font=('TkDefaultFont', 10), offvalue=0, onvalue=1, text='Underline', variable=self.underline)
		self.cb3.pack(pady=10, anchor='w')
		self.cb3.config(command=lambda args=[self.underline, 'underline']: self.checkbutton_command(args))
		
		self.overstrike = tkinter.StringVar()
		self.cb4 = tkinter.Checkbutton(self.top, font=('TkDefaultFont', 10), offvalue=0, onvalue=1, text='Overstrike', variable=self.overstrike)
		self.cb4.pack(pady=10, anchor='w')
		self.cb4.config(command=lambda args=[self.overstrike, 'overstrike']: self.checkbutton_command(args))
		
		# Get current fontsize and show it in spinbox
		self.sb.delete(0, 'end')
		fontsize = self.font['size']
		self.sb.insert(0, fontsize)
		
		# Populate listbox
		for fontname in self.fontnames:
			self.lb.insert('end', fontname)
		
		# Show current fontname in listbox
		fontname = self.font.actual("family")
		fontindex = self.fontnames.index(fontname)
		self.lb.select_set(fontindex)
		self.lb.see(fontindex)
		
		# Check rest font configurations:
		self.cb1.deselect()
		self.cb2.deselect()
		self.cb3.deselect()
		self.cb4.deselect()
		
		if self.font['weight'] == 'bold': self.cb1.select()
		if self.font['slant'] == 'italic': self.cb2.select()
		if self.font['underline'] == 1: self.cb3.select()
		if self.font['overstrike'] == 1: self.cb4.select()

		self.lb.bind('<ButtonRelease-1>', self.change_font)
			
		
	def button_command(self, event=None):
		'''	In case there is not font-scaling in use by OS and
			using hdpi-screen.
		'''
		widgetlist = [
					self.optionmenu,
					self.lb,
					self.sb,
					self.cb1,
					self.cb2,
					self.cb3,
					self.cb4
					]
					
		if self.button['text'] == 'BIG':
			for widget in widgetlist:
				widget.config(font=('TkDefaultFont', 20))
			
		if self.button['text'] == 'SMALL':
			for widget in widgetlist:
				widget.config(font=('TkDefaultFont', 10))
				
		if self.button['text'] == 'BIG':
			self.button['text'] = 'SMALL'
		else:
			self.button['text'] = 'BIG'
			
			
	def checkbutton_command(self, args, event=None):
		'''	args[0] is tkinter.StringVar instance
			args[1] is string
		'''
		var = args[0]
		key = args[1]
		
		self.font[key] = var.get()
		
		
	def optionmenu_command(self, event=None):
		'''	When font(instance) is selected from optionmenu.
		'''
		self.font = tkinter.font.nametofont(self.var.get())
		fontname = self.font.actual("family")
		fontindex = self.fontnames.index(fontname)
		self.top.selection_clear()
		self.lb.select_set(fontindex)
		self.lb.see(fontindex)
		self.sb.delete(0, 'end')
		fontsize = self.font['size']
		self.sb.insert(0, fontsize)
		
		self.cb1.deselect()
		self.cb2.deselect()
		self.cb3.deselect()
		self.cb4.deselect()
		
		if self.font['weight'] == 'bold': self.cb1.select()
		if self.font['slant'] == 'italic': self.cb2.select()
		if self.font['underline'] == 1: self.cb3.select()
		if self.font['overstrike'] == 1: self.cb4.select()

		
	def change_font(self, event=None):
		'''	Change values of current font-instance.
		'''
		try:
			self.font.config(
				family=self.lb.get(self.lb.curselection()),
				size=self.sb.get()
				)
				
			if self.tracefunc:
				self.tracefunc()
				
		except tkinter.TclError as e:
			print(e)
			
			
			
			
			
			
			