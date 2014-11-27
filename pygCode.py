__author__ = 'Sergio Sicari'
__email__  = "sergiosicari@gmail.com"

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class PygCode:
    def __init__(self):
        self._lexer = None
        self._formatter = HtmlFormatter(linenos=False, 
                                        noclasses=True)

    def setLexer(self, language):
        self._lexer = get_lexer_by_name(language, stripall=True)
          
    def getHighLightCode(self, code):
        result = highlight(code, self._lexer, self._formatter)
        return result

    def getFileContent(self, filename):
        in_file = open(filename,"r")
        text = in_file.read()
        in_file.close()
        return text