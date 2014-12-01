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

		setting = Local();
		if (setting.developer_token is None) or (setting.developer_token is ''):
			sublime.error_message('set your developer token in settings!')
			return False
		evercode = EverCode(setting)

		code = PygCode()
		''' set language '''
		code.setLexer(language)

		''' set content '''
		#source = code.getFileContent("evercode.py")
		# set content from selection
		source = ''.join(selected_rows)
		body = code.getHighLightCode(source)

		''' set title '''
		title = "test-da-sublime"
		sublime.Window.showInputPanel('add a title to this snippet', '', None, None, None)

		''' connect to evercode account '''
		evercode.setClient();
		''' send snippet '''
		if evercode.makeNote(title, body) is not None:
			sublime.status_message("snippet created on evernote account")
