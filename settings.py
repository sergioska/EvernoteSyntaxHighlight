__author__ = 'Sergio Sicari'
__email__  = "sergiosicari@gmail.com"

from configurations.Settings import Setting

class Local(Setting):
	def __init__(self):
		self.local = True
		self.developer_token = 'S=s193:U=1709c19:E=151482645e8:C=149f07517b0:P=1cd:A=en-devtoken:V=2:H=28b536f27005f57ecc48814f64a835e8'
		self.sandbox = False

class Local_Dev(Setting):
	def __init__(self):
		self.local = True
		self.developer_token = ''
		self.sandbox = True

class Dev(Setting):
	def __init__(self):
		self.consumer_key = ""
		self.consumer_secret = ""
		self.sandbox = False
		self.authorize_url = ""
		'''Settings.callback_url = '''

class Prod(Setting):
	def __init__(self):
		Settings.consumer_key = "consumer_key"
		Settings.consumer_secret = "consumer_secret"
		Settings.sandbox = False
		Settings.callback_url = "url"
