#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: dschu <http://github.com/dschu-lab>
#project: SiriServer
#Displays Info about Raspberry Pi


from plugin import *
import os
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class test(Plugin):

	res = {
		'status': {
			'de-DE': u'.*status.*'
		}
	}

	@register("de-DE", res['status']['de-DE'])
	def status(self, speech, language):
	    temperature = os.popen("/opt/vc/bin/vcgencmd measure_temp").readline().strip()
	    servertype = ' '.join(os.uname())
	    uptime = os.popen("uptime").read()
	    freemem = os.popen("grep MemFree /proc/meminfo").read()
	    message = ''
	    self.say('Hier ist der Status:')
	    if servertype != None:
	        #self.say(servertype, ' ')
	        message += servertype
	        message +="\r\n\r\n"
	    if uptime != None:
	        #self.say(uptime.split(" ")[3].split(",")[0], ' ')
	        message += "Laufzeit: "+uptime.split(" ")[3].split(",")[0]
	        message +="\r\n\r\n"
	    if freemem != None:
	        message += "Freier Speicher: "+freemem.split("MemFree:")[1].strip()
	        message +="\r\n\r\n"
	    if temperature != None:
	        message += "Temperatur: "+temperature.split('=')[1].split("'")[0]+u" °C"
	        message +="\r\n\r\n"
	    
	    self.say(message)
	    self.complete_request()