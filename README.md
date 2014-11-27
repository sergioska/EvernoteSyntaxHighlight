Evernote Syntax Highlight
=========================

Evernote Syntax Hightlight is a Sublime Text editor plugin that save code snippet with syntax hightlight in Evernote.
To install this plugin, you can clone git repository on Sublime package directory.

Install
========

1. clone git repository

    cd ~/Library/Application\ Support/Sublime\ Text 2/Packages
    git clone https://github.com/sergioska/EvernoteSyntaxHighlight.git

2. create an access token on evernote (if you don't have one yet)

go to https://www.evernote.com/Login.action?targetUrl=%2Fapi%2FDeveloperToken.action

3. add access token on settings.py

    cd ~/Library/Application Support/Sublime Text 2/Packages/EvernoteSyntaxHighlight


change this:

    self.developer_token = ''

with this:

    self.developer_token = '<access-token>'





