#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: dschu
#project: SiriServer
#german fefe plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
import re
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class memebase(Plugin):

	res = {
		'latestfefe': {
			'de-DE': '.*fefe.*(news|nachrichten).*'
		}
	}

	@register("de-DE", res['latestfefe']['de-DE'])
	def get_latestfefe(self, speech, language):
		
		
		html = urllib.urlopen("http://blog.fefe.de/")
		soup = BeautifulSoup(html)
		
		num_tags = len(soup.find('ul').findAll("li"))
		stories = soup.find('ul').findAll("li")
		
		print num_tags
		
		
		if num_tags > 0:
		    for entry in stories:
		        sayText = entry.text.replace("[l]","")
		        self.say(sayText)
		else:
		    print("Nichts gefunden.")
		
		self.sendRequestWithoutAnswer(view)
		self.complete_request()