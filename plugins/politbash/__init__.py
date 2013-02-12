#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: dschu <www.github.com/dschu-lab>
# polit-bash

from plugin import *
import urllib
import re
import random
from bs4 import BeautifulSoup

class wissen(Plugin):
	res = {
        'kaspertheater': {
            'de-DE': '(Kaspertheater|Kasperltheater).*'
        },
        'kaspertop': {
            'de-DE': '.*Best of (Kaspertheater|Kasperltheater).*'
        }
    }

	@register("de-DE", res['kaspertheater']['de-DE'])
	def kaspertheater(self, speech, language):
		html = urllib.urlopen("http://polit-bash.org/index.php?p=random").read()
		soup = BeautifulSoup(html)
		zitat = soup.p.get_text()
		zitat = re.sub('#[0-9]* \(\+\|\-\)', "",zitat).strip()
		self.say(zitat)
		self.complete_request()

	@register("de-DE", res['kaspertop']['de-DE'])
	def kaspertop(self, speech, language):
		html = urllib.urlopen("http://polit-bash.org/index.php?p=top").read()
		soup = BeautifulSoup(html)
		zitat = soup.findAll("p", {"class": "quote"})
		number = random.randint(0, len(zitat))
		zitat = zitat[number].get_text()
		zitat = re.sub('#[0-9]* \(\+\|\-\)', "",zitat).strip()
		output = "Rang "+str(number + 1)+" von "+str(len(zitat) + 1)+"\r\n\r\n"
		output += zitat
		self.say(output)
		self.complete_request()