#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: dschu <www.github.com/dschu-lab>

from plugin import *
import urllib
import re
import random
from bs4 import BeautifulSoup

class fussballzitat(Plugin):
	res = {
        'fussballzitat': {
            'de-DE': 'fussball.*zitat.*'
        }
    }

	@register("de-DE", res['fussballzitat']['de-DE'])
	def fussballzitat(self, speech, language):
		urls = (
			"http://www.fussballerzitate.de/spieler/spieler.htm",
			"http://www.fussballerzitate.de/spieler/spieler2.htm",
			"http://www.fussballerzitate.de/spieler/spieler3.htm",
			"http://www.fussballerzitate.de/spieler/spieler4.htm",
			"http://www.fussballerzitate.de/spieler/spieler5.htm",
			"http://www.fussballerzitate.de/spieler/spieler6.htm",
			"http://www.fussballerzitate.de/trainer/trainer.htm",
			"http://www.fussballerzitate.de/trainer/trainer2.htm",
			"http://www.fussballerzitate.de/trainer/trainer3.htm",
			"http://www.fussballerzitate.de/trainer/trainer4.htm",
			"http://www.fussballerzitate.de/trainer/trainer5.htm",
			"http://www.fussballerzitate.de/trainer/trainer6.htm",
			)

		html = urllib.urlopen(random.choice(urls)).read()
		soup = BeautifulSoup(html)
		
		entries = soup.findAll("tr", {"class": ""})
		
		number = random.randint(1, len(entries))
		entry = entries[number].get_text()
		
		self.say(entry)
		self.complete_request()
