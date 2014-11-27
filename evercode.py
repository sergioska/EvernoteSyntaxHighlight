__author__ = 'Sergio Sicari'
__email__  = "sergiosicari@gmail.com"

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.NoteStore as NoteStore
import evernote.edam.userstore.UserStore as UserStore

class EverCode:

     def __init__(self, Settings):
          self._settings = Settings
          self._token = self._settings.developer_token

     def setClient(self):
          self._client = EvernoteClient(token=self._token, sandbox=self._settings.sandbox)
          self._userStore = self._client.get_user_store()
          self._user = self._userStore.getUser()
          self._noteStore = self._client.get_note_store()
          self._notebooks = self._noteStore.listNotebooks()
     '''
     def login(self):
          self._client = EvernoteClient(
               consumer_key = self._settings.consumer_key,
               consumer_secret = self._settings.consumer_secret,
               sandbox=self._settings.sandbox
          )
          request_token = self._client.get_request_token('YOUR CALLBACK URL')
          self._client.get_authorize_url(request_token)
          access_token = self._client.get_access_token(
               request_token['oauth_token'],
               request_token['oauth_token_secret'],
               request_token.GET.get('oauth_verifier', '')
          )
          self._token = access_token
     '''

     def makeNote(self, noteTitle, noteBody, parentNotebook=None):
 
          result = noteBody.replace('class="highlight"', '')
      
          nBody =  "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
          nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
          nBody += "<en-note>%s</en-note>" % result
      
          ## Create note object
          ourNote = Types.Note()
          ourNote.title = noteTitle
          ourNote.content = nBody
      
          ## parentNotebook is optional; if omitted, default notebook is used
          if parentNotebook and hasattr(parentNotebook, 'guid'):
               ourNote.notebookGuid = parentNotebook.guid
      
          ## Attempt to create note in Evernote account
          try:
               note = self._noteStore.createNote(self._token, ourNote)
          except Errors.EDAMUserException, edue:
               ## Something was wrong with the note data
               ## See EDAMErrorCode enumeration for error code explanation
               ## http://dev.evernote.com/documentation/reference/Errors.html#Enum_EDAMErrorCode
               print "EDAMUserException:", edue
               return None
          except Errors.EDAMNotFoundException, ednfe:
               ## Parent Notebook GUID doesn't correspond to an actual notebook
               print "EDAMNotFoundException: Invalid parent notebook GUID"
               return None
               ## Return created note object
          return note