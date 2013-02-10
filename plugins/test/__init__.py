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
from siriObjects.sportsObjects import SportsEntity

class test(Plugin):

	res = {
		'test': {
			'de-DE': '.*test.*'
		}
	}

	@register("de-DE", res['test']['de-DE'])
	def get_latesttest(self, speech, language):
		
		
		html = urllib.urlopen("http://blog.fefe.de/")
		soup = BeautifulSoup(html)
		
		num_tags = len(soup.find('ul').findAll("li"))
		stories = soup.find('ul').findAll("li")
		
		print num_tags
		
		
		if num_tags > 0:
		    for entry in stories:
		        #sayText = entry.text.replace("[l]","")
		        #self.say(sayText)
		        view.views = SportsEntity(image="http://shadowvision.de/blog/wp-content/gallery/lolcats/lolcat_004.jpg", name="BVB", punchout="test")
		        self.sendRequestWithoutAnswer(view)
		else:
		    print("Nichts gefunden.")
		
		self.sendRequestWithoutAnswer(view)
		self.complete_request()