#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: dschu <http://github.com/dschu-lab>
#project: SiriServer
#Randomly make a choice


from plugin import *
import re
import random
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class test(Plugin):

	res = {
		'entscheide': {
			'de-DE': u'.*(Wähle|Entscheide).*'
		}
	}

	@register("de-DE", res['entscheide']['de-DE'])
	def choose(self, speech, language):
		options = speech.replace(u"Wähle","").replace("Entscheiden","").replace("Entscheide","").replace("zwischen","")
		options = options.split("oder")
		
		if options > 0:
		    self.say(random.choice(options).title().strip());
		else:
		    self.say("Ich habe nichts zu entscheiden.")
		
		self.complete_request()