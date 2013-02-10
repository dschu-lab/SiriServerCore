#!/usr/bin/python
# -*- coding: utf-8 -*-
# Written by Linus Yang <laokongzi@gmail.com>
# Renewed by dschu <dschu.de>

from plugin import *
import requests
import json
import re

class SimiWorker:

    def __init__(self):
        #self.cjar = cookielib.CookieJar()
        #self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cjar))
        #self.opener.addheaders = [('Referer','http://www.simsimi.com/talk.htm')]
        #try:
        #    self.opener.open('http://www.simsimi.com/talk.htm')
        #except:
        #    pass
        self.url = 'http://www.simsimi.com/func/req?lc=ch&msg=%s'

    def chat(self, message=''):
        message = message.encode('utf-8').strip()
        if message != '':
            try:
                r = requests.get("http://api.simsimi.com/request.p", params={'key': '64dc3942-e06f-4b47-8b9e-34c593409d3e', 'lc': 'de', 'text': message})
                
                
                return json.loads(r.text)['response']
            except:
                return u'Versuch es noch einmal.'
        else:
            return u'Kannst du das wiederholen？'

def respond(self, simiWorker, inputString):
    if re.match(u'.*(Ende|Stop|Klappe|Beenden).*', inputString) != None:
        self.say(u"Bis dann, {0}".format(self.user_name()))
        self.complete_request()
    else:
        answer = self.ask(simiWorker.chat(inputString))
        respond(self, simiWorker, answer)
    self.complete_request()
                              
class SimSimi(Plugin):

    @register("de-DE", u".*(Chat|Reden|Gespräch|Unterhaltung).*")
    def Simi_Message(self, speech, language):
        simiWorker = SimiWorker()
        if language == 'de-DE':
            answer = self.ask(u"Zum Beenden 'Stop Chat' oder 'Chat beenden' sagen.")
            respond(self, simiWorker, answer)
	    self.complete_request()
