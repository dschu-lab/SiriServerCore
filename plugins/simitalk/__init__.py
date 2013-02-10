#!/usr/bin/python
# -*- coding: utf-8 -*-
# Written by Linus Yang <laokongzi@gmail.com>
# Updated by dschu <www.dschu.de>

from plugin import *
import json
import requests
import urllib2
#import cookielib
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
        #self.url = 'http://api.simsimi.com/request.p?key=64dc3942-e06f-4b47-8b9e-34c593409d3e&lc=de&text=%s'

    def chat(self, message=''):
        message = message.encode('utf-8').strip()
        if message != '':
            try:
                r = requests.get("http://api.simsimi.com/request.p", params={'key': '64dc3942-e06f-4b47-8b9e-34c593409d3e', 'lc': 'de', 'text': message})
                print json.loads(r.text)['response']
                #r = urllib2.urlopen(self.url % message.strip()).read()
                return json.loads(r.text)['response']
            except:
                return u'Lass es mich noch einmal versuchen?!'
        else:
            return u'Kannst du das noch einmal wiederholen？'
                              
class SimiTalk(Plugin):

    @register("de-DE", u".*")
    def Simi_Message(self, speech, language):
        simiWorker = SimiWorker()
        if language == 'de-DE':
            self.say(simiWorker.chat(speech))
	    self.complete_request()
