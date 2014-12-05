__author__ = 'Sergio Sicari'
__email__  = "sergiosicari@gmail.com"

import sublime, sublime_plugin
import sys,os
libraries = ["evernote", "oauth2", "httplib2", "pygments"]
abspath = os.path.abspath(os.path.dirname(__file__))
basepath = abspath
#abspath = os.path.dirname(__file__)
for library in libraries:
	if abspath+"/"+library not in sys.path:
		sys.path.append(abspath+"/"+library)	
sys.path.append(basepath)
#print(sys.path)
from settings import Local
from evercode import EverCode
from pygCode import PygCode

class EvernoteCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		extFixer = {'.py':'python'}
		# select text
		fileName, fileExtension = os.path.splitext(self.view.file_name())
		language = fileExtension.replace(".","")
		if fileExtension in extFixer:
			language = extFixer[fileExtension]
		print(language)
		sels = self.view.sel()
		selected_rows = []
		for sel in sels:
			selected_rows.append(self.view.substr(sel))

		try:
			with open("token") as file:
				token_string = file.read()
				file.close();
				if (token_string is None) or (token_string is ''):
					sublime.error_message("Your token string is Empty! Set it on token file in root directory plugin.");
					return False;
		except IOError as e:
			sublime.error_message("Your token file dosn't not exist! You need a token file on root directory plugin.");
			print "Unable to open file. Does not exist or no read permissions"
			return False

		token = token_string.strip()

		setting = Local();
		setting.developer_token = token

		self.evercode = EverCode(setting)

		code = PygCode()
		''' set language '''
		code.setLexer(language)

		''' set content '''
		# set content from selection
		source = ''.join(selected_rows)
		self.body = code.getHighLightCode(source)

		''' set title '''
		self.title = "snippet from sublime"
		self.placeholder_title = "snippet from sublime"
		self.view.window().show_input_panel("Snippet title", self.placeholder_title, self.set_title, None, None)

	def set_title(self, title):
		if not title:
			title = self.title
		''' connect to evercode account '''
		self.evercode.setClient();
		''' send snippet '''
		try:
			if self.evercode.makeNote(title, self.body) is not None:
				sublime.status_message("snippet created on evernote account")
			else: 
				sublime.status_message("snippet was empty")
		except:
			sublime.error_message('There was a problem on snippet creation!');
			return False

