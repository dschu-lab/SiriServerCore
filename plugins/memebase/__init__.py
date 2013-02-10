#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: cytec iamcytec@googlemail.com
#project: SiriServer
#german memebase plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine


class memebase(Plugin):

	res = {
		'latestmeme': {
			'de-DE': '.*neuste.*meme.*',
			'en-US': '.*latest meme.*'
		},
		'lasttroll': {
			'de-DE': '.*(problem|troll|trollface).*',
			'en-US': '.*(problem|troll|trollface).*'
		},
		'fffuuu': {
			'de-DE': '.*(fuck|fffuuu|ficken|scheiße).*',
			'en-US': '.*(fuck|fffuuu|shit|fuck you).*'
		},
		'yuno': {
			'de-DE': '.*(wieso|warum|y u no|why you no|why you know).*',
			'en-US': '.*(y u no|why you no|why you know|why you not).*'
		},
		'megusta': {
			'de-DE': '.*(me gusta|mag ich|i like).*',
			'en-US': '.*(me gusta|i like).*'
		},
		'likeaboss': {
			'de-DE': '.*(like a boss|like boss|wie ein boss|wie ein chef).*',
			'en-US': '.*(like a boss|like boss).*'
		},
		'likeasir': {
			'de-DE': '.*(like a sir|like sir|like a gentleman|wie ein gentleman|wie ein sir).*',
			'en-US': '.*(like a sir|like sir|like a gentleman).*'
		},
		'icanhaz': {
			'de-DE': '.*(lolcat|i can has|cheeseburger|lol cat).*',
			'en-US': '.*(lolcat|i can has|cheeseburger|lol cat).*'
		}
	}

	@register("de-DE", res['latestmeme']['de-DE'])
	@register("en-US", res['latestmeme']['en-US'])
	def get_latestmeme(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Latest Meme:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['lasttroll']['de-DE'])
	@register("en-US", res['lasttroll']['en-US'])
	def get_lasttroll(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/tag/troll-face")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Trollface",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['fffuuu']['de-DE'])
	@register("en-US", res['fffuuu']['en-US'])
	def get_fffuuu(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/ragecomics/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Rage:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['yuno']['de-DE'])
	@register("en-US", res['yuno']['en-US'])
	def get_yuno(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/tag/y-u-no-guy")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Y U NO:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['megusta']['de-DE'])
	@register("en-US", res['megusta']['en-US'])
	def get_megusta(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/ragecomics/tag/me-gusta")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Me gusta",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['likeaboss']['de-DE'])
	@register("en-US", res['likeaboss']['en-US'])
	def get_likeaboss(self, speech, language):
		html = urllib.urlopen("http://icanhas.cheezburger.com/tag/like-a-boss")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		print ImageURL
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Like a Boss:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['likeasir']['de-DE'])
	@register("en-US", res['likeasir']['en-US'])
	def get_likeasir(self, speech, language):
		html = urllib.urlopen("http://memebase.cheezburger.com/tag/sir")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Like a Sir",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['icanhaz']['de-DE'])
	@register("en-US", res['icanhaz']['en-US'])
	def get_icanhaz(self, speech, language):
		html = urllib.urlopen("http://icanhas.cheezburger.com/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("a", {"class": "js-img-link"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="I Can Has Cheezburger?:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()